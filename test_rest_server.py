from unittest import TestCase
from unittest.mock import patch, Mock
import rest_server
from pprint import pprint


class RestServerRecipeTests(TestCase):
    @patch('libs.database.findOne')
    def test_get(self, mock_find_one):
        mock_find_one().return_value = [
            {
                'id': 1,
                'test_key1': 'test_value1',
                'test_key2': 'test_value2',
                'test_key3': 'test_value3',
                'test_key4': 'test_value4',
            }
        ]

        response = rest_server.Recipe.get(self, 1)

        self.assertIsNotNone(response)
        self.assertIsInstance(response[0]()[0], dict)
        self.assertEqual(response[1], 200)


    @patch('libs.database.deleteOne')
    def test_delete(self, mock_delete_one):
        mock_delete_one().return_value = {}

        response = rest_server.Recipe.delete(self, 1)
        self.assertIsNotNone(response)
        self.assertEqual(response[0], 'document deleted')
        self.assertEqual(response[1], 204)

class RestServerRecipeListTests(TestCase):
    @patch('libs.database.find')
    def test_get(self, mock_find):
        mock_find().return_value = [
            {
                'id': 1,
                'test_key1': 'test_value1',
                'test_key2': 'test_value2',
                'test_key3': 'test_value3',
                'test_key4': 'test_value4',
            }
        ]

        response = rest_server.RecipeList.get(self)

        self.assertIsNotNone(response)
        self.assertIsInstance(response[0]()[0], dict)
        self.assertEqual(response[1], 200)









