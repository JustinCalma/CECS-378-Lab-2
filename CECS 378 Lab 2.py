# Justin Calma
# CECS 378 - 9
# MW 8 AM - 10:15 AM
# Lab 2 - Malware

# Declare variable that will store the address of my save file
save = "C:\\DOSBox\\Ultima_5\\Ultima_5\\SAVED.GAM"

# Declare variables that will store the max amount for each stat
max1Byte = chr(99)
firstMax2Byte999 = 231
secondMax2Byte999 = 3
firstMax2Byte9999 = 15
secondMax2Byte9999 = 39

# Function that will write into the save file and update the desired stat
# Function takes in the read file, the offset of the selected stat and the value of the desired stat
def statChanger(file, offset, stat):

    # Seek the offset of the desired stat
    file.seek(offset, 0)

    # Update the current stat to be the desired value
    # write() takes in a string value, so convert the ascii value to a string before writing
    # Opened the file as a binary file, so when writing a bytes-like object is required use .encode() on the string
    file.write(str(stat).encode())

    # Output a simple message to the user
    print("The 1 byte length stat has been updated... \n")


# Function that will write into the save file and update the desired stat
# Similar to the statChanger() function;
# however, this function overwrites a stat that has a length of 16 bites / (2 Bytes)
# Writes the value in little Endian notation
def twoByteStatChanger(file, offset1, offset2, stat1, stat2):

    # Seek the first offset of the desired stat
    file.seek(offset1, 0)

    # Update the current stat to be the desired value
    # write() takes in a string value, so convert the ascii value to a string before writing
    # Opened the file as a binary file, so when writing a bytes-like object is required use .encode() on the string
    file.write(bytes([stat1]))

    # Repeat for the offset2 and stat2
    file.seek(offset2, 0)
    file.write(bytes([stat2]))

    # Output a simple message to the user
    print("The 2 byte length stat has been updated... \n")

# Function that will be used for all 15 party members
# Determine if the user wants to update the current stat with an inputted value
# This function will take in the desired stat value and overwrite the old value with the new one
# This is used for the 8 bit or 2 byte length stat values
def determineOneByteStat(file, offset):

    # Determine if the user wants to update the current stat
    yesOrNo = input("(Y/N): ")

    # If the user wants to change the current stat value
    if (yesOrNo == "Y" or yesOrNo == "y"):

        # Get the input from the user
        newStat = int(input("Enter the desired value for the current stat (0-99): "))

        # Convert the input of the user to the ASCII value so it can be written into the save file
        asciiNewStat = chr(newStat)

        # Call the statChanger() function to save the new stat
        statChanger(file, offset, asciiNewStat)

# This function will be used for all 15 party members
# Determine if the user wants to update the current stat with an inputted value
# This function will take in the desired stat value and overwrite the old value with the new one
# This is used for the 16 bit or 2 byte length stat values
def determineTwoByteStat(file, offset1, offset2):

    # Determine if the user wants to update the current stat
    yesOrNo = input("(Y/N): ")

    # If the user wants to change the current stat value
    if (yesOrNo == "Y" or yesOrNo == "y"):

        # Prompt the user to enter their desired new stat and save it
        newStat = int(input("Enter the desired value for the current stat (HP & MAX HP: 0-999) or (EXP: 0-9999): "))
        x = format(newStat, "#04x")
        hexNewStat = int(x, 16)
        y = hexNewStat.to_bytes(2, 'little')
        twoByteStatChanger(file, offset1, offset2, y[0], y[1])

# Definition of the main function
def main():

    # Output messages to the user at the start of the program
    print("Ultima V: Save File Editor")
    print("Enter the address of the save file: ")

    # Open the binary save file for reading and writing
    file = open(save, "rb+")

    # Keep looping until the user decides to quit the program
    while (True):

        # Output the options of the user
        print("-----------------------------------------------------------------------\n"
              " \n1: Update the stats of your main character"
              " \n2: Update the stats of your party members"
              " \n3: Set all stats of your main character and party members to max"
              " \n4: Receive 100 KEYS in your inventory"
              " \n5: Receive 100 SKULL KEYS in your inventory"
              " \n6: Receive 100 GEMS in your inventory"
              " \n7: Receive 1 BLACK BADGE in your inventory"
              " \n8: Receive 2 MAGIC CARPETS in your inventory"
              " \n9: Receive 10 MAGIC AXES in your inventory"
              "\n10: Change amount received for options 4-9"
              "\n Enter any character to quit the program")

        print("-----------------------------------------------------------------------\n")

        # Prompt the user for their desired option and save it into a variable
        userInput = input("Enter the number corresponding to the desired option or press any key to quit: ")

        # ---------------------------------------- Selection 1 ----------------------------------------#

        # If the user has chosen option 1. Update the desired stats of the Main Character
        if (userInput == "1"):

            # STRENGTH --> 8 bit / 1 byte
            # Determine if the user wants to update the Strength stat
            yesOrNo = input("Do you want to update the Strength stat? (Y/N): ")

            # Update the Strength stat if the user wants to
            if (yesOrNo == "Y" or yesOrNo == "y"):

                # Prompt the user to input their desired stat for Strength
                strength = int(input("Enter the desired Strength value for your character (0-99): "))

                # Convert the input of the user to the ASCII value so it can be written into the save file
                asciiStrength = chr(strength)

                # Call the statChanger function to update the Strength stat to the desired value
                # Offset 0x0000000E => 14 in decimal
                statChanger(file, 14, asciiStrength)

            # Repeat the process for the rest of the 1 byte length stats
            # DEXTERITY => 8 bit / 1 byte
            yesOrNo = input("Do you want to update the Dexterity stat? (Y/N): ")
            if (yesOrNo == "Y" or yesOrNo == "y"):
                dexterity = int(input("Enter the desired Dexterity value for your character (0-99): "))
                asciiDexterity = chr(dexterity)
                # Offset 0x0000000F => 15 in decimal
                statChanger(file, 15, asciiDexterity)

            # INTELLIGENCE => 8 bit / 1 byte
            yesOrNo = input("Do you want to update the Intelligence stat? (Y/N): ")
            if (yesOrNo == "Y" or yesOrNo == "y"):
                intelligence = int(input("Enter the desired Intelligence value for your character (0-99): "))
                asciiIntelligence = chr(intelligence)
                # Offset 0x00000010 => 16 in decimal
                statChanger(file, 16, asciiIntelligence)

# ---------------------------------------- 2 Byte length values ----------------------------------------#

            # HEALTH => 16 bits / 2 bytes
            yesOrNo == input("Do you want to update the Health stat? (Y/N): ")
            if (yesOrNo == "Y" or yesOrNo == "y"):
                health = int(input("Enter the desired Health value for your character (0-999): "))

                # Format the input value as a 2 digit hexadecimal string with leading zeros to make up the length
                x = format(health, "#04x")

                # Convert the string x to an integer with a base of 16
                hexHealth = int(x, 16)

                # Return an array of bytes representing the hex value of Health (In little Endian notation)
                y = hexHealth.to_bytes(2, 'little')

                # Offset 0x00000012 & 0x00000013 => 18 & 19 in decimal
                twoByteStatChanger(file, 18, 19, y[0], y[1])

            # Repeat the process for the rest of the 2 byte length stats
            # MAX HP => 16 bits / 2 bytes
            yesOrNo == input("Do you want to update the Max HP stat? (Y/N): ")
            if (yesOrNo == "Y" or yesOrNo == "y"):
                maxHP = int(input("Enter the desired Maximum HP value for your character (0-999): "))
                x = format(maxHP, "#04x")
                hexMaxHP = int(x, 16)
                y = hexMaxHP.to_bytes(2, 'little')
                # Offset 0x00000014 & 0x00000015 => 20 & 21 in decimal
                twoByteStatChanger(file, 20, 21, y[0], y[1])

            # EXPERIENCE => 16 bits / 2 bytes
            yesOrNo == input("Do you want to update the Experience stat? (Y/N): ")
            if (yesOrNo == "Y" or yesOrNo == "y"):
                experience = int(input("Enter the desired Experience value for your character (0-9999): "))
                x = format(experience, "#04x")
                hexExperience = int(x, 16)
                y = hexExperience.to_bytes(2, 'little')
                # Offset 0x00000016 & 0x00000017 => 22 & 23 in decimal
                twoByteStatChanger(file, 22, 23, y[0], y[1])

            # GOLD => 16 bits / 2 bytes
            yesOrNo == input("Do you want to update the amount of Gold? (Y/N): ")
            if (yesOrNo == "Y" or yesOrNo == "y"):
                gold = int(input("Enter the desired Gold value for your character (0-9999): "))
                x = format(gold, "#04x")
                hexGold = int(x, 16)
                y = hexGold.to_bytes(2, 'little')
                # Offset 0x00000204 & 0x00000205 => 516 & 517 in decimal
                twoByteStatChanger(file, 516, 517, y[0], y[1])

            # Output a simple message to the user
            print("All stats of the main character have been updated...\n")
            print("Returning to the menu...\n")

# ---------------------------------------- Selection 2 ----------------------------------------#

        elif (userInput == "2"):

            # Keep looping until the user decides to quit
            while (True):

                # Output a simple menu to the user
                print("-----------------------------------------------------------------------\n"
                      " \n1: Shamino"
                      " \n2: Iolo"
                      " \n3: Mariah"
                      " \n4: Geoffrey"
                      " \n5: Jaana"
                      " \n6: Julia"
                      " \n7: Dupre"
                      " \n8: Katrina"
                      " \n9: Sentri"
                      "\n10: Gwenno"
                      "\n11: Johne"
                      "\n12: Gorn"
                      "\n13: Maxwell"
                      "\n14: Toshi"
                      "\n15: Saduj"
                      "\n16: Amount of Gold the party has"
                      "\n Enter any key to return to the menu")

                print("-----------------------------------------------------------------------\n")

                userInput = input("Enter the number corresponding to the desired option or press any key to return to the main menu: ")

                # ---------------------------------------- Shamino ----------------------------------------#

                # If the user selects to update the stats of Shamino
                # Perform the same actions as the MC; however, use the offsets containing Shamino's stats
                if (userInput == "1"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    # Determine if the user wants to update the Strength stat of Shamino
                    print("Do you wish to update the Strength stat of Shamino? ")

                    # Call the oneByteStatPartyMembers() function to check if the user wants to change the current stat or not
                    # If yes then update the current stat with the desired value
                    determineOneByteStat(file, 0x002E)

                    # Repeat for the rest of Shamino's stats
                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Shamino? ")
                    determineOneByteStat(file, 0x002F)

                    # INTELLIGENCE
                    print("Do you wish to update the Intelligence stat of Shamino? ")
                    determineOneByteStat(file, 0x0030)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Shamino? ")
                    determineTwoByteStat(file, 0x0032, 0x0033)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Shamino? ")
                    determineTwoByteStat(file, 0x0034, 0x0035)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Shamino? ")
                    determineTwoByteStat(file, 0x0036, 0x0037)

                    print("All stats of Shamino have been updated...")

                # ---------------------------------------- Iolo ----------------------------------------#

                # The user decided to update the stats of Iolo
                elif (userInput == "2"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Iolo? ")
                    determineOneByteStat(file, 0x004E)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Iolo? ")
                    determineOneByteStat(file, 0x004F)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Iolo? ")
                    determineOneByteStat(file, 0x0050)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Iolo? ")
                    determineTwoByteStat(file, 0x0052, 0x0053)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Iolo? ")
                    determineTwoByteStat(file, 0x0054, 0x0055)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Iolo? ")
                    determineTwoByteStat(file, 0x0056, 0x0057)

                    print("All stats of Iolo have been updated...")

                # ---------------------------------------- Mariah ----------------------------------------#

                # The user decided to update the stats of Mariah
                elif (userInput == "3"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Mariah? ")
                    determineOneByteStat(file, 0x006E)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Mariah? ")
                    determineOneByteStat(file, 0x006F)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Mariah? ")
                    determineOneByteStat(file, 0x0070)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Mariah? ")
                    determineTwoByteStat(file, 0x0072, 0x0073)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Mariah? ")
                    determineTwoByteStat(file, 0x0074, 0x0075)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Mariah? ")
                    determineTwoByteStat(file, 0x0076, 0x0077)

                    print("All stats of Mariah have been updated...")

                # ---------------------------------------- Geoffrey ----------------------------------------#

                # The user decided to update the stats of Geoffrey
                elif (userInput == "4"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Geoffrey? ")
                    determineOneByteStat(file, 0x008E)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Geoffrey? ")
                    determineOneByteStat(file, 0x008F)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Geoffrey? ")
                    determineOneByteStat(file, 0x0090)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Geoffrey? ")
                    determineTwoByteStat(file, 0x0092, 0x0093)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Geoffrey? ")
                    determineTwoByteStat(file, 0x0094, 0x0095)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Geoffrey? ")
                    determineTwoByteStat(file, 0x0096, 0x0097)

                    print("All stats of Geoffrey have been updated...")

                # ---------------------------------------- Jaana ----------------------------------------#

                # The user decided to update the stats of Jaana
                elif (userInput == "5"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Jaana? ")
                    determineOneByteStat(file, 0x00AE)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Jaana? ")
                    determineOneByteStat(file, 0x00AF)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Jaana? ")
                    determineOneByteStat(file, 0x00B0)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Jaana? ")
                    determineTwoByteStat(file, 0x00B2, 0x00B3)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Jaana? ")
                    determineTwoByteStat(file, 0x00B4, 0x00B5)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Jaana? ")
                    determineTwoByteStat(file, 0x00B6, 0x00B7)

                    print("All stats of Jaana have been updated...")

                # ---------------------------------------- Julia ----------------------------------------#

                # The user decided to update the stats of Julia
                elif (userInput == "6"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Julia? ")
                    determineOneByteStat(file, 0x00CE)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Julia? ")
                    determineOneByteStat(file, 0x00CF)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Julia? ")
                    determineOneByteStat(file, 0x00D0)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Julia? ")
                    determineTwoByteStat(file, 0x00D2, 0x00D3)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Julia? ")
                    determineTwoByteStat(file, 0x00D4, 0x00D5)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Julia? ")
                    determineTwoByteStat(file, 0x00D6, 0x00D7)

                    print("All stats of Julia have been updated...")

                # ---------------------------------------- Dupre ----------------------------------------#

                # The user decided to update the stats of Dupre
                elif (userInput == "7"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Dupre? ")
                    determineOneByteStat(file, 0x00EE)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Dupre? ")
                    determineOneByteStat(file, 0x00EF)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Dupre? ")
                    determineOneByteStat(file, 0x00F0)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Dupre? ")
                    determineTwoByteStat(file, 0x00F2, 0x00F3)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Dupre? ")
                    determineTwoByteStat(file, 0x00F4, 0x00F5)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Dupre? ")
                    determineTwoByteStat(file, 0x00F6, 0x00F7)

                    print("All stats of Dupre have been updated...")

                # ---------------------------------------- Katrina ----------------------------------------#

                # The user decided to update the stats of Katrina
                elif (userInput == "8"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Katrina? ")
                    determineOneByteStat(file, 0x010E)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Katrina? ")
                    determineOneByteStat(file, 0x010F)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Katrina? ")
                    determineOneByteStat(file, 0x0110)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Katrina? ")
                    determineTwoByteStat(file, 0x0112, 0x0113)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Katrina? ")
                    determineTwoByteStat(file, 0x0114, 0x0115)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Katrina? ")
                    determineTwoByteStat(file, 0x0116, 0x0117)

                    print("All stats of Katrina have been updated...")

                # ---------------------------------------- Sentri ----------------------------------------#

                # The user decided to update the stats of Sentri
                elif (userInput == "9"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Sentri? ")
                    determineOneByteStat(file, 0x012E)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Sentri? ")
                    determineOneByteStat(file, 0x012F)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Sentri? ")
                    determineOneByteStat(file, 0x0130)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Sentri? ")
                    determineTwoByteStat(file, 0x0132, 0x0133)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Sentri? ")
                    determineTwoByteStat(file, 0x0134, 0x0135)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Sentri? ")
                    determineTwoByteStat(file, 0x0136, 0x0137)

                    print("All stats of Sentri have been updated...")

                # ---------------------------------------- Gwenno ----------------------------------------#

                # The user decided to update the stats of Gwenno
                elif (userInput == "10"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Gwenno? ")
                    determineOneByteStat(file, 0x014E)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Gwenno? ")
                    determineOneByteStat(file, 0x014F)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Gwenno? ")
                    determineOneByteStat(file, 0x0150)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Gwenno? ")
                    determineTwoByteStat(file, 0x0152, 0x0153)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Gwenno? ")
                    determineTwoByteStat(file, 0x0154, 0x0155)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Gwenno? ")
                    determineTwoByteStat(file, 0x0156, 0x0157)

                    print("All stats of Gwenno have been updated...")

                # ---------------------------------------- John ----------------------------------------#

                # The user decided to update the stats of John
                elif (userInput == "11"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of John? ")
                    determineOneByteStat(file, 0x016E)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of John? ")
                    determineOneByteStat(file, 0x016F)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of John? ")
                    determineOneByteStat(file, 0x0170)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of John? ")
                    determineTwoByteStat(file, 0x0172, 0x0173)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of John? ")
                    determineTwoByteStat(file, 0x0174, 0x0175)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of John? ")
                    determineTwoByteStat(file, 0x0176, 0x0177)

                    print("All stats of John have been updated...")

                # ---------------------------------------- Gorn ----------------------------------------#

                # The user decided to update the stats of Gorn
                elif (userInput == "12"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Gorn? ")
                    determineOneByteStat(file, 0x018E)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Gorn? ")
                    determineOneByteStat(file, 0x018F)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Gorn? ")
                    determineOneByteStat(file, 0x0190)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Gorn? ")
                    determineTwoByteStat(file, 0x0192, 0x0193)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Gorn? ")
                    determineTwoByteStat(file, 0x0194, 0x0195)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Gorn? ")
                    determineTwoByteStat(file, 0x0196, 0x0197)

                    print("All stats of Gorn have been updated...")

                # ---------------------------------------- Maxwell ----------------------------------------#

                # The user decided to update the stats of Maxwell
                elif (userInput == "13"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Maxwell? ")
                    determineOneByteStat(file, 0x01AE)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Maxwell? ")
                    determineOneByteStat(file, 0x01AF)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Maxwell? ")
                    determineOneByteStat(file, 0x01B0)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Maxwell? ")
                    determineTwoByteStat(file, 0x01B2, 0x01B3)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Maxwell? ")
                    determineTwoByteStat(file, 0x01B4, 0x01B5)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Maxwell? ")
                    determineTwoByteStat(file, 0x01B6, 0x01B7)

                    print("All stats of Maxwell have been updated...")

                # ---------------------------------------- Toshi ----------------------------------------#

                # The user decided to update the stats of Toshi
                elif (userInput == "14"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Toshi? ")
                    determineOneByteStat(file, 0x01CE)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Toshi? ")
                    determineOneByteStat(file, 0x01CF)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Toshi? ")
                    determineOneByteStat(file, 0x01D0)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Toshi? ")
                    determineTwoByteStat(file, 0x01D2, 0x01D3)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Toshi? ")
                    determineTwoByteStat(file, 0x01D4, 0x01D5)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Toshi? ")
                    determineTwoByteStat(file, 0x01D6, 0x01D7)

                    print("All stats of Toshi have been updated...")

                # ---------------------------------------- Saduj ----------------------------------------#

                # The user decided to update the stats of Saduj
                elif (userInput == "15"):

                    # 8 bit / 1 - byte length stats
                    # STRENGTH
                    print("Do you wish to update the Strength stat of Saduj? ")
                    determineOneByteStat(file, 0x01EE)

                    # DEXTERITY
                    print("Do you wish to update the Dexterity stat of Saduj? ")
                    determineOneByteStat(file, 0x01EF)

                    # INTELLIGENCE
                    print("Do you wish to update Intelligence stat of Saduj? ")
                    determineOneByteStat(file, 0x01F0)

                    # 2 - byte length stats #
                    # HEALTH
                    print("Do you wish to update Health stat of Saduj? ")
                    determineTwoByteStat(file, 0x01F2, 0x01F3)

                    # MAX HP
                    print("Do you wish to update the Max HP stat of Saduj? ")
                    determineTwoByteStat(file, 0x01F4, 0x01F5)

                    # EXPERIENCE
                    print("Do you wish to update the Experience stat of Saduj? ")
                    determineTwoByteStat(file, 0x01F6, 0x01F7)

                    print("All stats of Saduj have been updated...")

                # ---------------------------------------- Gold ----------------------------------------#

                # The user decided to update the amount of gold the party has
                elif (userInput == "16"):

                    # GOLD => 16 bits / 2 bytes
                    gold = int(input("Enter the desired Gold value for your character (0-9999): "))
                    x = format(gold, "#04x")
                    hexGold = int(x, 16)
                    y = hexGold.to_bytes(2, 'little')
                    # Offset 0x00000204 & 0x00000205 => 516 & 517 in decimal
                    twoByteStatChanger(file, 516, 517, y[0], y[1])

                # The user has decided to quit and return to the main menu
                else:
                    print("All stats have been updated...\n")
                    print("Returning to the menu...\n")
                    break

        # ---------------------------------------- Selection 3 ----------------------------------------#

        # The user has chosen to max all possible stats for the MC and Party Members
        elif (userInput == "3"):

            # Main Character
            # Call statChanger() and twoByteStatChanger() to set the stats of the Main Character to max
            statChanger(file, 0x000E, max1Byte)
            statChanger(file, 0x000F, max1Byte)
            statChanger(file, 0x0010, max1Byte)
            twoByteStatChanger(file, 0x0012, 0x0013, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0014, 0x0015, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0016, 0x0017, firstMax2Byte9999, secondMax2Byte9999)

            # Repeat for the rest of the party members
            # Shamino
            statChanger(file, 0x002E, max1Byte)
            statChanger(file, 0x002F, max1Byte)
            statChanger(file, 0x0030, max1Byte)
            twoByteStatChanger(file, 0x0032, 0x0033, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0034, 0x0035, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0036, 0x0037, firstMax2Byte9999, secondMax2Byte9999)

            # Iolo
            statChanger(file, 0x004E, max1Byte)
            statChanger(file, 0x004F, max1Byte)
            statChanger(file, 0x0050, max1Byte)
            twoByteStatChanger(file, 0x0052, 0x0053, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0054, 0x0055, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0056, 0x0057, firstMax2Byte9999, secondMax2Byte9999)

            # Mariah
            statChanger(file, 0x006E, max1Byte)
            statChanger(file, 0x006F, max1Byte)
            statChanger(file, 0x0070, max1Byte)
            twoByteStatChanger(file, 0x0072, 0x0073, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0074, 0x0075, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0076, 0x0077, firstMax2Byte9999, secondMax2Byte9999)

            # Geoffrey
            statChanger(file, 0x008, max1Byte)
            statChanger(file, 0x008F, max1Byte)
            statChanger(file, 0x0090, max1Byte)
            twoByteStatChanger(file, 0x0092, 0x0093, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0094, 0x0095, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0096, 0x0097, firstMax2Byte9999, secondMax2Byte9999)

            # Jaana
            statChanger(file, 0x00AE, max1Byte)
            statChanger(file, 0x00AF, max1Byte)
            statChanger(file, 0x00B0, max1Byte)
            twoByteStatChanger(file, 0x00B2, 0x00B3, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x00B4, 0x00B5, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x00B6, 0x00B7, firstMax2Byte9999, secondMax2Byte9999)

            # Julia
            statChanger(file, 0x00CE, max1Byte)
            statChanger(file, 0x00CF, max1Byte)
            statChanger(file, 0x00D0, max1Byte)
            twoByteStatChanger(file, 0x00D2, 0x00D3, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x00D4, 0x00D5, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x00D6, 0x00D7, firstMax2Byte9999, secondMax2Byte9999)

            # Dupre
            statChanger(file, 0x00EE, max1Byte)
            statChanger(file, 0x00EF, max1Byte)
            statChanger(file, 0x00F0, max1Byte)
            twoByteStatChanger(file, 0x00F2, 0x00F3, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x00F4, 0x00F5, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x00F6, 0x00F7, firstMax2Byte9999, secondMax2Byte9999)

            # Katrina
            statChanger(file, 0x010E, max1Byte)
            statChanger(file, 0x010F, max1Byte)
            statChanger(file, 0x0110, max1Byte)
            twoByteStatChanger(file, 0x0112, 0x0113, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0114, 0x0115, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0116, 0x0117, firstMax2Byte9999, secondMax2Byte9999)

            # Sentri
            statChanger(file, 0x012E, max1Byte)
            statChanger(file, 0x012F, max1Byte)
            statChanger(file, 0x0130, max1Byte)
            twoByteStatChanger(file, 0x0132, 0x0133, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0134, 0x0135, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0136, 0x0137, firstMax2Byte9999, secondMax2Byte9999)

            # Gwenno
            statChanger(file, 0x014E, max1Byte)
            statChanger(file, 0x014F, max1Byte)
            statChanger(file, 0x0150, max1Byte)
            twoByteStatChanger(file, 0x0152, 0x0153, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0154, 0x0155, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0156, 0x0157, firstMax2Byte9999, secondMax2Byte9999)

            # John
            statChanger(file, 0x016E, max1Byte)
            statChanger(file, 0x016F, max1Byte)
            statChanger(file, 0x0170, max1Byte)
            twoByteStatChanger(file, 0x0172, 0x0173, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0174, 0x0175, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0176, 0x0177, firstMax2Byte9999, secondMax2Byte9999)

            # Gorn
            statChanger(file, 0x018E, max1Byte)
            statChanger(file, 0x018F, max1Byte)
            statChanger(file, 0x00190, max1Byte)
            twoByteStatChanger(file, 0x0192, 0x0193, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0194, 0x0195, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x0196, 0x0197, firstMax2Byte9999, secondMax2Byte9999)

            # Maxwell
            statChanger(file, 0x01AE, max1Byte)
            statChanger(file, 0x01AF, max1Byte)
            statChanger(file, 0x01B0, max1Byte)
            twoByteStatChanger(file, 0x01B2, 0x01B3, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x01B4, 0x01B5, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x01B6, 0x01B7, firstMax2Byte9999, secondMax2Byte9999)

            # Toshi
            statChanger(file, 0x01CE, max1Byte)
            statChanger(file, 0x01CF, max1Byte)
            statChanger(file, 0x01D0, max1Byte)
            twoByteStatChanger(file, 0x01D2, 0x01D3, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x01D4, 0x01D5, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x01D6, 0x01D7, firstMax2Byte9999, secondMax2Byte9999)

            # Saduj
            statChanger(file, 0x01EE, max1Byte)
            statChanger(file, 0x01EF, max1Byte)
            statChanger(file, 0x01F0, max1Byte)
            twoByteStatChanger(file, 0x01F2, 0x01F3, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x01F4, 0x01F5, firstMax2Byte999, secondMax2Byte999)
            twoByteStatChanger(file, 0x01F6, 0x01F7, firstMax2Byte9999, secondMax2Byte9999)

            # Gold
            twoByteStatChanger(file, 0x0204, 0x0205, firstMax2Byte9999, secondMax2Byte9999)

            print("All stats have been maxed out...")
            print("Returning to the main menu...")

        # ---------------------------------------- Selection 4 ----------------------------------------#

        # The user has chosen to receive 100 keys
        elif (userInput == "4"):

            # Set the amount of keys in the inventory to 100
            statChanger(file, 0x0206, chr(100))
            print("You have received 100 keys in your inventory...")
            print("Returning to the main menu...")

        # ---------------------------------------- Selection 5 ----------------------------------------#

        # The user has chosen to receive 100 skull keys
        elif (userInput == "5"):

            # Set the amount of skull keys in the inventory to 100
            statChanger(file, 0x020B, chr(100))
            print("You have received 100 skull keys in your inventory...")
            print("Returning to the main menu...")


        # ---------------------------------------- Selection 6 ----------------------------------------#

        # The user has chosen to receive 100 gems
        elif (userInput == "6"):

            # Set the amount of gems in the inventory to 100
            statChanger(file, 0x0207, chr(100))
            print("You have received 100 gems in your inventory...")
            print("Returning to the main menu...")


        # ---------------------------------------- Selection 7 ----------------------------------------#

        # The user has chosen to receive 1 black badge
        elif (userInput == "7"):

            # Set the amount of black badges in the inventory to 1
            statChanger(file, 0x0218, chr(1))
            print("You have received 1 black badge in your inventory...")
            print("Returning to the main menu...")

        # ---------------------------------------- Selection 8 ----------------------------------------#

        # The user has chosen to receive 2 magic carpets
        elif (userInput == "8"):

            # Set the amount of magic carpets in the inventory to 2
            statChanger(file, 0x020A, chr(2))
            print("You have received 2 magic carpets in your inventory...")
            print("Returning to the main menu...")


        # ---------------------------------------- Selection 9 ----------------------------------------#

        # The user has chosen to receive 10 magic axes
        elif (userInput == "9"):

            # Set the amount of magic axes in the inventory to 10
            statChanger(file, 0x0240, chr(10))
            print("You have received 10 magic axes in your inventory...")
            print("Returning to the main menu...")

        # ---------------------------------------- Selection 10 ----------------------------------------#

        # The user has chosen to change the amount of items they will receive in options 4 - 9
        elif (userInput == "10"):

            # KEYS
            # Call oneByteStatPartyMembers to determine if the user wants to update the amount of keys they receive
            print("Do you want to update the amount of keys in your inventory? ")
            determineOneByteStat(file, 0x0206)

            # Repeat for the rest of the items
            # SKULL KEYS
            print("Do you want to update the amount of skull keys in your inventory? ")
            determineOneByteStat(file, 0x020B)

            # GEMS
            print("Do you want to update the amount of gems in your inventory? ")
            determineOneByteStat(file, 0x0207)

            # BLACK BADGES
            print("Do you want to update the amount of black badges in your inventory? ")
            determineOneByteStat(file, 0x0218)

            # MAGIC CARPETS
            print("Do you want to update that amount of magic carpets in your inventory? ")
            determineOneByteStat(file, 0x020A)

            # MAGIC AXES
            print("Do you want to update the amount of magic axes in your inventory? ")
            determineOneByteStat(file, 0x0240)

            # Output a simple message to the user
            print("All items have been updated to be received in the desired amounts...")
            print("Returning to the main menu...")

        # ---------------------------------------- Quit Option ----------------------------------------#

        # Else, the user has chosen to quit the program
        else:

            # Output a message to the user
            print("FINISHED: The stats of all the characters and items have been updated to the desired value. ")

            # Close the file after all actions have been executed
            file.close()

            # Quit the program
            quit()


# Call the main function to start the program
main()


