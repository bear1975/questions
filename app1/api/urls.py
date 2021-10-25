from django.urls import path

from .api_views import ViewType, ViewGroup, ViewTask, ViewTList, ViewQuest,  ViewReadQuest, ViewValueQuest, ViewWork, ViewCMD, ViewUserQuest



urlpatterns = [
    path('cmd/', ViewCMD.as_view()),
    path('types/', ViewType.as_view()),

    path('groups/', ViewGroup.as_view()),
    path('groups/<int:pk>', ViewGroup.as_view()),

    path('tasks/', ViewTask.as_view()),
    path('tasks/<int:pk>', ViewTask.as_view()),

    path('tlist/', ViewTList.as_view()),
    path('tlist/<int:pk>', ViewTList.as_view()),

    path('quests/', ViewQuest.as_view()),
    path('quests/<int:pk>', ViewQuest.as_view()),
    
    path('tests/', ViewQuest.as_view()),
    path('tests/<int:pk>', ViewQuest.as_view()),

    path('work/', ViewWork.as_view()),
    path('work/<int:pk>', ViewWork.as_view()),
    
    path('quest_read/<int:pk>', ViewReadQuest.as_view()),
    path('quest_view/<int:pk>', ViewValueQuest.as_view()),
    path('quest_view/', ViewUserQuest.as_view())


]
