# initiate a class 
class employee:
    # special method/ func/ magic/ dunder - constructor
    def __init__(self):
        # print(id(self))
        #print("Started executing attributes/ data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        #print("Attributes and data have been initiated")

    def travel(self):
        print("This travel method was called manually")
        print(f"Employee is now travelling to Delhi")    

# creating an obj or instance of a class
sam = employee()
#sam.name = "Samyy"
# print(id(sam))
#print(sam.name)
# shakt = employee()
# print(id(shakt))


# print(sam.salary)
# print(sam.id)
#calling a 
# sam.travel("Delhi")
# print(type(sam))
