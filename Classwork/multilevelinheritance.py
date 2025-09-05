#Multiple Inheritance
#more parents and single child
#A class inherits from more than one parent class.
class A:
   def display_a(self):
      print("parent class A")

class B:
   def display_b(self):
      print('parent class B ')

class C:
   def display_c(self):
      print('parent class C ')

class D(A,B,C):
   def display_d(self):
      print('Child class A,B,C->D ')

d=D()

d.display_a()
d.display_b()
d.display_c()
d.display_d()