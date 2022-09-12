user1= input("Enter username:")
pass1= input("Enter password:")
counter=1
while counter < 3:
    if user1 == 'python' and pass1 == 'rules':
        print("welcom")
        break
    else:
         user1 = input("Enter user name :")
         pass1 = input("Enter password:")
         counter = counter + 1
print("access denied")
