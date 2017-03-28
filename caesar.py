def alphabet_position(letter):
    if ord(letter) >= 65 and ord(letter) <= 90:
        char_num = ord(letter) - 65
    elif ord(letter) >= 97 and ord(letter) <= 122:
        char_num = ord(letter) - 97
    return char_num

def rotate_character(char, rot):
    encrypted_letter = ""
    if char.isupper():
        char_num = alphabet_position(char)
        rot_char = char_num + rot
        char_rot = chr((rot_char % 26) + 65)
        encrypted_letter += char_rot

    elif char.islower():
        char_num = alphabet_position(char)
        rot_char = char_num + rot
        char_rot = chr((rot_char % 26) + 97)
        encrypted_letter += char_rot
    return encrypted_letter

def encrypt(text, rot):
    encrypted_message = ""
    for i in text:
        if i.isalpha():
            encrypted_letter = rotate_character(i, rot)
            encrypted_message += encrypted_letter
        else:
            encrypted_message += i
    return encrypted_message
