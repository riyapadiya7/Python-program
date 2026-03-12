with open("marks.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")

        roll = data[0]
        name = data[1]
        marks = list(map(int, data[2:]))

        total = sum(marks)
        percent = total / 4

        if percent >= 75:
            grade = "A"
        elif percent >= 60:
            grade = "B"
        else:
            grade = "C"

        print(roll, name, total, percent, grade)
