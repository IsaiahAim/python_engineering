import json
import logging

from helpers import process_object

# Constants
ENUM_ARRAY_TYPE = "enum array"
ARRAY_TYPE = "array"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_schema(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            json_data = json.load(f)

        schema = {}  # initialize an empty schema
        schema = process_object(schema, json_data["message"])

        with open(output_file, 'w') as f:
            json.dump(schema, f, indent=2)

        logger.info(f"Schema generated and saved to {output_file}")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON: {e}")
    except Exception as e:
        logger.error(f"Default Exceptions: {e}")
