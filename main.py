choice = input("""Enter your choice :
                  1. Turn on security system 
                  2. Add new user to the system
                  3. Train Data
                  4. Remove an exixting user""")
#1                  
def face_recognition():
    print("Running Face Recognision sysytem ")
    import face_recognise
#2
def add_User():
    import add_pics
#3  
def face_training():
    import face_train
#4   
def remove_User():
    import remove_account
#5   
def unknown_action():
    print("Choice doesn't exist")
'''    
if choice == 1:
    face_recognition()
elif choice == 2:
    add_User()
elif choice == 3:
    face_training()
elif choice == 4:
    remove_User()  
else:
    unknown_action()
'''  
    
my_switch = {"1" : face_recognition,"2" : add_User,"3" : face_training,"4" : remove_User}

my_switch.get(choice, unknown_action)()

    
    