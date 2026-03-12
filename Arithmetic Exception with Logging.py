import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    a = 10
    b = 5
    print(a / b)

except Exception as e:
    logging.error("Error occurred: " + str(e))
    print("Error logged in file")
