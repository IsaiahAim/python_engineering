
# Python Engineer-Talent Pipeline.
A python  genertic program that Reads a JSON file, 
Sniffs the schema of the JSON file and 
Dumps the output in (./schema/)

The program recursively processes the JSON object and updates the schema.  The unique key for each iteration is obtained from the full key path. For example:
    
    obj = {
        "battle": {
            "id": "ABCDEFGHIJKLMNOPQR",
            "name": "ABCDEFGHIJKLMNOPQRSTUVWX",
        }
    }
The respective keys will be 
```
"battle", "battle.id", "battle.name".
```
This ensures the uniqueness of the keys incase there are clashing keys with the same character with the json imput. 




## Documentation
There are 4 main python files wich are located in the service dirctory
  - **helpers.py file**: it contains three main functions
  process_object, process_array, update_schema_properties and get_data_type, all of these functions help in sniffing and tagging keys to a new schema.
  
  - **Schema_generator.py file**: it contains the  ```generate_schema``` method, which is responsible for opening the the json documents. It uses the ```process_object``` method in helpers file to handle the process.

  - **main.py file**: It serves as the entry point to the service. it uses  ```__file__``` attribute to get the script's directory and provide data file paths relative to the script's directory

- **test.py file**: The file contains unitest for the service


## Installation and Usage

To run the projeect, you don't need a virtual environment since there are not third parties services used. However you can create and activate  a virtual environtment by running the commands below. Please use the command based on your os version

**Linux / macOS**:
```

To Create a virtual environment
python3 -m venv venv

Activate the virtual environment
source venv/bin/activate


```
**Windows**
```
Create a virtual environment
python -m venv venv

Activate the virtual environment
venv\Scripts\activate
```

## Generate Schema

To generate the schema
-  navigate to the service directory
  ```cd service```

- run the python command based on the version and configuration of python on your machine

```
python service/main.py 
or 
python3 service/main.py 
```



When the file run succesfully the ```schema_1.json and schema_2.json``` files will be populated with the output with new json which is the output of the sniffed files  ```data_1.json and data_2.json```


## Run the test file

- navigate to the service directory 

  ```cd service```
- Run the python command
  ```
  python -m unittest test.py 

  ```







    