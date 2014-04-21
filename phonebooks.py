import os
import json

class SimpleFilePhonebook(object):
    def __init__(self, filename):
        self.filename = filename
    def __getitem__(self, key):
        with open(self.filename, 'r') as f:
            return json.load(f)[key]
    def __setitem__(self, key, value):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        data[key] = value
        with open(self.filename, 'w') as f:
            json.dump(data, f)
    def __delitem__(self, key):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        del data[key]
        with open(self.filename, 'w') as f:
            json.dump(data, f)
    def reverselookup(self, number):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return [(k, v) for k, v in data.iteritems() if v == number]
    def change(self, name, number):
        del self[name]
        self[name] = number
    @classmethod
    def create(cls, filename):
        if os.path.exists(filename):
            raise IOError("phonebook already exists")
        with open(filename, 'w') as f:
            json.dump({}, f)

class FilePhonebookWithEfficientReverseLookup(object):
    def __getitem__(self, key):
        with open(self.filename, 'r') as f:
            return json.load(f)[0][key]
    def __setitem__(self, key, value):
        with open(self.filename, 'r') as f:
            data, index = json.load(f)
        data[key] = value
        if value in index:
            index[value]
        with open(self.filename, 'w') as f:
            json.dump(data, f)
    def __delitem__(self, key):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        del data[key]
        with open(self.filename, 'w') as f:
            json.dump(data, f)
    def reverselookup(self, number):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return [(k, v) for k, v in data.iteritems() if v == number]
    def change(self, name, number):
        del self[name]
        self[name] = number
    @classmethod
    def create(cls, filename):
        if os.path.exists(filename):
            raise IOError("phonebook already exists")
        with open(filename, 'w') as f:
            json.dump({}, f)
