from django.test import TestCase
from bs4 import BeautifulSoup


class DomTestMixin:

    def soup(self, res):
        return BeautifulSoup(res.content, 'html.parser')


class TopPageTest(TestCase, DomTestMixin):

    def setUp(self):
        pass

    def assert_title(self, soup, expected):
        self.assertEqual(soup.select('title')[0].text, expected)

    def test_top_page(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

        soup = self.soup(res)
        self.assert_title(soup, 'Utomica')



