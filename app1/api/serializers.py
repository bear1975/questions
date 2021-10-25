from rest_framework import serializers

from ..models import Types, Groups, Tasks, Quests, TList, Work

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = "__all__"

#---------------------------------------------------------------------------------------------

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"
    
    def create(self, validated_data):
        return Work.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.quest = validated_data.get('quest', instance.quest)
        instance.value = validated_data.get('value', instance.value)

        instance.save()
        return instance

#---------------------------------------------------------------------------------------------

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"

    def create(self, validated_data):
        return Groups.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

#---------------------------------------------------------------------------------------------

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"
    
    def create(self, validated_data):
        return Tasks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ttype = validated_data.get('ttype', instance.ttype)
        instance.group = validated_data.get('group', instance.group)
        instance.save()
        return instance

#---------------------------------------------------------------------------------------------

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quests
        fields = "__all__"

    def create(self, validated_data):
        return Quests.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.user_noauth = validated_data.get('user_noauth', instance.user_noauth)
        instance.user_auth = validated_data.get('user_auth', instance.user_auth)
        instance.group = validated_data.get('group', instance.group)
        instance.time_begin = validated_data.get('time_begin', instance.time_begin)
        instance.time_end = validated_data.get('time_end', instance.time_end)
        instance.escriptin = validated_data.get('escriptin', instance.escriptin)
        instance.save()
        return instance

#---------------------------------------------------------------------------------------------

class TListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TList
        fields = "__all__"

    def create(self, validated_data):
        return TList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

#---------------------------------------------------------------------------------------------

class TaskReadSerializer(serializers.ModelSerializer):
    task_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = Tasks
        fields = "__all__"
        


#---------------------------------------------------------------------------------------------

class TaskPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'task', 'value']
        

#---------------------------------------------------------------------------------------------

class ClientGroupSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Groups
        fields = ['id','name','tasks']#"__all__"
        