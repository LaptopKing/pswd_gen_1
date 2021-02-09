import random

chars = ['-', '_', ' ']
passwords = []
password = ""

for num in range(10):
    chars.append(num)

for num2 in range(65, 91):
    chars.append(chr(num2))

for num3 in range(97, 122):
    chars.append(chr(num3))

# This defines the number of the passwords will be generated
num_of_passwords = 1000

for i in range(num_of_passwords):
    length_of_password = random.randint(8, 12)
    password = ""
    for k in range(length_of_password):
        chars_length = len(chars)
        random_index = random.randint(0, (chars_length - 1))
        password += str(chars[random_index])
    passwords.append(password)

# Change this to save it to a different file with different file name
password_file_name = "passwords"

writer = open(password_file_name, "w")
writer.write("")
writer.flush()
writer.close()
writer = open(password_file_name, "a+")

for psw in passwords:
    print (psw)
    
    # Uncomment the below line if you want to save the generated passwords ( these passwords are totally random so probably \
    # there is a very little chance if somebody uses one of it )
    
    writer.write(psw + "\n")