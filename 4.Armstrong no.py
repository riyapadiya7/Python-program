#Write a program to enter 10 numbers and display all armstrog number from those numbers.

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    return total == num


numbers = []
print("Enter 10 numbers:")

for i in range(10):
    n = int(input(f" {i+1}: "))
    numbers.append(n)

print("\nArmstrong number is:")
for n in numbers:
    if is_armstrong(n):
        print(n)
