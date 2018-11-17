from rest_framework import serializers

from todo.models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'
