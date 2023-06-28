import json

# change the json to a full spell list


with open("bard-spell-list.json", "r+") as bard_spell_list:
    bard_spells = json.load(bard_spell_list)
""" with open("cleric-spell-list.json", "w") as cleric_spell_list:
    cleric_spells = json.load(cleric_spell_list)
with open("druid-spell-list.json", "w") as druid_spell_list:
    druid_spells = json.load(druid_spell_list)
with open("paladin-spell-list.json", "w") as paladin_spell_list:
    paladin_spells = json.load(paladin_spell_list)
with open("ranger-spell-list.json", "w") as ranger_spell_list:
    ranger_spells = json.load(ranger_spell_list)
with open("sorcerer-spell-list.json", "w") as sorcerer_spell_list:
    sorcerer_spells = json.load(sorcerer_spell_list)
with open("warlock-spell-list.json", "w") as warlock_spell_list:
    warlock_spells = json.load(warlock_spell_list)
with open("wizard-spell-list.json", "w") as wizard_spell_list:
    wizard_spells = json.load(wizard_spell_list) """

# Generate jsons for the different classes
bard_spell_arr = []
cleric_spells_arr = []
druid_spells_arr = []
paladin_spells_arr = []
ranger_spells_arr = []
sorcerer_spells_arr = []
warlock_spells_arr = []
wizard_spells_arr = []

for spell in bard_spells:
    count = 1
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
    bard_spell_arr.append(spell_dict)

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

with open("bard-spell-list.json", "w") as spell_list:
    json.dump(bard_spell_arr, spell_list, indent = 6)
""" with open("cleric-spell-list.json", "w") as spell_list:
    json.dump(cleric_spells, spell_list, indent = 6)
with open("druid-spell-list.json", "w") as spell_list:
    json.dump(druid_spells, spell_list, indent = 6)
with open("paladin-spell-list.json", "w") as spell_list:
    json.dump(paladin_spells, spell_list, indent = 6)
with open("ranger-spell-list.json", "w") as spell_list:
    json.dump(ranger_spells, spell_list, indent = 6)
with open("sorcerer-spell-list.json", "w") as spell_list:
    json.dump(sorcerer_spells, spell_list, indent = 6)
with open("warlock-spell-list.json", "w") as spell_list:
    json.dump(warlock_spells, spell_list, indent = 6)
with open("wizard-spell-list.json", "w") as spell_list:
    json.dump(wizard_spells, spell_list, indent = 6) """