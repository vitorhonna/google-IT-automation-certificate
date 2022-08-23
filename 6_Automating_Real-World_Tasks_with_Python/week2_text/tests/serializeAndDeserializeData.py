import yaml
import json

####################################################
# Python object

people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]
print()

####################################################
# YAML

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)
# print(people_yaml)

####################################################
# JSON

# Serialize a Python object and create a file
with open('people.json', 'w') as people_json_file:
    json.dump(people, people_json_file, indent=2)
# print(people_json_file)

# Deserialize a file and create a Python object
with open('people.json', 'r') as people_json_file:
    people_objectFromFile = json.load(people_json_file)
    print(type(people_objectFromFile))
    print(people_objectFromFile)
print(people_objectFromFile[0]['name'])

# Serialize a Python object and create a string
people_json_string = json.dumps(people, indent=2)
# print(people_json_string)

# Deserialize a string and create a Python object
people_objectFromString = json.loads(people_json_string)
print()
print(type(people_objectFromString))
print(people_objectFromString)
print(people_objectFromString[1]['name'])

