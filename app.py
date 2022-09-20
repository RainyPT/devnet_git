import json
import unittest
class CustomParser:
    
    def parseJson(self):
        with open("data.json","r") as jsonfile:
            data=json.load(jsonfile)
            name=data['user']['name']
            return name

class TestParse(unittest.TestCase):
    def test_parse_user_name(self):
        cp=CustomParser()
        expectedName="Rainy"
        parsedName=cp.parseJson()
        self.assertEqual(expectedName,parsedName)
