
##### all the imports here
from django.urls import path
from . import views


##### all the url here
urlpatterns = [
    path('', views.home_page, name = 'homePage'),
    # path('showTask/', views.show_task, name = 'showTaskPage'),
    path('addTask/', views.add_task, name = 'addTaskPage'),
]
