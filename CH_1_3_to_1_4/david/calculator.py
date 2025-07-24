
def add(a, b):  
    return a+b

def subtract(a, b):  
    return a-b

def multiply(a, b):  
    return a*b

def divide(a, b):  
    try :
        return a/b
    except ZeroDivisionError :
        return "Error: Division by zero."  # print("Error: Division by zero.")??

if __name__ == "__main__":
    a = int(input("1번째 숫자를 입력하세요: "))
    b = int(input("2번째 숫자를 입력하세요: "))
    cal = input("연산자를 입력하세요: ")

    if cal == "+":
        result = add(a,b)
        print("Result: ", result)

    elif cal == "-":
        result = subtract(a,b)
        print("Result: ", result)

    elif cal == "*":
        result =  multiply(a,b)
        print("Result: ", result)

    elif cal == "/":
        result = divide(a,b)
        print("Result: ", result)

    else :
        print("Invalid operator.")
