import os #imported os to check if a text file exists or not
#Used variables to store admin info
admin_user = "abdul"
admin_password = "111"
#A movie class that has mathod to display ,add and remove movies
class Movie:
    def __init__(self):
        pass
    def add_movie(self,title):
        self.title = title
        with open("movies.txt","a") as file:
            file.write(f",{self.title}")
    def remove_movie(self,title):
        self.title = title
        with open("movies.txt","r") as file:
            content = file.read()
        modified_content = content.replace(self.title,"")
        with open("movies.txt","w") as file:
            file.write(modified_content)
    def display_movies(self):
        with open("movies.txt","r") as file:
            movie = file.read()
            print(movie)
#Time slots class deals with all stuff related to time slots
class TimeSlots:
    def __init__(self):
        pass
    #it will display the available time slots
    def available_time(self):
        with open("slots.txt","r") as file:
            slots = file.read()
            print(slots)
    #remove time slot
    def remove_time_slot(self,time):
        self.time = time
        with open("slots.txt","r") as file:
            content = file.read()
        modified_content = content.replace(self.time,"")
        with open("slots.txt","w") as file:
            file.write(modified_content)
    #add time slots
    def add_time_slot(self,time):
        self.time = time
        with open("slots.txt","a") as file:
            file.write(f",({self.time})")
    #It will assign the time slots
    def slot_assignment(self,screen,title,time,seats):
        self.screen = screen
        self.title = title
        self.time = time
        self.seats = seats
        #it checks if a slot is booked 
        with open("shows.txt","r") as file:
            content = file.read()
            if f"{self.screen},{self.time}:{self.title}" not in content:
                with open("shows.txt","a") as file:
                    file.write(f"\n{self.screen},{self.time}:{self.title}") #show booked
                with open(f"{self.screen}({self.time}).txt","w") as file:
                    file.write(str(self.seats)) #will add seats for that show
                #check if a time-slot exist if not it will add that time-slot in slots file
                with open("slots.txt","r") as file:
                    for i in file:
                        if self.time in i: 
                            break
                        else:
                            with open("slots.txt","a") as file:
                                file.write(f",({self.time})")
                #Check if the screen exist if not it will add that screen in screens file
                with open("screens.txt","r") as file:
                    for i in file:
                        if self.screen in i:
                            break
                        else:
                            with open("screens.txt","a") as file:
                                file.write(f",{self.screen}")
                #checks if movie exists if not it will add that movie in screen file
                with open("movies.txt","r") as file:
                    for i in file:
                        if self.title in i:
                            break
                        else:
                            with open("movies.txt","a") as file:
                                file.write(f",{self.title}")
            else:
                print("Slot already booked!")
    #it will update a slot
    def slot_updataion(self,screen,time,action,movie):
        self.screen = screen
        self.action = action
        self.time = time
        self.movie = movie
        #if the admin want to delete a time slot
        if self.action == "d":
            with open("shows.txt", "r") as file:
                content = file.read()
            updated = content.replace(f"{self.screen},{self.time}:{self.movie}","")
            with open("shows.txt", "w") as file:
                file.write(updated)
                print("Updated")
            seats_file = f"{self.screen}({self.time}).txt"
            os.remove(seats_file)
        #If the admin wants to play someother movie on a time slot
        elif self.action == "u":
            new_movie = input("Enter the title of the new movie: ")
            with open("shows.txt", "r") as file:
                content = file.read()
            updated = content.replace(f"{self.screen},{self.time}:{self.movie}", f"{self.screen},{self.time}:{new_movie}")
            with open("shows.txt", "w") as file:
                file.write(updated)
                print("Updated")
        else:
            print("Wrong inputs")            
#Screen class has methods that display,add and rmeove screens
class Screen:
    def __init__(self):
        pass
    def available_screens(self):
        with open("screens.txt","r") as file:
            screen = file.read()
            print(screen)
    def remove_screen(self,name):
        self.name = name
        with open("screens.txt","r") as file:
            content = file.read()
        modified_content = content.replace(self.name,"")
        with open("screens.txt","w") as file:
            file.write(modified_content)
    #add time slots
    def add_screen(self,name):
        self.name = name
        with open("screens.txt","a") as file:
            file.write(f",({self.name})")
class Booking:
    def __init__(self):
        pass
    #This method upadate booking record in bookings.txt like a a particular seat of a particular seat is booked by a user
    def booking_details_updation(self,user,screen,time,seats):
        with open("bookings.txt","a") as file:
            file.write(f"\nName: {user} , Seat: {seats} , Screen: {screen}, Time: {time}")
    def delete_booking(self,user,screen,time,seats):
        with open("bookings.txt","r") as file:
            content = file.read()
        modified_content = content.replace(f"\nName: {user} , Seat: {seats} , Screen: {screen}, Time: {time}","")
        with open("bookings.txt","w") as file:
            file.write(modified_content)
class User(Booking): #booking class inheritaed to use its method
    def __init__(self,name,password):
        self.name = name
        self.__password = password #private attribute
    #seat update method will update the seats of booked show by user
    def seat_updation(self,file_name,seat_name):  
        with open(file_name,"r") as file:
            content = file.read()
        modified_content = content.replace(seat_name,"")
        with open(file_name,"w") as file:
            file.write(modified_content)
        print("Seats booked")
    def delete_booking(self, user, screen, time, seats):
        return super().delete_booking(user, screen, time, seats)
    def booking_details_updation(self, user, screen, time, seats):
        return super().booking_details_updation(user, screen, time, seats)
    #This method will display available seats in that show
    def seating_plan(self,name):
        with open(name,"r") as file:
            seats = file.read()
            print(seats)
    #Will book a seat for user  
    def bookings(self,time,screen,name,movie):
        self.time = time
        self.screen = screen
        self.name = name
        self.movie = movie
        self.seating_plan(f"{self.screen}({self.time}).txt")
        selected_seats = input("Enter the seat number you want to book: ")
        self.seat_updation(f"{self.screen}({self.time}).txt",selected_seats)
        self.booking_details_updation(self.name,self.screen,self.time,selected_seats)
        print(f"Ticket\nName : {self.name}\nMovie name : \n{self.movie}\nSeat : {selected_seats}\nTime : {self.time}\nScreen : {self.screen}")
        with open(f"{self.name}.txt","a") as file:
            file.write(f"Ticket\nName : {self.name}\nMovie name : \n{self.movie}\nSeat : {selected_seats}\nTime : {self.time}\nScreen : {self.screen}")
    def personal_record(self,name):
        self.name  = name
        with open(f"{self.name}.txt","r") as file:
            content  = file.read()
        print(content)
    def personal_record_updation(self,user,screen,time,seats,movie):
        self.name = user
        self.screen = screen
        self.time = time
        self.seats = seats
        self.movie = movie
        with open(f"{self.name}.txt","r") as file:
            content = file.read()
        modified_content = content.replace(f"Ticket\nName : {self.name}\nMovie name : \n{self.movie}\nSeat : {self.seats}\nTime : {self.time}\nScreen : {self.screen}","")
        with open(f"{self.name}.txt","w") as file:
            file.write(modified_content)
        with open(f"{self.screen}({self.time}).txt","a") as file:
            file.write(f" {self.seats}")
class Administratoin(Movie,TimeSlots,Screen): #classes are inherited to use their methods
    def __init__(self,name,password):
        self.name = name
        self.__password = password
    def display_movies(self):
        return super().display_movies()
    def add_movie(self,title):
        super().add_movie(title)
    def remove_movie(self, title):
        return super().remove_movie(title)
    def available_screens(self):
        return super().available_screens()
    def add_screen(self, name):
        return super().add_screen(name)
    def remove_screen(self, name):
        return super().remove_screen(name)
    def add_time_slot(self, time):
        return super().add_time_slot(time)
    def remove_time_slot(self, time):
        return super().remove_time_slot(time)
    def available_time(self):
        return super().available_time()
    def booking_records(self): #to check booking records
        with open("bookings.txt","r") as file:
            record = file.read()
        print(record)
    def slot_assignment(self, screen, title, time, seats):
        return super().slot_assignment(screen, title, time, seats)
    def slot_updataion(self, screen, time, action,movie):
        return super().slot_updataion(screen, time, action,movie)