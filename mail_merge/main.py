names_list = []
with open("Input/Names/invited_names.txt") as file:
    names = file
    for name in names:
        names_list.append(name.replace("\n", ""))

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names_list:
        file_name = "Output/ReadyToSend/" + "letter_for_" + name + ".txt"
        with open(file_name, 'w') as file:
            file.write(letter.replace("[name]", name))