import unittest.mock
from unittest import TestCase
from unittest import mock
from accounting import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, \
    add_new_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, show_all_docs_info, add_new_doc, \
    append_doc_to_shelf


class TestAccounting(TestCase):

    @classmethod
    def setUp(self) -> None:
        print("method setUp")

    @classmethod
    def tearDown(self) -> None:
        print('method tearDown')

    def test_show_all_docs_info(self):
        self.assertEqual(show_all_docs_info(), ['Список всех документов:', 'passport "2207 876234" "Василий Гупкин"',
                                                'invoice "11-2" "Геннадий Покемонов"',
                                                'insurance "10006" "Аристарх Павлов"'])

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance('11-2'), True)

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf(10), (10, True))

    @mock.patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name(), "Геннадий Покемонов")

    def test_append_doc_to_shelf(self):
        self.assertEqual(append_doc_to_shelf('123-21', '3'), 'document 123-21 add to 3')

    @mock.patch('builtins.input', lambda *args: '2207 876234')
    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf(), '1')

    @mock.patch('builtins.input', side_effect=['10006', '3'])
    def test_move_doc_to_shelf(self, mock_inputs):
        self.assertEqual(move_doc_to_shelf(), 'Документ номер "10006" был перемещен на полку номер "3"')

    @mock.patch('builtins.input', side_effect=['9', 'd lessons', 'Random Person', '1'])
    def test_add_new_doc(self, mock_inputs):
        self.assertEqual(add_new_doc(), '1')

    @mock.patch('builtins.input', lambda *args: '9')
    def test_delete_doc(self):
        self.assertEqual(delete_doc(), ('9', True))

    def test_remove_doc_from_shelf(self):
        self.assertEqual(remove_doc_from_shelf('10006'), 'documet 10006 deleted ')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), ['Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'])

    @unittest.mock.patch('builtins.input', lambda *args: '7')
    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf(), ('7', True))
