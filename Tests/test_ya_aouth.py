from unittest import TestCase
from ya_aouth import ya_aouth, login,password

class TestYaAouth(TestCase):
    def setUp(self) -> None:
        print("method setUp")

    def tearDown(self) -> None:
        print('method tearDown')

    def test_ya_aouth(self):
        self.assertEqual(ya_aouth(login,password),'login')