# Create the list of known users
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My Name is Travis")
    #use the strip funtion to remove the space after the text and capitalize
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n): ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print ("No problem, I didn't want you to leave anyway!")
            
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_user = input("Would you like to be added to the system {}? (y/n): ").strip().lower()
        
        if add_user == "y":
            known_users.append(name)
        elif remove == "n":
            print ("No problem, I didn't want to add you anyway!")

    