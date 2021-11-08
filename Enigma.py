# CW1 - Enigma

import math

message = input("Enter the message: ")
message = message.upper()

a = eval(input("Which rotor would you like to use as your first rotor (Between 1&5)?  "))
print("First Rotor: ",a)

b = eval(input("Which rotor would you like to use as your second rotor (Between 1&5)?  "))
print("Second Rotor: ",b)

c = eval(input("Which rotor would you like to use as your third rotor (Between 1&5)?  "))
print("Third Rotor: ",c)

x = eval(input("Input the first rotor start setting (0-25)?  "))
print("Rotor setting: ",x)

y = eval(input("Input the first rotor start setting (0-25)?  "))
print("Rotor setting: ",y)

z = eval(input("Input the first rotor start setting (0-25)?  "))
print("Rotor setting: ",z)

numb = []

for sign in message:
    number = ord(sign) - 65
    numb.append(number)


# Rotors
R1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
R2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
R3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
R4 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
R5 = [9, 15, 6, 21, 14, 20, 12, 5, 24, 16, 1, 4, 13, 7, 25, 17, 3, 10, 0, 18, 23, 11, 8, 2, 19, 22]

# Rotor Settings
Reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
Plugboard = [0, 24, 2, 3, 4, 5, 22, 7, 8, 9, 10, 12, 11, 16, 14, 15, 13, 17, 18, 19, 20, 21, 6, 23, 1, 25]
R1start = x
R2start = y
R3start = z
