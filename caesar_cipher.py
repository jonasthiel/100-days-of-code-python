from os import system

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

end = False

while not end:
	print(logo)

	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))

	def caesar(direction, text, shift):
		output_text = ""
		if shift > 26:
			shift %= 26
		if direction == "encode":
			for i in text:
				if i in alphabet:
					index = alphabet.index(i)
					if index + shift > 25:
						output_text += alphabet[index + shift - 26]
					else:
						output_text += alphabet[index + shift]
				else:
					output_text += i
		elif direction == "decode":
			for i in text:
				if i in alphabet:
					index = alphabet.index(i)
					if index - shift < 0:
						output_text += alphabet[index - shift + 26]
					else:
						output_text += alphabet[index - shift]
				else:
					output_text += i
		print(f"The {direction}d text is {output_text}")

	caesar(direction, text, shift)

	if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower() == "no":
		end = True
	else:
		system('clear')