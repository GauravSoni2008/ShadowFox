import random

num_of_1 = 0 #number of times you rolled a 1
num_of_6 = 0 #number of times you rolled a 6
num_of_two_6 = 0 #number of times you rolled two six in a row
prev = 0
for i in range(20):
    die = random.randint(1, 6)
    print(f"Roll {i+1}: {die}")

    if die == 1:
        num_of_1 += 1
    
    elif die == 6:
        num_of_6 += 1
        if prev == 6:
            num_of_two_6 += 1

    prev = die

print(f"Number of times you rolled a 6: {num_of_6}")
print(f"Number of times you rolled a 1: {num_of_1}")
print(f"Number of times you rolled two 6s in a row: {num_of_two_6}")