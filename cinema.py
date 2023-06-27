films={
            "Welcome":[5,7],
            "Housefull":[8,5],
            "Hate Story":[18,3],
            "Raone":[15,5]
}

while True:
    choice=input("Which movie would you like to watch?: ").strip().title()

    if choice in films:
        age=int(input("How old are you?: ").strip())
        if age>=films[choice][0]:
            if films[choice][1]>0:
                print("Enjoy the film!")
                films[choice][1]=films[choice][1]-1
            else:
                print("Sorry :( We are sold out!")
        else:
            print("You are too young to watch tht movie!")
    else:
        print("We do not have this film!")
