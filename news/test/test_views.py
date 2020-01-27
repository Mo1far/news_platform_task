from django.test import TestCase
from django.urls import reverse

from news.models import News
from users.models import User


class HomePageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        activated_user = User.objects.create(email='test1@test.com', password='test_pass2', is_active=True)

        published_news = News.objects.create(content='PUBLISHED news by activated user',
                                             title='test', author=activated_user,
                                             status='PUBLISHED')
        unpublished_news = News.objects.create(content='UNPUBLISHED news by activated user',
                                               title='test', author=activated_user,
                                               status='UNPUBLISHED')
        waiting_confirmation_news = News.objects.create(content='WAITING_CONFIRMATION news by activated user',
                                                        title='test', author=activated_user,
                                                        status='WAITING_CONFIRMATION')

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        response = self.client.get('/news/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('news:main'))
        self.assertEquals(resp.status_code, 200)

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('news:main'))
        self.assertTemplateUsed(resp, 'news/home.html')

    def test_published_news_from_activated_user_show(self):
        resp = self.client.get(reverse('news:main'))
        self.assertContains(resp, 'PUBLISHED news by activated user', status_code=200)

    def test_unpublished_news_from_activated_user_not_show(self):
        resp = self.client.get(reverse('news:main'))
        self.assertNotContains(resp, 'UNPUBLISHED news by activated user', status_code=200)

    def test_wait_confirmation_news_from_activated_user_not_show(self):
        resp = self.client.get(reverse('news:main'))
        self.assertNotContains(resp, 'WAITING_CONFIRMATION news by activated user', status_code=200)

    def test_pagination_on_1_news_not_show(self):
        resp = self.client.get(reverse('news:main'))
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.context['is_paginated'])

    def test_pagination_on_15_news_show(self):
        activated_user = User.objects.create(email='testpagination@test.com', password='test_pass2', is_active=True)

        for i in range(15):
            news = News.objects.create(content=f'PUBLISHED news {i} by activated user',
                                       title='test', author=activated_user,
                                       status='PUBLISHED')
            news.save()

        resp = self.client.get(reverse('news:main'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['is_paginated'])

        self.assertEquals(len(resp.context['news_list']), 3)


class NewsDetailTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        activated_user = User.objects.create(email='test1@test.com', password='test_pass2', is_active=True)

        published_news = News.objects.create(content='PUBLISHED news by activated user',
                                             title='test', author=activated_user,
                                             status='PUBLISHED')

    def test_detail_page_status_code(self):
        resp = self.client.get('/news/1/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('news:detail', kwargs={'pk': 1}))
        self.assertEquals(resp.status_code, 200)

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('news:detail', kwargs={'pk': 1}))
        self.assertTemplateUsed(resp, 'news/news_detail.html')

    def test_view_on_nonexistent_news(self):
        resp = self.client.get(reverse('news:detail', kwargs={'pk': 999}))
        self.assertEquals(resp.status_code, 404)

    def test_comment_form_available(self):
        resp = self.client.get(reverse('news:detail', kwargs={'pk': 1}))
        self.assertIsNotNone(resp.context['comment_form'])


class NewsCreateTest(TestCase):

    def test_detail_page_status_code(self):
        resp = self.client.get('/create/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('news:create'))
        self.assertEquals(resp.status_code, 200)

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('news:detail', kwargs={'pk': 1}))
        self.assertTemplateUsed(resp, 'news/news_create.html')
