import cmath
a =int(input("Enter the 'a' value of the Equation:"))
b =int(input("Enter the 'b' value of the Equation:"))
c =int(input ("Enter the 'c' value of the Equation:"))
#Solving the Discriminant
d = (b**2)-(4*a*c)
# Finding the two solutions
sola = (-b-cmath.sqrt(d))/2*a
solb = (-b+cmath.sqrt(d))/2*a
print(sola)
print(solb)


    
    
    
