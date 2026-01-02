import random as r

#Greater Number Checker
def greater(a:float,b:float):
    if a - b == 0:
        return "a = b"
    elif a - b < 0:
        return " a < b "
    elif a == 0 or b == 0:
        return "None"
    else:
        return " a > b "

#Input From User For Guess Range
select_range = input("Select Range: ").split()

#Filtering Numbers Out of Statement
numbers = []
for integer in select_range:
    if integer.replace("-","").isdigit():
        numbers.append(int(integer))
    else:
        "Not a Number"
response_greater = greater(numbers[0], numbers[1])

#Guess Range Selection Conditions
if response_greater == "a = b":
    guess = r.randint(numbers[0], numbers[1])
elif response_greater == " a < b ":
    guess = r.randint(numbers[0], numbers[1])
elif response_greater == "None":
    print("No Range Selected")
else:
    guess = r.randint(numbers[1], numbers[0])

#User Guess
user = int(input(f"Guess a Number Between ({min(numbers)} and {max(numbers)}): "))

#Checking if Correct Guess
if user == guess:
    print("Correct Guess")
elif user > max(numbers) or user < min(numbers):
    print("Your Guess is Out Of Range")
else:
    print(f"Wrong Guess!\nCorrect Guess: {guess}")
