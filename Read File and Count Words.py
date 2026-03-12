with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

words = data.split()
print("Total words:", len(words))
