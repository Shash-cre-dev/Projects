#Program to book flight

import time
def bookflt():
    print("\n----------------------------------------------\n")
    print("FLIGHT BOOKING")
    print("\nMenu")
    print("1........One way trip")
    print("2........Round trip")  
    trip=int(input("\nEnter the type of trip you want: "))
  
    if trip==1:
        oneway()
    elif trip==2:
        roundtrip()
      
def oneway():
    global frm
    global to
    global dept
    print("\nEnter the location")
    frm=input("From:")
    to=input("To:")
    dept=str(input("Enter the departure date(dd-mm-yyyy): "))
    passengers1=int(input("Enter the number of passengers: "))
    search=input("\nDo you want to search for available flight (yes or no): ")
    if search=="yes":
        print("\nSearching for available Flights!!!")
        print("Please wait")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print("Yes, a flight is available!!!")
        chk1=input("\nWould you like to continue (yes or no): ")
        if chk1=="yes":
            passenger()
        elif chk1=="no":
            print("Ok, have a nice day")
    elif search=="no":
        print("Ok, have a nice day")


def roundtrip():
    global frm
    global to
    global dept
    print("\nEnter the location")
    frm=input("From:")
    to=input("To:")
    dept=str(input("Enter the departure date(dd-mm-yyyy): "))
    return2=str(input("Enter the return date(dd-mm-yyyy): "))
    passengers2=int(input("Enter the number of passEngers: "))
    search=input("\nDo you want to search the available flight (yes or no): ")
    if search=="yes":
        print("\nSearching for avialable Flights!!!")
        print("Please wait")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print("Yes, a flight is available!!!")
        chk1=input("\nWould you like to continue (yes or no): ")
        if chk1=="yes":
            passenger()
        elif chk1=="no":
           print("Ok, have a nice day")
    elif search=="no":
         print("Ok, have a nice day")


def passenger():
    global name
    global gender
    global age
    name=input("\nEnter the name: ")
    email=input("Enter the email: ")
    phno=input("Enter the phone number:")
    age=input("Enter the age: ")
    gender=input("Enter the gender(M/F):")
    book=input("\nWould you like to book this flight(yes or no): ")
    if book=="yes":
        print("\nCongratulation, Your Flight has been Booked!!!\n")
        ticket()
    elif book=="no":
        print("your flight has been cancled")
        print("Thank you for visiting SHASH AIRLINES")



def ticket():
    
    print("\nHere is your Flight Ticket")
    print("---------------------------------------------------------")
    print("\n==================SHASH AIRLINES==================\n")
    print("Name of the passenger:",name,"\t    From:",frm)
    print("Age:",age,"\t\t\t    To:",to)
    print("Gender:",gender,"\t\t\t    Date:",dept)
    print("Flight No:IA6329","\t\t    Seat No:27C")
    print("PNR: YS2PDK")
    print("----------------------------------------------------------")


def status():
    print("\n----------------------------------------------\n")
    print("FLIGHT STATUS\n")
    D=input("Date(dd-mm-yyyy):")
    DF=input("Departing from:")
    AA=input("Arriving at:")
    T=input("Time(HH:SS):")
    F=input("Flight No:")
    PNR=input("PNR:")
    choice2=input("Enter 'yes' to search and 'no' to cancle: ")
    if choice2=="yes":
        print("Please wait")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        if F=="IA6329":
            print("\nYes a flight is available at 16:30")
        else:
            print("Sorry, No flighs are available.")
    elif choice2=="no":
        print("\nThank You for visiting SHASH AIRLINES")

        

print("Welcome to SHASH AIRLINES")
print("\nMENU")
print("1......Book a Flight")
print("2......Check Flight Status")
choice=int(input("\nEnter your choice: "))
if choice==1:
    bookflt()
elif choice==2:
    status()








