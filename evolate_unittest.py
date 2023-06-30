import unittest

# Import your custom data structure implementation here
from data_structures.evolate import Evolate
from data_types import DataType, ResponseType

class YourDataStructureTest(unittest.TestCase):

    def setUp(self):
        # Create an instance of your custom data structure for testing
        self.data_structure = Evolate(DataType.TREE_MAP)

    def test_add(self):
        self.data_structure.add("value1")

        self.assertEqual(self.data_structure.get(0).get_value(), "value1")

    def test_multiple_add(self):
        self.data_structure.add("value1")
        self.data_structure.add("value2")

        self.assertEqual(self.data_structure.get(0).get_value(), "value1")
        self.assertEqual(self.data_structure.get(1).get_value(), "value2")

    def test_empty_get(self):
        response = self.data_structure.get(0)

        self.assertEqual(response, ResponseType.EMPTY_LIST)

    def test_first_element_get(self):
        self.data_structure.add("value1")
        response = self.data_structure.get(0)

        self.assertEqual(response.get_value(), "value1")
    
    def test_index_out_of_bounds(self):
        self.data_structure.add("value1")

        response = self.data_structure.get(1)

        self.assertEqual(response, ResponseType.NODE_NOT_FOUND)
    
    def test_multiple_get(self):
        self.data_structure.add("value1")
        self.data_structure.add("value2")
        self.data_structure.add("value3")

        self.assertEqual(self.data_structure.get(0).get_value(), "value1")
        self.assertEqual(self.data_structure.get(1).get_value(), "value2")
        self.assertEqual(self.data_structure.get(2).get_value(), "value3")

    def test_remove_empty(self):
        response = self.data_structure.remove(0)

        self.assertEqual(response, ResponseType.EMPTY_LIST)
    
    def test_remove_one(self):
        self.data_structure.add("value1")
        res = self.data_structure.remove(0)

        self.assertEqual(res.get_value(), "value1")
        self.assertEqual(self.data_structure.get_length(), 0)
    
    def test_remove_index_out_of_bounds(self):
        self.data_structure.add("value1")

        res = self.data_structure.remove(1)

        self.assertEqual(res, ResponseType.NODE_NOT_FOUND)

    def test_remove_multiple(self):
        self.data_structure.add("value1")
        self.data_structure.add("value2")
        self.data_structure.add("value3")

        res = self.data_structure.remove(1)

        self.assertEqual(res.get_value(), "value2")
        self.assertEqual(self.data_structure.get(0).get_value(), "value1")
        self.assertEqual(self.data_structure.get(1).get_value(), "value3")
        self.assertEqual(self.data_structure.get_length(), 2)

    def test_multiple_remove(self):
        self.data_structure.add("value1")
        self.data_structure.add("value2")
        self.data_structure.add("value3")

        res = self.data_structure.remove(1)

        res2 = self.data_structure.remove(1)

        self.assertEqual(res.get_value(), "value2")
        self.assertEqual(res2.get_value(), "value3")
        self.assertEqual(self.data_structure.get(0).get_value(), "value1")
        self.assertEqual(self.data_structure.get_length(), 1)

    def test_update_empty(self):
        res = self.data_structure.update(0, "temp")

        self.assertEqual(res, ResponseType.EMPTY_LIST)

    def test_update_one(self):
        self.data_structure.add("value1")

        res = self.data_structure.update(0, "value2")

        self.assertEqual(res, ResponseType.SUCCESS)
        self.assertEqual(self.data_structure.get(0).get_value(), "value2")
    
    def test_update_multiple(self):
        self.data_structure.add("value1")
        self.data_structure.add("value2")
        self.data_structure.add("value3")

        res = self.data_structure.update(1, "value4")

        self.assertEqual(res, ResponseType.SUCCESS)
        self.assertEqual(self.data_structure.get(1).get_value(), "value4")
    
    def test_mulitple_update(self):
        self.data_structure.add("value1")
        self.data_structure.add("value2")
        self.data_structure.add("value3")

        res = self.data_structure.update(1, "value4")
        res2 = self.data_structure.update(2, "value5")

        self.assertEqual(res, ResponseType.SUCCESS)
        self.assertEqual(self.data_structure.get(1).get_value(), "value4")
        self.assertEqual(res2, ResponseType.SUCCESS)
        self.assertEqual(self.data_structure.get(2).get_value(), "value5")
    
    def test_update_out_of_bounds(self):
        self.data_structure.add("value1")

        res = self.data_structure.update(3, "value2")

        self.assertEqual(res, ResponseType.NODE_NOT_FOUND)
        self.assertEqual(self.data_structure.get(0).get_value(), "value1")

if __name__ == '__main__':
    unittest.main()
