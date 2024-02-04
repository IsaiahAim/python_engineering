import logging

# Constants
ENUM_ARRAY_TYPE = "enum array"
ARRAY_TYPE = "array"

# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_object(schema, obj, path=''):
    """
     Recursively processes the JSON object and updates the schema. 

    The unique key for each iteration is obtained from the full key path.
    For example:
    obj = {
        "battle": {
            "id": "ABCDEFGHIJKLMNOPQR",
            "name": "ABCDEFGHIJKLMNOPQRSTUVWX",
        }
    }
    
    The respective keys will be "battle", "battle.id", "battle.name".
    This ensures the uniqueness of the keys.
    """
    for key, value in obj.items():
        full_path = f"{path}{key}"
        logger.debug(f"Processing: {full_path}")
        if isinstance(value, dict):
            update_schema_properties(schema, full_path, value)
            process_object(schema, value, f"{full_path}.")
        elif isinstance(value, list):
            process_array(schema, value, full_path)
        else:
            update_schema_properties(schema, full_path, value)
    return schema


def process_array(schema, array, full_path):
    """
    Process arrays within the JSON object.
    """
    update_schema_properties(schema, full_path, array)
    if array and isinstance(array[0], dict):
        process_object(schema, array[0], f"{full_path}.")
    else:
        update_schema_properties(schema, full_path, array)


def update_schema_properties(schema, full_path, value):
    """
    Update the schema properties based on the data type and add
    padding with "tag" and "description" keys to schema properties.
    """
    data_type = get_data_type(full_path, value)
    schema[full_path] = {
        "type": data_type,
        "tag": "",
        "description": "",
        "required": False
    }
    return schema


def get_data_type(key, value):
    """
    Returns the data type of the value.
    """
    logger.debug(f"Identifying data type for: {key}")
    if isinstance(value, str):
        return "string"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, list) and all(isinstance(item, str) for item in value):
        return ENUM_ARRAY_TYPE
    elif isinstance(value, list) and all(isinstance(item, dict) for item in value):
        return ARRAY_TYPE
    else:
        return "object"
