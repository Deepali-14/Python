email=input("What is your email id?: ").strip("")
user=email[:email.index("@")]
domain=email[email.index("@")+1:]
answer="Your username is {} and your domain is {}".format(user,domain)
print(answer)
