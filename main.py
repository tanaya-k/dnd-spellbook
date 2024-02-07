import json

with open("spell-list.json") as spell_list:
    all_spells = json.load(spell_list)


# Generate jsons for the different classes
bard_spells = []
cleric_spells = []
druid_spells = []
paladin_spells = []
ranger_spells = []
sorcerer_spells = []
warlock_spells = []
wizard_spells = []
for spell in all_spells:
    if "bard" in spell['classes']:
        bard_spells.append(spell)
    if "cleric" in spell['classes']:
        cleric_spells.append(spell)
    if "druid" in spell['classes']:
        druid_spells.append(spell)
    if "paladin" in spell['classes']:
        paladin_spells.append(spell)
    if "ranger" in spell['classes']:
        ranger_spells.append(spell)
    if "sorcerer" in spell['classes']:
        sorcerer_spells.append(spell)
    if "warlock" in spell['classes']:
        warlock_spells.append(spell)
    if "wizard" in spell['classes']:
        wizard_spells.append(spell)

with open("bard-spell-list.json", "w") as spell_list:
    json.dump(bard_spells, spell_list, indent = 6)
with open("cleric-spell-list.json", "w") as spell_list:
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
    json.dump(wizard_spells, spell_list, indent = 6)