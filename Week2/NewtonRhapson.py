# A method given by Sir Issac Newton and Rhapson at the same time
# To fine the root of a polynomial with a single variable

# Lets take polynomial x**2 - 24 = 0 and fing it's square root using newton rhapson

y = 24.0
epsilon = 0.01
guess = y/2.0
numGuesses = 0
while abs(guess*guess - y)>=epsilon:
    numGuesses += 1
    guess = guess - (guess*guess - y)/(2*guess)

print("Number of Guesses : ", numGuesses)
print("Square root of ",y," is = ", guess)