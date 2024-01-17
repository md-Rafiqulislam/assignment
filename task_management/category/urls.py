

##### all the imports here
from django.urls import path
from . import views

##### all the urls here
urlpatterns = [
    path('', views.add_category, name = 'addCategory'),
]
