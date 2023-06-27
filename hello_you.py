name=input("What is your name?: ")
age=input("How old are you?: ")
city=input("Which city do you live in?: ")
hobby=input("What do you love doing?: ")
string="Your name is {} and you are {} years old. You live in {} and you love {}."
print(string.format(name,age,city,hobby))
