# Justin Calma
# CECS 378 - 9
# MW 8 AM - 10:15 AM
# Lab 2 - Malware

# Declare variable that will store the address of my save file
save = "C:\\DOSBox\\Ultima_5\\Ultima_5\\SAVED.GAM"


# Definition of the main function
def main():

    # Output messages to the user at the start of the program
    print("Ultima V: Save File Editor")
    print("Enter the address of the save file: ")

    # Open the binary save file for reading and writing
    file = open(save, "r+")

    # Prompt the user to input the desired strength stat for their characters
    # Get the input as a int value
    strength = int(input("Enter the desired Strength value for your characters (0-99): "))

    # Seek the offset of the Strength stat of the main character
    # Offset 0x0000000E => 14 in decimal
    file.seek(14, 0)

    # Convert the input of the user to the ASCII value so it can be written into the save file
    asciiStrength = chr(strength)

    # Overwrite the new Strength stat of the MC
    # write() takes in a string value, so convert the ascii value to a string before writing
    file.write(str(asciiStrength))

#########################################################################################################

    # Prompt the user to input the desired intelligence stat for their characters
    # Get the input as an int value
    intelligence = int(input("Enter the desired Intelligence value for your characters (0-99): "))

    # Seek the offset of the Intelligence stat of the main character
    # Offset 0x00000010 => 16
    file.seek(16, 0)

    # Convert the input of the user to the ASCII value so it can be written into the save file
    asciiIntelligence = chr(intelligence)

    # Overwrite the old intelligence stat of the MC with the new
    # write() takes in a string value, so convert the ascii value to a string before writing
    file.write(str(asciiIntelligence))

#########################################################################################################

    # Prompt the user to input the desired dexterity stat for their characters
    # Get the input as an int value
    dexterity = int(input("Enter the desired Dexterity value for your characters (0-99): "))

    # Seek the offset of the Dexterity stat of the main character
    # Offset 0x0000000F => 15
    file.seek(15, 0)

    # Convert the input of the user to the ASCII value so it can be written into the save file
    asciiDexterity = chr(dexterity)

    # Overwrite the the old Dexterity stat of the MC with the new
    # write() takes in a string value, so convert the ascii value to a string before writing
    file.write(str(asciiDexterity))

    # Output a message to the user
    print("FINISHED: The stats of all the characters have been updated to the desired value. ")

    # Close the file after all actions have been executed
    file.close()


# Call the main function to start the program
main()
