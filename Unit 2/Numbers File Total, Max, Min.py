with open("numbers.txt", "r") as f:
    nums = list(map(int, f.read().split()))

print("Total:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))
