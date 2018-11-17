from django.urls import reverse
from drftest import BaseAuthenticatedViewTest
from rest_framework.permissions import IsAuthenticated

from todo.views import ToDoItemViewSet


# TODO: Create auth providers

class CreateToDoItemViewTest(BaseAuthenticatedViewTest):
    def _make_url(self, kwargs=None):
        return reverse('todo:items-list', kwargs=kwargs)

    def _get_view_class(self):
        return ToDoItemViewSet

    def _get_permission_classes(self):
        return [IsAuthenticated]


class EditToDoItemViewTest(BaseAuthenticatedViewTest):
    def _make_url(self, kwargs=None):
        return reverse('todo:items-detail', kwargs=kwargs)

    def _get_view_class(self):
        return ToDoItemViewSet

    def _get_permission_classes(self):
        return [IsAuthenticated]

    def _get_default_url_kwargs(self):
        return {'pk': 1}
