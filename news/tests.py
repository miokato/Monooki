import factory

from django.test import TestCase

from .models import News


class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News

    title = 'ジャンプに載りました。'
    url = 'example.com'
    pub_date = '2018-03-14'


class TestNews(TestCase):
    def setUp(self):
        self.news = NewsFactory.create()

    def test_collect_field_name(self):
        self.assertEqual(self.news.title, 'ジャンプに載りました。')
        self.assertEqual(self.news.url, 'example.com')
        self.assertEqual(self.news.pub_date, '2018-03-14')

    def test_save_object(self):
        self.assertEqual(News.objects.count(), 1)
