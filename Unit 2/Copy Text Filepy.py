with open("source.txt", "r") as s:
    data = s.read()

with open("test.txt", "w") as d:
    d.write(data)

print("File copied successfully")
