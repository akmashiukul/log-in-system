print("Welcome to the lgo in system.")
def login():
    try:
        login_file=open('login_file.txt','r')
        a=login_file.read()
        b=a.split(" ")
        email=input("Email or Phone number:")
        password=input("Password:")
        if email in b and password in b:
            print("Log in sucessfull.")
        else:
            print("Invalid id or pass try again.")
    except:
        print("Please register first.")
def register():
    email=input("Email:")
    password=input("Password:")
    register_file=open("Login_file.txt",'w')
    register_file.write(email+' '+password)
    print("register sucessfull")
d=input("Log in or register:")
if d=='log in':
    login()
if d=='register':
    register()
