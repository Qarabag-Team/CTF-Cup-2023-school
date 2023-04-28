def write_to_file(filename, encrypted_message):
    with open(filename, 'w') as f:
        f.write(encrypted_message.encode('utf-8').hex())  
    f.close()

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
    

if __name__ == '__main__':
    print('_________                        __                  '
          '\n\_   ___ \_______ ___.__._______/  |_  ____   ____   '
          '\n/    \  \/\_  __ <   |  |\____ \   __\/  _ \ /    \  '
          '\n\     \____|  | \/\___  ||  |_> >  | (  <_> )   |  \ '
          '\n \______  /|__|   / ____||   __/|__|  \____/|___|  / '
          '\n        \/        \/     |__|                    \/  ')
    
    message = str(input('\n\nEnter message >> '))
    key = int(input('Enter key >> '))
    
    print('Your message will be encrypted and written to a file \'message.txt\' in hex')
    
    encrypted_message = encrypt_message(message, key)
    write_to_file('message.txt', encrypted_message)