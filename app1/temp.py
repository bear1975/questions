firlds = [
    "id",
    "quest",
    "task",
    "value"
]

values = {
    "id": 1,
    "quest_id": 22,
    "task": 16,
    "value": "name1"
}
for f in firlds:
    if f not in values.keys():
        values[f] = values['%s_id'%f]
        del values['%s_id'%f]


for d in values:
    d1 = d.replace('_id', '')
    d[d1] = d.pop(d)


data = {"value":"name10"}

list_ids = []

for v in values:
    vv = v.replace("_id", "")
    if vv != v:
        values[vv] = values[v]


for d in data:
    dr = str(d).replace('_id','')
    values[dr] = data[dr]

print(values)


aaa = "qqq_id"
bbb = aaa.replace("_iaad","")


a = {'a1':'a11'}
k = a.keys()

b= a.copy()
a['b1'] = a.get("b1","b1")




b='b1'
a.b = 'b11'

print(a)
print()


{
    "task_id": 3,
    "name": "Мужской",
}

{
    "name": "quest1",
    "group": 1,
    "descriptin": "Пробная анкета 1"
}


{
    "cmd":"create_form",
    "data":
    {
        "name":"form1",
        "tasks":
        [
            {
                "task":"ФИО",
                "type":"1",
                "list":[]
            },
            {
                "task":"Национальность",
                "type":"1",
                "list":[]
            },
            {
                "task":"Пол",
                "type":"2",
                "list":
                [
                    "Мужчина",
                    "Женщина"
                ]
            },
             {
                "task":"Увлечения",
                "type":"3",
                "list":
                [
                    "Спорт",
                    "Кино",
                    "Музыка",
                    "Рисование"
                ]
            }
        ]
    }
}


{
    "cmd":"create_quest",
    "data":
    {
        "name":"quest1",
        "group":"39",
        "description":"Тест для Иванова И.И."
    }
}
{
    "value":"Иванов Иван Иванович"    
}

{
    "id":"19",
    "value":[1,3]    
}

{
    "value":"name1"
}


{
    "task": 16,
    "value": "asd",
    "quest": 22
}

{
    "task": 16,
    "value": "name2",
    "quest": 22
}


"WorkSerializer(data={'name': 'name1'},                         instance=<Work: Work object (1)>):\n    id = IntegerField(label='ID', read_only=True)\n    task = IntegerField()\n    value = CharField(allow_null=True, label='Ответ', required=False, style={'base_template': 'textarea.html'})\n    quest = PrimaryKeyRelatedField(queryset=Quests.objects.all())"
"WorkSerializer(data={'task': 16, 'value': 'asd', 'quest': 22}, instance=<Work: Work object (1)>):\n    id = IntegerField(label='ID', read_only=True)\n    task = IntegerField()\n    value = CharField(allow_null=True, label='Ответ', required=False, style={'base_template': 'textarea.html'})\n    quest = PrimaryKeyRelatedField(queryset=Quests.objects.all())"