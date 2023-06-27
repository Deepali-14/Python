known_users=['Anubhav Singh', 'Deepali Singh', 'Sudhiksha Singh', 'Reena Singh', 'Sita Sharan Singh']
while True:
    print("Hi! My name is Travis")
    name=input("What is your name?: ").strip().title()
    if name in known_users:
        print("Hello {}!".format(name))
        print("Would you like to be removed from the system {}?".format(name))
        remove=input("Enter yes or no(y/n): ").lower()
        print(known_users)
        if remove=='y':
            print("Good Bye :)")
            known_users.remove(name)
            print(known_users)
        else:
            print("No worries :) I too don't want you to leave.")
    else:
        print("I have not met you yet! {}.".format(name))
        print("Would you like to be added to the system {}?".format(name))
        add=input("Enter yes or no(y/n): ").lower()
        print(known_users)
        if add=='y':
            print("Hello {}!".format(name))
            known_users.append(name)
            print(known_users)
        else:
            print("No worries :) See you around.")
    
