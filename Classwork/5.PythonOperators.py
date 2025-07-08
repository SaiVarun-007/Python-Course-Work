#1.Arithmetic Operators

a=10
b=20
print("Addition(+) :", a+b)
print("Subtraction(-) :", a-b)
print("Multiplication(*) :", a*b)
print("Division(/) :", a/b)
print("Floor Division(//) :", a//b)
print("Modulus(%) :", a%b)
print("Exponentiation(**) :", a**b)

#Comparison Operators

a=20
b=10
print("Equal To(==) :", a==b)
print("Not Equal To(!=) :", a!=b)
print("Greater Than(>) :", a>b)
print("Less Tahn(<) :", a<b)
print("Greater Than or Equal to(>=) :", a>=b)
print("Less Than or Equal To(<=) :", a<=b)


#Assignment operators 
a=20
print("Assign (=):",a ) #Assign (=): 20
a+=2
print("Add & Assign (+=):",a ) #Add & Assign (+=): 22
a-=2
print("Subtract & Assign (-=):", a) #Subtract & Assign (-=): 20
a*=2
print("Multiply & Assign (=):",a ) #Multiply & Assign (=): 40
a/=2
print("Divide & Assign (/=):", a) #Divide & Assign (/=): 20.0
a//=2
print("Floor Divide & Assign (//=):", a) #Floor Divide & Assign (//=): 10.0
a%=2
print("Modulus & Assign (%=):", a) #Modulus & Assign (%=): 0.0
a**=2
print("Exponentiate & Assign (=):", a) #Exponentiate & Assign (=): 0.0

#logical operators
a=10
b=20
print("AND:",a%2==0 and b%3==0) #AND: False
print("OR:",a%2==0 or b%3==0) #OR: True
print("not:",not b%5==0) #not: False

#Membership Operators
a = 'rasool'
print('a' in a) # in True
print('a' not in a) #false

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # Output: True
print("grape" not in fruits) # Output: True

#Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # Output: True (Both refer to the same object)
print(a is c) # Output: False (Different objects with the same content)
print(a is not c) # Output: True

#Bitwise operators
a = 5 # Binary: 0101
b = 3 # Binary: 0011
print(a & b) # Output: 1 (Binary: 0001 → AND operation)
print(a | b) # Output: 7 (Binary: 0111 → OR operation)
print(a ^ b) # Output: 6 (Binary: 0110 → XOR operation)
print(~a) # Output: -6 (Binary: Inverts bits of 5)
print(a << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(a >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)