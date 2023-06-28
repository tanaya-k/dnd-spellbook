import json

# change the json to a full spell list

"""with open("bard-spell-list.json") as bard_spell_list:
    spells = json.load(bard_spell_list)
with open("cleric-spell-list.json") as cleric_spell_list:
    spells = json.load(cleric_spell_list)
with open("druid-spell-list.json") as druid_spell_list:
    spells = json.load(druid_spell_list)
with open("paladin-spell-list.json") as paladin_spell_list:
    spells = json.load(paladin_spell_list)
with open("ranger-spell-list.json") as ranger_spell_list:
    spells = json.load(ranger_spell_list)
with open("sorcerer-spell-list.json") as sorcerer_spell_list:
    spells = json.load(sorcerer_spell_list)
with open("warlock-spell-list.json") as warlock_spell_list:
    spells = json.load(warlock_spell_list)"""
with open("wizard-spell-list.json") as wizard_spell_list:
    spells = json.load(wizard_spell_list)

# Generate jsons for the different classes
spell_arr = []
count = 1

for spell in spells:
    
    # format to fixture

    spell_dict = {
        "model": "spells.Spell",
        "pk": count,
        "fields": {
            "name": spell['name'],
            "classes": spell['classes'],
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

"""with open("bard-spell-list.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)
with open("cleric-spell-list.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)
with open("druid-spell-list.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)
with open("paladin-spell-list.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)
with open("ranger-spell-list.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)
with open("sorcerer-spell-list.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)
with open("warlock-spell-list.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)"""
with open("wizard-spell-list.json", "w") as spell_list:
    json.dump(spell_arr, spell_list, indent = 6)