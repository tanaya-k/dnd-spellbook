import json

with open('spell-list.json') as spell_list:
        data = json.load(spell_list)

class SpellsInfo:
    def __init__(self):
        self.name = data['name']
        self.desc = data['desc']
        self.duration = data['duration']
        self.level = data['level']
        self.range = data['range']

    def get_name(self):
         return self.name
    
    def get_desc(self):
         return self.desc
    
    def get_duration(self):
         return self.duration
    
    def get_level(self):
         return self.level
    
    def get_range(self):
         return self.range
    