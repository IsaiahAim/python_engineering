import unittest
from helpers import get_data_type, process_object


class TestSchemaGenerator(unittest.TestCase):
    def test_get_data_type_string(self):
        data_type = get_data_type("id", "ABCDEFGHIJKLMNOPQR")
        self.assertEqual(data_type, "string")

    def test_get_data_type_integer(self):
        data_type = get_data_type("minParticipants", 942)
        self.assertEqual(data_type, "integer")

    def test_get_data_type_enum_array(self):
        data_type = get_data_type("participantIds", ["participants", "participants", "participants3"])
        self.assertEqual(data_type, "enum array")

    def test_get_data_type_array(self):
        data_type = get_data_type("creator", [{"id": "ABCDEFGHIJKLMNOPQRSTUVWXYZA"}])
        self.assertEqual(data_type, "array")

    def test_process_object_without_mock(self):
        schema = {}
        json_data = {"message": {"key": "value"}}
        result_schema = process_object(schema, json_data["message"])
        self.assertEqual(result_schema, {"key": {"type": "string", "tag": "", "description": "", "required": False}})


if __name__ == '__main__':
    unittest.main()
