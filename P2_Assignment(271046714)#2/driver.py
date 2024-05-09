import os
from P2_Assignment_no2 import admin_user,admin_password,Administratoin,User
#                            ---------DRIVER CODE----------
#an outer loop flag so that program never stops
outer_most_loop = 1
while outer_most_loop == 1:
    print("----------------CINEMA BOOKING SYSTEM----------------")
    #the user will comeback here every time he/she logsout
    login = input("Welcome!\nPlease press 1 if you are a costumer\npress 2 if you want to signup as costumer\npress 3 if you are from administration: ")
    if login == "3":
        #Admin interface
        middle_loop = 1 #loop flag to let user stay in admin section as long as he want
        while middle_loop == 1:
            name = input("Enter you username: ")
            password = input("Enter your password: ")
            #checks if admin's username and password are correct
            if name == admin_user and password == admin_password:
                print(f"Welcome back {admin_user} You have Successfully logged in!")
                admin = Administratoin(name,password)
                #loop to let admin access all features for as long as he want
                while True:
                    print("Options:\n1)Display movies\n2)Add_movie\n3)Remove movie\n4)Display Available time\n5)Add time slot\n6)Remove time slot\n7)Display Available screens\n8)Add Screen\n9)Remove screen\n10)Check Booking records\n11)Slot Assignment\n12)Slot updation\n13)Log out")
                    option = int(input("Enter the action number you wanna perform: "))
                    if option == 1:
                        admin.display_movies()
                        continue
                    elif option == 2:
                        print("Type back (at any point) to go back: ")
                        title = input("Enter the movie name you wanna add: ")
                        if title != "back":
                            admin.add_movie(title)
                        else:
                            continue
                    elif option == 3:
                        print("Type back (at any point) to go back: ")
                        title = input("Enter the movie name: ")
                        if title != "back":
                            admin.remove_movie(title)
                        else:
                            continue
                    elif option ==4:
                        admin.available_time()
                        continue
                    elif option ==5:
                        print("Type back (at any point) to go back: ")
                        time = input("Enter the time(i.e 00-00-00-00): ")
                        if time != "back":
                            admin.add_time_slot(time)
                        else:
                            continue
                    elif option == 6:
                        print("Type back (at any point) to go back: ")
                        time = input("Enter the time(i.e 00-00-00-00): ")
                        if time != "back":
                            admin.remove_time_slot(time)
                        else:
                            continue
                    elif option == 7:
                        admin.available_screens()
                        continue
                    elif option == 8:
                        print("Type back (at any point) to go back: ")
                        screen = input("Enter the screen name: ")
                        if screen != "back":
                            admin.add_screen(screen)
                        else:
                            continue
                    elif option ==9:
                        print("Type back (at any point) to go back: ")
                        screen = input("Enter the screen name: ")
                        if screen != "back":
                            admin.remove_screen(screen)
                        else:
                            continue
                    elif option == 10:
                        admin.booking_records()
                        continue
                    elif option == 11:
                        with open("shows.txt","r") as file:
                            shows = file.read()
                            print(shows)
                        print("Type back (at any point) to go back: ")
                        screen = input("Enter the screen name: ")
                        if screen!="back":
                            title = input("Enter movie name: ")
                            if screen!="back":
                                time = input("Enter the time(i.e 00-00-00-00): ")
                                if time!="back":
                                    seats = input("Enter the list of seats: ")
                                    if seats!="back":
                                        admin.slot_assignment(screen,title,time,seats)
                        else:
                            continue
                    elif option == 12:
                        print("Type back (at any point) to go back: ")
                        with open("shows.txt","r") as file:
                            shows = file.read()
                            print(shows)
                        screen = input("Enter the screen name: ")
                        if screen != "back":
                            time = input("Enter the time(i.e 00-00-00-00): ")
                            if time != "back":
                                movie = input("Enter the movie name(Exact title): ")
                                if movie != "back":
                                    action = input("Enter the following accroding to the action you wanna perform\n'u'to update\n'd' to delete: ")
                                    if action != "back":
                                        with open("shows.txt","r") as file:
                                            content = file.read()
                                            if f"{screen},{time}:{movie}" in content:            
                                                    admin.slot_updataion(screen,time,action,movie)                            
                                            else:
                                                print("Record not found")
                        else:
                            continue
                    elif option == 13:
                        print("Successfully logedout!")
                        middle_loop = 0
                        #if admin wants to logout
                        break
                    else:
                        print("Wrong input!")
                        continue
            else:
                print("Wrong login details!!!\nPlease try again.")
                continue
    elif login == "1":
        #user interface
        middle_loop = 1 #loop flag to let user stay in user's section as long as he want
        while middle_loop == 1:
            name = input("Enter you username: ")
            password = input("Enter your password: ")
            with open("user_accounts.txt","r") as file:
                credentials = file.read()
            #checks if username and password are correct by going through file where all login details are stored
            if f"{name},{password}" in credentials:
                print(f"Welcome back {name} You have Successfully logged in!")
                user = User(name,password)
                #loop to let user access all features for as long as he want
                while True:
                    print("Options:\n1)Ticket Booking\n2)Booking history\n3)Ticket Cancellation\n4)logout")
                    option = int(input("Enter the action number you wanna perform: "))
                    if option == 1:
                        with open("shows.txt","r") as file:
                            shows = file.read()
                            print(shows)
                        while True:
                            time = input("Enter the time (format = 00-00-00-00): ")
                            if time != "back":
                                screen = input("Enter the screen : ")
                                if screen != "back":
                                    movie = input("Enter (exact) movie name: ")
                                    if movie != "back":
                                        if os.path.exists(f"{screen}({time}).txt"):
                                            user.bookings(time,screen,name,movie)
                                            break
                                        else:
                                            print("Something went wrong\nCheck your inputs again")
                                            continue
                            else:
                                break
                        continue
                    elif option == 2:
                        #check if record exists
                        if os.path.exists(f"{name}.txt"):
                                user.personal_record(name)
                                continue
                        else:
                            print("No Bookings yet")
                            continue
                    elif option == 3:
                        screen = input("Enter the screen name: ")
                        if screen != "back":
                            time = input("Enter the time(i.e 00-00-00-00): ")
                            if time != "back":
                                movie = input("Enter the movie name(Exact title): ")
                                if movie != "back":
                                    seats =  input("Enter seat: ")
                                    if seats != "back":
                                        with open("bookings.txt","r") as file:
                                            content = file.read()
                                            #Checks if record exits
                                            if f"Name: {name} , Seat: {seats} , Screen: {screen}, Time: {time}" in content:
                                                user.delete_booking(name,screen,time,seats)
                                                user.personal_record_updation(name,screen,time,seats,movie)
                                                print("Updated!")
                                                continue
                                            else:
                                                print("wrong input!")
                                                continue
                                        
                        else:
                            continue
                    elif option == 4:
                        print("Successfully logedout!")
                        #if admin wants to logout
                        middle_loop = 0
                        break
                    else:
                        print("Wrong input!")
                        continue
            else:
                print("Wrong login details!!!\nPlease try again.")
                continue
    elif login == "2":
        #Signup user interface
        while True:
            name = input("Please enter a unique username: ")
            with open("user_accounts.txt","r") as file:
                user_name_check = file.read()
                #checks if username is unique by going through file where all login details are stored
                if name in user_name_check:
                    print("Sorry!This username is currently not available\nTry something else:")
                    continue
                else: 
                    password = input("Please set your password: ")
                    with open("user_accounts.txt","a") as file:
                        file.write(f",{name},{password}")
                    print("Thank you so much!\nYou can now login to your account")
                    #will take the user to home page
                    break