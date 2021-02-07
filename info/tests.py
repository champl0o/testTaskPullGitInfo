import vcr
import requests
from django.test import TestCase

class GitApiTest(TestCase):

    @vcr.use_cassette('fixtures/cassetes/usernamegit_get.yaml')
    def test_git_username(self):
        responce = requests.get('https://api.github.com/users/champl0o')
        self.assertEqual(responce.status_code, 200)
