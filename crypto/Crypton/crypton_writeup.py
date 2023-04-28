message = "YetiCTF{unusu4lly_c1ph3r_w1th_b1ts}"
key = 89

def encrypt_message(message, key):
    encrypted_message = ''
    for i in range(len(message)):
        char_code = ord(message[i])
        if i % 2 == 0:
            half_byte = (char_code >> 4) + key
            encrypted_char = chr((half_byte << 4) + (char_code & 0x0F))
        else:
            half_byte = (char_code & 0x0F) + key
            encrypted_char = chr((char_code & 0xF0) + half_byte)
        encrypted_message += encrypted_char
    return encrypted_message

def write_to_file(filename, encrypted_message):
    with open('message.txt', 'w') as f:
        f.write(encrypted_message.encode('utf-8').hex())  
    f.close()

def read_from_file(filename):
    with open('message.txt', 'r') as f:
        hex_string = f.readline()
        encrypted_message = bytes.fromhex(hex_string).decode('utf-8')  
    f.close()
    return encrypted_message

def decrypt_message(message):
    for key in range(1001):
        decrypted_message = ""
        for i in range(len(encrypted_message)):
            char_code = ord(encrypted_message[i])
            if i % 2 == 0:
                half_byte = (char_code >> 4) - key
                decrypted_char = chr((half_byte << 4) + (char_code & 0x0F))
            else:
                half_byte = (char_code & 0x0F) - key
                decrypted_char = chr((char_code & 0xF0) + half_byte)
            decrypted_message += decrypted_char
        print(f"Key: {key}, Decrypted message: {decrypted_message}")
        
if __name__ == '__main__':
    encrypted_message = encrypt_message(message, key)
    write_to_file('message.txt', encrypted_message)
    
    encrypted_message = read_from_file('message.txt')
    decrypt_message(encrypted_message)
    