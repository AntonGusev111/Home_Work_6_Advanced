import unittest
from unittest import TestCase
from ya_path import ya_folder,check_folder, token, path
import time


class TestYafolder(TestCase):
    def setUp(self) -> None:
        print("method setUp")

    def tearDown(self) -> None:
        print('method tearDown')

    @unittest.skipIf(check_folder(path, token)=='<Response [200]>','path alredy exists')
    def test_ya_path(self):
       self.assertEqual(ya_folder(path, token),'<Response [201]>')

    @unittest.skipIf(check_folder(path, token)=='<Response [404]>','path does not exist')
    def test_check_folder(self):
        self.assertEqual(check_folder(path, token),'<Response [200]>')

    @unittest.expectedFailure
    def test_check_folder_failure(self):
        self.assertEqual(check_folder(path, token),'<Response [20212]>')

    def test_path_fail_token(self):
        self.assertEqual(check_folder(path, 'token'), '<Response [401]>')

    def test_fail_incorrect_data(self):
        self.assertEqual(check_folder(path,token,preview_size='asdad32e41414'),'<Response [400]>')

    def test_fail_API_URL(self):
        self.assertEqual(check_folder(path,token,v='v2'),'<Response [403]>')

    def test_fail_server(self):
        self.assertEqual(check_folder(path,token,Accept='123application/json'), '<Response [500]>')

