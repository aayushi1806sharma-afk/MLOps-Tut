# Single 
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# class child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# Child = child("Alice")
# Child.greet()
# Child.play()

# Multilevel 

# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells a stroy")

# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working.") 

# class child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# Child = child("Charlie")
# Child.tell_story()
# Child.work()
# Child.play()

# Hierarchical 

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying.")

# child1 = Child1("Daisy")
# child2 = Child2("Noisy")

# child1.greet()
# child1.play()

# child2.greet()
# child2.study()

# Multiple/ Diamond Problem

# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}")

# class B(A):
#     def greet(self):
#         print(f"Hello from B, {self.name}")
#         super().greet()

# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}")
#         super().greet()

# class D(B, C):
#     def greet(self):
#         print(f"Hello from D, {self.name}")
#         super().greet()

# d = D("Elliee")
# d.greet()

