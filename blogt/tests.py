from django.test import TestCase
from.models import Blog_Post
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Blogtest(TestCase):
    # @classmethod
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.post_test = Blog_Post.objects.create(title='title', text='text', author=self.user,
                        status=Blog_Post.STATUS_CHOICES[0][0])
        self.post2 =Blog_Post.objects.create(title='title2', text='text', status=Blog_Post.STATUS_CHOICES[1][0],
                                            author=self.user)
    def test_blogpost_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
    def test_blogpost_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
    def test_blogpost_title(self):
        response = self.client.get('/blog/')
        self.assertContains(response, self.post_test.title)
        self.assertContains(response, self.post_test.text)
    def test_postdetail_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
    def test_post_name(self):
        response = self.client.get(reverse('post detail', args=[1]))
        self.assertEqual(response.status_code, 200)
    def test_post_title_text(self):
        response = self.client.get('/blog/1/')
        self.assertContains(response, self.post_test.text)
        self.assertContains(response, self.post_test.title)

    def test_get_object(self):
        response = self.client.get(reverse('post detail', args=[999]))
        self.assertEqual(response.status_code, 404)
    def test_draft_post_not_show(self):
        response = self.client.get(reverse('blog'))
        self.assertContains(response, self.post_test.title)
        self.assertNotContains(response, self.post2.title)
    def test_creat_str_post(self):
        post = self.post_test
        self.assertEqual(str(post), post.text)
    def test_title_post(self):
        self.assertEqual(self.post_test.title, 'title')
        self.assertEqual(self.post_test.text, 'text')
        self.assertEqual(self.post_test.author, self.user)
        self.assertEqual(self.post_test.status, Blog_Post.STATUS_CHOICES[0][0])
    def test_new_postform_view(self):
        response = self.client.post(reverse('newpost'), {
            'title': 'this is my title',
            'text': 'text1',
            'status': 'pub',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog_Post.objects.last().title, 'this is my title')
        self.assertEqual(Blog_Post.objects.last().text, 'text1')
        self.assertEqual(Blog_Post.objects.last().status, 'pub')
        self.assertEqual(Blog_Post.objects.last().author, self.user)
    def test_update_view(self):
        response = self.client.post(reverse('update', args=[self.post2.id]), {
            'title': 'title updated',
            'text': 'text updated',
            'status': 'pub',
            'author': self.user.id,

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog_Post.objects.last().title, 'title updated')
        self.assertEqual(Blog_Post.objects.last().author, self.user)
        self.assertEqual(Blog_Post.objects.last().text, 'text updated')
    def test_deletepost_view(self):
        response = self.client.post(reverse('delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)




























