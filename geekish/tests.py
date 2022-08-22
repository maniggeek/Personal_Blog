# blog/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class TestPost(TestCase):


    def setUp(self):
        Post.objects.create(
        title ='nice title',
        paragraph_1 ='nice body'
        )

    ##test__string_representation
    def test_string_representation(self):
        post = Post(title='nice title')
        self.assertEqual(str(post),post.title)
    ##test_post_content use 'f{self}'

    def test_post_content(self):
        post = Post(title='nice title',paragraph_1='nice body')

        self.assertEqual(f'{post.title}','nice title')
        self.assertEqual(f'{post.paragraph_1}','nice body')

    #test_post_list view with client.get(reverse())
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    #test test_post_detail client.get('/post/1') and 404
    #and contains and template used

    def test_post_detail_view(self):
        response = self.client.get('/post/30/')
        no_response = self.client.get('/post/100000/')

        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'nice title')
        self.assertTemplateUsed(response,'post_detail.html')
