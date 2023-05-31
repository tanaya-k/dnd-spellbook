from enum import Enum

classes = ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"]

# Input format, classType is the variable that can be used with print now
classType = input("Please type the name of your class: ")
classType = classType.upper()

if classType in classes:
    match classType:
        case "BARD":
            print(classes[0] + " Spells")
        case "CLERIC":
            print(classes[1] + " Spells")
        case "DRUID":
            print(classes[2] + " Spells")
        case "PALADIN":
            print(classes[3] + " Spells")
        case "RANGER":
            print(classes[4] + " Spells")
        case "SORCERER":
            print(classes[5] + " Spells")
        case "WARLOCK":
            print(classes[6] + " Spells")
        case "WIZARD":
            print(classes[7] + " Spells")
else: print("No/Invalid Input")
