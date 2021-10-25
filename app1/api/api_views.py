from django.db.models.base import Model
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from ..models import Types, Groups, Tasks, Quests, TList, Work
from .serializers import TypeSerializer, GroupSerializer, TaskSerializer, QuestSerializer, TListSerializer, WorkSerializer, TaskPassSerializer,  ClientGroupSerializer

import time
import random
import json

#---------------------------------------------------------------------------------------------

class TableControl(APIView):
    def __init__(self,Model,ModelSerializer):
        self.Model = Model
        self.ModelSerializer = ModelSerializer

    def get(self, request,*args, **kwargs):
        objs = self.Model.objects.all()
        serializer = self.ModelSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        serializer = self.ModelSerializer(data = request.data)
        if serializer.is_valid():
            saved = serializer.save() 
            return Response({'success':True})       
        return Response({'success':False})
        
    def put(self, request, pk):
        data = request.data

        obj = self.Model.objects.filter(id=pk)        
        fields =[f.name for f in self.Model._meta.get_fields()]
        
        values = obj.values()[0]

        for f in fields:
            if f not in values.keys():
                values[f] = values['%s_id'%f]
                del values['%s_id'%f]
        del values['id']

        for d in data:
            values[d] = data[d]

        obj = get_object_or_404(self.Model.objects.all(), pk=pk)
        serializer = self.ModelSerializer(instance=obj, data = values)

        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()
            return Response({'success':True,'id':pk})
        return Response({'success':False, 'msg':'почему-то не работает, если не все поля ообновлять!???'})
        
    def delete(self, request, pk):
        obj = get_object_or_404(self.Model.objects.all(), pk=pk)
        obj.delete()
        return Response({"message": "Group with id `{}` has been deleted.".format(pk)}, status=204)
        
#---------------------------------------------------------------------------------------------

class ViewGroup(TableControl):
    def __init__(self):
        super(ViewGroup, self).__init__(Groups, GroupSerializer)
        
class ViewTask(TableControl):
    def __init__(self):
        super(ViewTask, self).__init__(Tasks, TaskSerializer)
        
class ViewTList(TableControl):
    def __init__(self):
        super(ViewTList, self).__init__(TList,  TListSerializer)

class ViewQuest(TableControl):
    def __init__(self):
        super(ViewQuest, self).__init__(Quests,  QuestSerializer)
        
class ViewWork(TableControl):
    def __init__(self):
        super(ViewWork, self).__init__(Work,  WorkSerializer)

#---------------------------------------------------------------------------------------------

class ViewType(APIView):
    def get(self, request):
        objs = Types.objects.all()
        serializer = TypeSerializer(objs, many=True)
        return Response(serializer.data)

#---------------------------------------------------------------------------------------------

class ViewReadQuest(APIView):
    def get(self, request, pk):
       
        quest = Quests.objects.get(id=pk)
        group = Groups.objects.get(id=quest.group_id)
        tasks = Tasks.objects.filter(group=group)

        serializer = GroupSerializer(tasks, many=True)

        return Response(serializer.data)

#---------------------------------------------------------------------------------------------

class ViewUserQuest(APIView):
    def get(self, request):
        if 'user_id' not in request.query_params:
            return Response('Добавьте в запрос параметр user_id')
        user_id = request.query_params.get('user_id')
        
        quests = Quests.objects.filter(user_auth=user_id)
        data_all = []
        for quest in quests:
            #return Response(quest.name)
            works = Work.objects.filter(quest=quest)            
            serializer = TaskPassSerializer(works, many=True)

            for data in serializer.data:
                data['task'] = Tasks.objects.get(id=data['task']).name
            data_all.append({quest.name:serializer.data})
        return Response(data_all)

#---------------------------------------------------------------------------------------------

class ViewValueQuest(APIView):
    def get(self, request, pk):
       
        quest = Quests.objects.get(id=pk)
        works = Work.objects.filter(quest=quest)
        serializer = TaskPassSerializer(works, many=True)

        for data in serializer.data:
            data['task'] = Tasks.objects.get(id=data['task']).name
        data = {quest.name:serializer.data}
        return Response(data)


#---------------------------------------------------------------------------------------------
def post(data,ModelSerializer):    
    serializer = ModelSerializer(data = data)
    return {'success': serializer.is_valid(),'serializer':serializer}

def create_form(data):
    group_js = {'name':data['name']}
    group = post(group_js,GroupSerializer)
    if not group['success']:
        return {'success':False}

    ids = {}
    group_saved = group['serializer'].save()

    ids['group'] = group_saved.id
    ids['tasks'] = []
    ids['tlist'] = []

    tasks_js = data['tasks']

    for task_js in tasks_js:
        t = {
            "group":group_saved.id,
            "name":task_js['task'],
            "ttype":task_js['type']
        }
        task = post(t,TaskSerializer)
        if task['success']:
            task_saved = task['serializer'].save()
            ids['tasks'].append(task_saved.id)

            for l in task_js['list']:
                type_js = {'task':task_saved.id,'name':l}
                ttype = post(type_js,TListSerializer)
                if ttype['success']:
                    type_saved = ttype['serializer'].save()
                    ids['tlist'].append(type_saved.id)

    return {'success':True, 'ids':ids}

def create_quest(data):
    user_auth = 'user_' + str(int(time.time())) + str(random.randint(0,1000))

    if 'user_auth' not in data:
        data['user_auth'] = user_auth

    serializer = QuestSerializer(data = data)
    if serializer.is_valid():
        saved = serializer.save()   

        tasks = Tasks.objects.filter(group=data['group'])

        rows = []
        for t in tasks:
            rows.append(Work(quest = saved,task=t.id))
        Work.objects.bulk_create(rows)
        return {"success":True, 'quest_id':saved.id}

    return {"success": False}



class ViewCMD(APIView):
    def post(self, request):
        data = request.data        

        if 'cmd' not in data:
            return  Response({'success':False,'msg':'Поле \'cmd\' не найдено'})        
        
        if data['cmd'] == 'create_form':
            ret = create_form(data['data'])
            return Response(ret)

        if data['cmd'] == 'create_quest':
            ret = create_quest(data['data'])
            return Response(ret)
 
        return Response({'success':False})



