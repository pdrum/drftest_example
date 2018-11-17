from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo.models import ToDoItem
from todo.serializers import ToDoItemSerializer


class ToDoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ToDoItems to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
