# This will be a simple maths program

def add():
    try:
        int1 = int(input("First number: "))
        int2 = int(input("Second number: "))
    except Exception:
        print("You have not entered a number.")
    return int1 + int2

def subtract():
    try:
        int1 = int(input("First number: "))
        int2 = int(input("Second number: "))
    except Exception:
        print("You have not entered a number,")
    return int1 - int2

print(add())
