from django.test import TestCase
from .forms import PostForm, RegistrationForm


class TestPostForm(TestCase):

    def test_fields_required(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        post = PostForm()
        self.assertEqual(post.Meta.fields, ('title', 'genre', 'content',))