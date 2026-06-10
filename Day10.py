def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations ={
    "+": add,
    "-":sub,
    "*":mul,
    "/":div
}
operation_symbol= input("Pick an Operation to to perform: +, -, *, /:  ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation_function=operations[operation_symbol]
result = operation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {result}")