from flask import Flask
app = Flask(__name__)

@app.route("/")

def add(a, b):  
    return a+b

def subtract(a, b):  
    return a-b

def multiply(a, b):  
    return a*b

def divide(a, b):  
    if b == 0:
        try :
            return a/b
        except ZeroDivisionError :
            print("Error: Division by zero.")
    

a = input()

if __name__ == '__main__':
    app.run()