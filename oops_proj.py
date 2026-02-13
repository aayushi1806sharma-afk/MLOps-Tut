class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chatbook !! How Would you like to proceed ? 
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           ->""")
        if user_input == "1":
            self.signup() 
        elif user_input == "2":
            self.signin() 
        elif user_input == "3":
            self.my_post() 
        elif user_input == "4":
            self.sendmsg() 
        else: 
            exit()

    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input ("Set your password -> ")
        self.username = email
        self.password = pwd
        print("You have signedup successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/ username here -> ")
            pwd = input("Enter your password -> ")
            if self.username == uname and self.password == pwd:
                print("You have signin successfully")
                self.loggedin = True
            else:
                print("Please enter the correct credentials...")
        print("\n")
        self.menu() 

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your meassage here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter you message here -> ")
            frnd = input("Whom to send the message ?")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first...")
        print("\n")
        self.menu()        

# obj = chatbook()