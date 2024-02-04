import os
from schema_generator import generate_schema

if __name__ == "__main__":
    # Using __file__ attribute to get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))


    # provide data faile paths relative to the script's directory
    input_file_path_1 = os.path.join(script_dir, "../data/data_1.json")
    output_file_path_1 = os.path.join(script_dir, "../schema/schema_1.json")

    input_file_path_2 = os.path.join(script_dir, "../data/data_2.json")
    output_file_path_2 = os.path.join(script_dir, "../schema/schema_2.json")

    generate_schema(input_file_path_1, output_file_path_1)
    generate_schema(input_file_path_2, output_file_path_2)