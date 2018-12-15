from django.contrib.auth.models import User
from django.urls import reverse
from drftest import BaseAuthenticatedViewTest
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from todo.models import ToDoItem
from todo.views import ToDoItemViewSet


class CreateToDoItemTest(BaseAuthenticatedViewTest):
    """
    This endpoint creates to-do items
    """

    def setUp(self):
        super().setUp()
        self.user = User.objects.create(username='u1')

    def _make_url(self, kwargs=None):
        return reverse('todo:items-list', kwargs=kwargs)

    def _get_view_class(self):
        return ToDoItemViewSet

    def _get_permission_classes(self):
        return [IsAuthenticated]

    def test_successful_creation(self):
        response = self._post_for_response(user=self.user, data={
            'name': 'First',
            'is_done': True,
        })
        self.assertSuccess(response)
        self.assertIn('id', response.data, 'Id should be serialized in response')
        self.assertEqual(response.data['name'], 'First')

    def test_without_name(self):
        """
        `name` should be provided in request body.
        """
        response = self._post_for_response(user=self.user, data={
            'is_done': True
        })
        self.assertStatus(response, status.HTTP_400_BAD_REQUEST)


class EditToDoItemTest(BaseAuthenticatedViewTest):
    """
    This endpoint edits to-do items.
    """

    def setUp(self):
        super().setUp()
        self.user = User.objects.create(username='u1')
        self.item = ToDoItem.objects.create(name='Foo')

    def _make_url(self, kwargs=None):
        return reverse('todo:items-detail', kwargs=kwargs)

    def _get_view_class(self):
        return ToDoItemViewSet

    def _get_permission_classes(self):
        return [IsAuthenticated]

    def _get_default_url_kwargs(self):
        return {'pk': 1234}  # Some random value for the required path parameter.

    def test_successful_edit(self):
        response = self._put_for_response(
            user=self.user,
            data={
                'name': 'Bar',
                'is_done': True,
            },
            url_kwargs={'pk': self.item.id}
        )
        self.assertSuccess(response)
        self.assertIn('id', response.data, 'Id should be serialized in response')
        self.assertEqual(response.data['name'], 'Bar')

    def test_when_name_is_missing(self):
        """
        `name` should be provided in request body.
        """
        response = self._put_for_response(
            user=self.user,
            data={
                'is_done': True,
            },
            url_kwargs={'pk': self.item.id}
        )
        self.assertStatus(response, status.HTTP_400_BAD_REQUEST)

    def test_when_id_does_not_exist(self):
        """
        `id` should correspond to an existing to-do item.
        """
        response = self._put_for_response(
            user=self.user,
            data={
                'name': 'Bar',
                'is_done': True,
            },
            url_kwargs={'pk': 53353}
        )
        self.assertStatus(response, status.HTTP_404_NOT_FOUND)


class DeleteToDoItemViewTest(BaseAuthenticatedViewTest):
    """
    This endpoint deletes to-do items.
    """

    def setUp(self):
        super().setUp()
        self.user = User.objects.create(username='u1')
        self.item = ToDoItem.objects.create(name='Foo')

    def _make_url(self, kwargs=None):
        return reverse('todo:items-detail', kwargs=kwargs)

    def _get_view_class(self):
        return ToDoItemViewSet

    def _get_permission_classes(self):
        return [IsAuthenticated]

    def _get_default_url_kwargs(self):
        return {'pk': 1234}  # Some random value for the required path parameter.

    def test_successful_deletion(self):
        response = self._delete_for_response(user=self.user, url_kwargs={
            'pk': self.item.id
        })
        self.assertStatus(response, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(ToDoItem.DoesNotExist):
            self.item.refresh_from_db()

    def test_when_id_does_not_exist(self):
        response = self._delete_for_response(user=self.user, url_kwargs={
            'pk': 34536
        })
        self.assertStatus(response, status.HTTP_404_NOT_FOUND)
