#import operator
import Operators as opr
#from operators import *
#from operators import add, sub, div, mul

a=int(input("Enter a: "))
b=int(input("Enter b: "))

op=input("Enter the op(+-/*%**): ")

if op=='+':
    opr.add(a,b)
elif op=='-':
    opr.sub(a,b)
elif op=='*':
    opr.mul(a,b)
elif op=='/':
    opr.div(a,b)
elif op=='%':
    opr.mod(a,b)
elif op=='**':
    opr.exp(a,b)
