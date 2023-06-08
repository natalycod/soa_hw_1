import json
import sys
import argparse
import dicttoxml
import xmltodict
import yaml
import avro

from dataclasses_avroschema import AvroModel
from rec_avro import to_rec_avro_destructive

def json_to_dict(js : json):
    obj = json.loads(json.dumps(js), object_hook=dict)
    return obj

def dict_to_json(d):
    s = json.dumps(d)
    return json.loads(s)

def dict_to_xml(d):
    return dicttoxml.dicttoxml(d)

def xml_to_dict(x):
    return xmltodict.parse(x)

def dict_to_yaml(d):
    return yaml.dump(d)

def dict_to_avro(d):
    class Temp(AvroModel):
        def __init__(self, dic):
            vars(self).update(dic)

    res = Temp(d)
    return res.avro_schema()

def read_json(filename):
    f = open(filename)
    js = json.loads(f.read())
    f.close()
    return js

class Solver:
    def __init__(self, data):
        self.d = data

    def get_dict_memory(self):
        return sys.getsizeof(self.d)
    
    def get_xml_memory(self):
        return sys.getsizeof(dict_to_xml(self.d))

    def get_json_memory(self):
        return sys.getsizeof(dict_to_json(self.d))
    
    def get_yaml_memory(self):
        return sys.getsizeof(dict_to_yaml(self.d))

    def get_avro_memory(self):
        return sys.getsizeof(dict_to_avro(self.d))

argparser = argparse.ArgumentParser()
argparser.add_argument(
    '--file',
    required=True,
    help='path to json file for testing'
)

argparser.add_argument(
    '--test_type',
    required=True,
    help='type which you want to test ("native", "xml", "json", "avro", "yaml")'
)

args = argparser.parse_args()
filename = args.file
test_type = args.test_type
s = Solver(json_to_dict(read_json(filename)))

if test_type == "native":
    print(s.get_dict_memory())
elif test_type == "json":
    print(s.get_json_memory())
elif test_type == "xml":
    print(s.get_xml_memory())
elif test_type == "yaml":
    print(s.get_yaml_memory())
elif test_type == "avro":
    print(s.get_avro_memory())
else:
    print("Sorry, this test_type is not supported now")
