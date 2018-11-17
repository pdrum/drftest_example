from django.contrib.auth.models import User
from rest_framework import viewsets

from todo.serializers import ToDoItemSerializer


class ToDoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ToDoItems to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = ToDoItemSerializer
