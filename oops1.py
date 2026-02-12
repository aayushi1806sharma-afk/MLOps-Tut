# initiate a class 
class employee:
    # special method/ func/ magic/ dunder - constructor
    def __init__(self):
        print("Started executing attributes/ data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes and data have been initiated")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")    

# creating an obj or instance of a class
sam = employee()


# print(sam.salary)
# print(sam.id)
#calling a method
sam.travel("Gurgaon")
# sam.travel("Delhi")
print(type(sam))
