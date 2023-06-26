import unittest

# Import your custom data structure implementation here
from data_structures.evolate import Evolate
from data_types import DataType, ResponseType

class YourDataStructureTest(unittest.TestCase):

    def setUp(self):
        # Create an instance of your custom data structure for testing
        self.data_structure = Evolate(DataType.SINGLY_LINKED_LIST)

    def test_add_and_get(self):
        # Add some elements to the data structure
        self.data_structure.add("value1")
        self.data_structure.add("value2")
        self.data_structure.add("value3")

        # Test the get function to retrieve the added elements
        self.assertEqual(self.data_structure.get(0).value, "value1")
        self.assertEqual(self.data_structure.get(1).value, "value2")
        self.assertEqual(self.data_structure.get(2).value, "value3")

    def test_remove(self):
        # Add some elements to the data structure
        self.data_structure.add("value1")
        self.data_structure.add("value2")
        self.data_structure.add("value3")

        # Remove an element and verify it is no longer present
        node = self.data_structure.remove(1)
        self.assertNotEqual(self.data_structure.get(1), node.value)

    def test_update(self):
        # Add an element to the data structure
        self.data_structure.add("value1")

        # Update the value of an existing element
        self.data_structure.update(0, "new_value")

        # Verify that the value has been updated
        self.assertEqual(self.data_structure.get(0).value, "new_value")

    def test_get_nonexistent_key(self):
        # Try to retrieve a value for a key that does not exist
        result = self.data_structure.get("nonexistent_key")

        # Verify that the result is None
        self.assertEqual(result, ResponseType.EMPTY_LIST)

    def test_add_and_get_multiple_data_types(self):
        # Add elements of different data types to the data structure
        self.data_structure.add("string")
        self.data_structure.add(123)
        self.data_structure.add(True)

        # Test the get function to retrieve the added elements
        self.assertEqual(self.data_structure.get(0).value, "string")
        self.assertEqual(self.data_structure.get(1).value, 123)
        self.assertEqual(self.data_structure.get(2).value, True)

    def test_remove_invalid_index(self):
        # Add some elements to the data structure
        self.data_structure.add("value1")
        self.data_structure.add("value2")

        # Try to remove an element at an invalid index
        self.assertEqual(self.data_structure.remove(2), ResponseType.NODE_NOT_FOUND)

    def test_update_invalid_index(self):
        # Add an element to the data structure
        self.data_structure.add("value1")

        # Try to update an element at an invalid index
        result = self.data_structure.update(1, "new_value")

        # Verify that the update operation fails and returns False
        self.assertEqual(result, ResponseType.NODE_NOT_FOUND)

    def test_get_size(self):
        # Add some elements to the data structure
        self.data_structure.add("value1")
        self.data_structure.add("value2")
        self.data_structure.add("value3")

        # Get the size of the data structure
        length = self.data_structure.get_length()

        # Verify that the size matches the number of added elements
        self.assertEqual(length, 3)


if __name__ == '__main__':
    unittest.main()
