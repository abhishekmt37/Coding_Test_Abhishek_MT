class Calculator:
    def __init__(self,a,b,oper):
        self.a = a
        self.b = b
        self.oper = oper
    
    def calculate(self):
        if self.oper == 'add':
            return self.a + self.b
        if self.oper == 'sub':
            return self.a - self.b
        if self.oper == 'mul':
            return self.a * self.b
        if self.oper == 'div':
            return self.a / self.b
        return "Invalid Operation"
    
a = float(input("Enter a first number"))
b = float(input("Enter a second number"))
oper = input("Enter a Operation your perferm (add,sub,mul,div)")

c = Calculator(a,b,oper)
print(c.calculate())
