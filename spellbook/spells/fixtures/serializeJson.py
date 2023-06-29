import json

# Change the json to a full spell list

with open("spells.json") as spell_list:
    spells = json.load(spell_list)

# [bard(1), cleric(2), druid(3), plaldin(4), ranger(5), sorcerer(6), warlock(7), wizard(8)]

# Generate jsons for the different classes
spell_arr = []
count = 1

for spell in spells:
    
    # format to fixture
    class_arr = []

    if "bard" in spell['classes']:
        class_arr.append(1)
    if "cleric" in spell['classes']:
        class_arr.append(2)
    if "druid" in spell['classes']:
        class_arr.append(3)
    if "paladin" in spell['classes']:
        class_arr.append(4)
    if "ranger" in spell['classes']:
        class_arr.append(5)
    if "sorcerer" in spell['classes']:
        class_arr.append(6)
    if "warlock" in spell['classes']:
        class_arr.append(7)
    if "wizard" in spell['classes']:
        class_arr.append(8)

    spell_dict = {
        "model": "spells.Spell",
        "pk": count,
        "fields": {
            "name": spell['name'],
            "classes": class_arr,
            "description": spell['description'],
            "duration": spell['duration'],
            "level": spell['level'],
            "range": spell['range'],
            "fave": False,
        }
    }

    count = count + 1
    spell_arr.append(spell_dict)

    """
    {
        "model": "myapp.person",
        "pk": 1,
        "fields": {
            "first_name": "John",
            "last_name": "Lennon"
        }
    },
    """

with open("spells.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)