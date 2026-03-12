class Age(Exception):
    pass

age = int(input("Enter age: "))

try:
    if age < 18:
        raise Age("You are not eligible")
    else:
        print("You are Eligible")

except Age as e:
    print(e)
