# Write a Python program to implement the addition, subtraction, and
# multiplication of complex numbers using classes. Use constructors to
# create objects. The input to the program consist of real and imaginary
# parts of the complex numbers.



class Complex:
    def __init__(self,real,imaginary) -> None:
        self.real = real
        self.imaginary = imaginary
    
    def addition(self,other):
        return Complex((self.real + other.real),(self.imaginary + other.imaginary)) 
    
    def subtraction(self,other):
        return Complex((self.real - other.real),(self.imaginary - other.imaginary)) 
    
    def multiplication(self,other):
        return Complex((self.real * other.real),(self.imaginary * other.imaginary)) 
    
    # def division(self,other):
    #     return Complex((self.real / other.real),(self.imaginary / other.imaginary)) 
    
    def display(self):
        print(f"{self.real} + {self.imaginary} i")
    

real1 = int(input("Enter the real part of complex number one: "))
imaginary1 = int(input("Enter the imaginary part of complex number one: "))


real2 = int(input("Enter the real part of complex number two: "))
imaginary2 = int(input("Enter the imaginary part of complex number two: "))

complex1 = Complex(real1,imaginary1)
complex2 = Complex(real2,imaginary2)

print("What operation you want to perform : \n1) Addition\n2) Subtraction\n3) Multiplication\n")
operation = int(input())

if(operation == 1):
    Complex.display(complex1.addition(complex2))
elif(operation == 2):
    Complex.display(complex1.subtraction(complex2))
elif(operation == 3):
    Complex.display(complex1.multiplication(complex2))
# elif(operation == 4):
#     Complex.display(complex1.division(complex2))
        
