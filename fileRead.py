f2=open("creds.txt","r")
contents=""
if f2.mode=="r":
    contents=[x for x in f2.read().split('\n')]
print(contents)
u=input("enter the username: ")
p=input("enter the password: ")
if(u in contents[0] and p in contents[1]):
    print("Correct Username and password")
else:
    print("Incorrect Username and password")
    
