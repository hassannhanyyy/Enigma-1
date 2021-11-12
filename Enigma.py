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

ed = eval(input("Would you like to Encrypt (1) or Decrypt (2)?  "))


if (ed == 1):
# Encrypted Message Class
 class Output1:
        def __init__(x, encrypt, message):
            x.encrypt = encrypt
            x.message = message

        def printed(output):
            print("The encrypted message " + output.encrypt)

 p1 = Output1("is: ", " ")
 p1.printed()

if (ed == 2):

# Decrypted Message Class
 class Output2:
        def __init__(x, decrypted, message):
            x.decrypted = decrypted
            x.message = message

        def printed(output):
            print("The decrypted message " + output.decrypted)

 p1 = Output2("is:  ", " ")
 p1.printed()


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

# Final Rotor #1
F1 = []
if(a == 1):
    F1 = R1

if(a == 2):
    F1 = R2

if(a == 3):
    F1 = R3

if(a == 4):
    F1 = R4

if(a == 5):
    F1 = R5

# Final Rotor #2
F2 = []
if(a == 1):
    F2 = R1

if(a == 2):
    F2 = R2

if(a == 3):
    F2 = R3

if(a == 4):
    F2 = R4

if(a == 5):
    F2 = R5

# Final Rotor #3
F3 = []
if(a == 1):
    F3 = R1

if(a == 2):
    F3 = R2

if(a == 3):
    F3 = R3

if(a == 4):
    F3 = R4

if(a == 5):
    F3 = R5

# Shifting the start setting for the rotor
def shiftstart(seq, n):
    return seq[n: ] + seq[:n]

# Shifting the rotors - rn for doube character literal sequence, n for a single character (integer), and trunc to output the truncated number without decimals
def shift(seq, n, rn, numb):
    if rn == 1:
        n = -n % len(seq)

    elif rn == 2:
        n = - math.trunc(n/25) % len(seq)
        
    elif rn == 3:
        n = - math.trunc(n/675) % len(seq)
       
    return seq[n:] + seq[:n]

# Going back through the rotor after reflection    
def rrev(seq):
    rrev = ['empty']*26
    for i in range(26):
        rrev[seq[i]] = i
    
    return rrev

# Going through the rotor
def rotor(seq, rev, numb, rn):
    number = []
    Rotorreverse = ['empty']*26
    if rev == 0:
        for i in range(len(numb)):
            rotation = shift(seq, i, rn, numb)
            number.append(rotation[numb[i]])
            
    elif rev == 1:
        for i in range(len(numb)):
            rotation = shift(seq, i, rn, numb)
            seqrev = rrev(rotation)
            number.append(seqrev[numb[i]])
        
    return number

# Going through the reflector or plugboard      
def RefPlug(list, numb3):
    ref = []
    for i in range(len(numb3)):
        ref.append(list[numb3[i]])
        
    return ref

# Enigma
Rotor1 = shiftstart(F1, x)
Rotor2 = shiftstart(F2, y)
Rotor3 = shiftstart(F3, z)

Seq = RefPlug(Plugboard, numb)
Seq1 = rotor(Rotor1, 0, Seq, 1)
Seq2 = rotor(Rotor2, 0, Seq1, 2)
Seq3 = rotor(Rotor3, 0, Seq2, 3) 
Seq4 = RefPlug(Reflector, Seq3)
Seq5 = rotor(Rotor3, 1, Seq4, 3)
Seq6 = rotor(Rotor2, 1, Seq5, 2)
Seq7 = rotor(Rotor1, 1, Seq6, 1)
Seq8 = RefPlug(Plugboard, Seq7)


# Message output - uppercase AND lowecase!!
uppercase = []
lowercase = []

for i in range(len(Seq8)):
    word = chr(Seq8[i]+97)
    word2 = chr(Seq8[i]+65)
    lowercase.append(word)
    uppercase.append(word2)


print("(In uppercase):   ",''.join(uppercase))
print("(and in lowercase):   ",''.join(lowercase))
