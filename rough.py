lst = [1, 2, 3]
str = "mlops playlist"
int = 999

# print(type(lst))
# print(type(str))
# print(type(int))

# lst.clear()
# print(lst)

# str = str.capitalize()
# print(str)

# a = "x"
# b = "y"
# print(a + b)

from oops_proj import chatbook 

user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)


#getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

# print(user1._chatbook__name)

# lst = [1, 2, 3]
# # functions
# a = len(lst)
# print(a)

# method 
# user1 = chatbook()
# user1.sendmsg()

