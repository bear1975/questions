from django.db import models

# Create your models here.

#---------------------------------------------------------------------------------------------

class Types(models.Model):
    name = models.CharField('Тип ответа',max_length=30)
    def __str__(self):
        return self.name

#---------------------------------------------------------------------------------------------

class Groups(models.Model):
    name = models.CharField('Имя группы',max_length=30)
    
    def __str__(self):
        return self.name

#---------------------------------------------------------------------------------------------

class Tasks(models.Model):
    group = models.ForeignKey(Groups, related_name='tasks', on_delete = models.PROTECT)
    name = models.CharField('Вопрос',max_length=150)
    ttype = models.ForeignKey(Types, on_delete = models.PROTECT)

    def __str__(self):
        return self.name
#---------------------------------------------------------------------------------------------

class TList(models.Model):
    task = models.ForeignKey(Tasks, on_delete = models.PROTECT)
    name = models.CharField('Имя группы',max_length=30)

    def __str__(self):
        return self.name

#---------------------------------------------------------------------------------------------

class Quests(models.Model):
    name = models.CharField('Наименование анкеты',max_length=30)
    user_auth = models.CharField('Id пользователя', max_length=200,null=True)
    group = models.ForeignKey(Groups, on_delete = models.CASCADE)
    time_begin = models.DateTimeField('Начальная дата',auto_now_add=True)
    time_end = models.DateTimeField('Коечная дата', auto_now=True)
    description = models.CharField('Описание анкеты',max_length=150, null=True)

    def __str__(self):
        return self.name

#---------------------------------------------------------------------------------------------

class Work(models.Model):
    quest = models.ForeignKey(Quests, on_delete = models.CASCADE)
    task = models.IntegerField()
    value = models.TextField('Ответ', null=True)
