from django.test import TestCase

from django.contrib.auth.models import User
from .models import Post
# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create user
        testuser1 = User.objects.create(username='testuser1', password='testpassword')
        testuser1.save()
        
        # create post
        testpost1 = Post.objects.create(author=testuser1, title='Blog title', body='Blog body')

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Blog body')