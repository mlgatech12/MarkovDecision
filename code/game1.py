print("Guess a six-digit number SLAYER so that following equation is true, " +
"where each letter stands for the digit in the position shown:" + 
"\nSLAYER + SLAYER + SLAYER = LAYERS")
guess = int(input("Enter your guess for SLAYER: "))
S = (guess//100000)%10
L = (guess//10000)%10
A = (guess//1000)%10
Y = (guess//100)%10
E = (guess//10)%10
R = (guess//1)%10
'''
print(S)
print(L)
print(A)
print(Y)
print(E)
print(R)


print((L*100000) + (A*10000) + (Y*1000) + (E*100) + (R*10) + S)
'''
if 3*guess == (L*100000) + (A*10000) + (Y*1000) + (E*100) + (R*10) + S:
    print("Your guess is correct!!!")
elif len((str(guess))) != 6:
    print("THE NUMBER HAS TO HAVE 6 DIGITS >:(. READ THE INSTRUCTIONS. BULLYISM.")
else:
    print("Your guess is not correct, sorry")
print("Thanks for playing!")
    


print(str(guess)[2])
S = (str(guess)[0])
L = (str(guess)[1])
A = (str(guess)[2])
Y = (str(guess)[3])
E = (str(guess)[4])
R = (str(guess)[5])
if str(3*guess) == (L + A + Y + E + R + S):
    print("Your guess is correct!!!")
else:
    print("Your guess is not correct, sorry")