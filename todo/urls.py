from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from todo.views import ToDoItemViewSet

app_name = 'todo'

router = routers.DefaultRouter()
router.register(r'/todo-items', ToDoItemViewSet, 'items')

urlpatterns = [
    url(r'^', include(router.urls)),
]
