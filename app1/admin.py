from django.contrib import admin
# Register your models here.


from .models import Types, Groups, Tasks, Quests, TList, Work

admin.site.register(Types)
admin.site.register(Groups)
admin.site.register(Tasks)
admin.site.register(Quests)
admin.site.register(TList)
admin.site.register(Work)

