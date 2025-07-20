while True:
    try: 
        number = float(input("Enter number: "))
        break
    except :
        print("Invalid number input.")

while True:
    try: 
        exponent = int(input("Enter exponent: "))
        break
    except :
        print("Invalid exponent input.")

if exponent==0:
    result =1
else :
    result = number
    for i in range (exponent-1):
        result = result * number

print("Result: ", result)

