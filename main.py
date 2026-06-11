import db_add as db
import tkinter 
db.cratedb()
while_1 = True
while_2 = False
input_nobat = 0
input_username = ""
while(while_1):
    print("1.Login\n2.Create an account")
    input_user_login = input("enter a 1.2: ")
    if(input_user_login == "1"):
        print("--------------Login--------------")
        input_nobat = int(input("enter a input_nobat: "))
        input_username = input("enter a username: ")
        input_password = input("enter a password: ")
        db.login_user(name=input_username,password=input_password,nobat=input_nobat)
        if(db.wellcom == True):
            while_2 = True
            break
        
              
    elif(input_user_login == "2"):
        print("--------------Create an account--------------")
        input_username = input("enter a username: ")
        input_phone = input("enter a phone: ")
        input_password = input("enter a password: ")
        input_gmail = input("enter a gmail: ")
        input_url_panel = input("enter a url_panel: ")
        input_id_telegram = input("enter a id_telegram: ")
        input_config_name= input("enter a config_name: ")
        input_config_password= input("enter a config_password: ")
        db.add_user(name=input_username,phone=input_phone,password=input_password,gmail=input_gmail,url_panel=input_url_panel,id_telegram=input_id_telegram,config_name=input_config_name,config_password=input_config_password,)
        
        
while(while_2):
    input_admin_meno = ""
    db.meno(nobat=input_nobat,name=input_username)
    if(input_nobat == 1):
        input_admin_meno = input("enter a 1-4: ")
    else:
        input_user_meno = input("enter a 1-4: ")
        
    if(input_admin_meno == "1"):
        print("-------------- view users --------------")
        db.view_users()
    if(input_admin_meno == "2"):
        print("-------------- add user --------------")
        input_username = input("enter a username: ")
        input_phone = input("enter a phone: ")
        input_password = input("enter a password: ")
        input_gmail = input("enter a gmail: ")
        input_url_panel = input("enter a url_panel: ")
        input_id_telegram = input("enter a id_telegram: ")
        input_config_name= input("enter a config_name: ")
        input_config_password= input("enter a config_password: ")
        db.add_user(name=input_username,phone=input_phone,password=input_password,gmail=input_gmail,url_panel=input_url_panel,id_telegram=input_id_telegram,config_name=input_config_name,config_password=input_config_password,)
        
    


