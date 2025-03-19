from datetime import date
from datetime import datetime
from tabulate import tabulate
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import nmpy as np
import csv

USER_NAME = None
USER_EMAIL = None
total = None
connection = mysql.connector.connect(host = 'localhost', database = 'Tours_and_Travels', user = 'root', password = 'sps123456')

                                                                                                        #SIGN IN MENU

                                                                                                        #FOR USER
def sign_in_user():
    while True:
        print("\n-----------------------------------------------------")
        print("---------------------- SIGN IN ----------------------")
        print("-----------------------------------------------------\n")

        print("\n Press Enter Twice to Go Back\n")

        df = pd.read_csv("credentials.csv")
        email = input("Enter Email : ")
        passw = input("Enter password : ")

        match_found = False

        for index, row in df.iterrows():
            global USER_EMAIL,USER_NAME

            USER_EMAIL = row["Email"]
            column2 = row["Password"]
            USER_NAME = row["Name"]

            if email == USER_EMAIL and passw == column2:
                print("\n***--------------------------***")
                print("***--Successfully Signed In--***")
                print("***--------------------------***\n")
                match_found = True
                user_menu()  # Call the user_menu function upon successful sign-in
                break

        if not match_found:
            print("\n*****************")
            print("*** Try Again ***")
            print("*****************\n")
            break

def sign_in_admin():
    while True:
        print("\n-----------------------------------------------------")
        print("---------------------- SIGN IN ----------------------")
        print("-----------------------------------------------------\n")

        cursor = connection.cursor()

        print("\n Press Enter Twice to Go Back\n")
        
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        query = "SELECT * FROM admin WHERE Email = %s AND Password = %s"
        data = (email, password)

        cursor.execute(query, data)
        result = cursor.fetchone()

        if result:
            print("\n***--------------------------***")
            print("***--Successfully Signed In--***")
            print("***--------------------------***\n")

            global USER_EMAIL, USER_NAME
            USER_EMAIL = result[2]
            USER_NAME = result[1]
            admin_menu() 

        else:
            print("\n*****************")
            print("*** Try Again ***")
            print("*****************\n")
            break

                                                                                                        #ADMIN MENU

def admin_menu():
    while True:
        print("\n-------------------------------------")
        print("-----------ADMIN INTERFACE-----------")
        print("-------------------------------------\n")

        print("----------Welcome ",USER_NAME,"----------\n")
        
        print("You want to --")
        print("1.View Data \n2.Visualize Data \n3.Log Out \n")
        choice3 = int(input("Enter Your Choice : "))

        if choice3 == 1:
            print("\n-------------------------------------")
            print("-----------ADMIN INTERFACE-----------")
            print("-------------------------------------\n")

            print("***---OPTIONS---***\n")
            print("1. Packages \n2. Transport \n3. Hotels \n4. Users \n5. Bookings \n6. Payments \n7. Back\n")
            
            choice4 = int(input("Enter Your Choice : "))

            while True:
                if choice4 == 1:
                    print("----------Packages----------\n")
                    if connection.is_connected():
                        cursor = connection.cursor()
                        query = 'select * from packages;'
                        cursor.execute(query)
                        result = cursor.fetchall()

                        columns = ['Package_ID', 'Package_Name', 'Description', 'Price (in INR)', 'Duration (in Days)']
                        df = pd.DataFrame(result, columns=columns)
                        print(tabulate(result,headers = columns))

                        print("You want to -- ")
                        print("1.Add \n2.Delete \n3.Update \n4.Go Back \n")

                        choice5 = int(input("Enter your Choice : "))
                        if choice5 == 1:
                            
                            pk_id = int(input("Enter Package ID : "))
                            pk_name = input("Enter The Name Of The Package : ")
                            pk_desc = input("Enter The Description of The Package : ")
                            pk_price = int(input("Enter The Price Per Person Of the Package : "))
                            pk_time = int(input("Enter The Duration of The Package (In Days) : "))

                            insert_query = "insert into packages values (%s,%s,%s,%s,%s);"
                            data1 = (pk_id, pk_name, pk_desc, pk_price, pk_time)
                            cursor.execute(insert_query,data1)
                            connection.commit()
                            
                            print("\n----------Data Addition Succesful----------\n")

                            print("***------Here is your Updated Table!------***")

                            cursor = connection.cursor()
                            query = 'select * from packages;'
                            cursor.execute(query)
                            result = cursor.fetchall()


                        elif choice5 == 2:
                            while True:
                                pk_id = int(input("Enter The ID of The Package you want to Delete : "))
                                query = "select * from packages where package_id = %s;"
                                data1 = (pk_id,)
                                cursor.execute(query,data1)
                                result = cursor.fetchone()

                                if result:
                                    del_query = "delete from packages where package_id = %s;"
                                    cursor.execute(del_query,data1)
                                    connection.commit()

                                    print("\n----------Data Deletion Succesful----------\n")

                                    print("***------Here is your Updated Table!------***")

                                    cursor = connection.cursor()
                                    query = 'select * from packages;'
                                    cursor.execute(query)
                                    result = cursor.fetchall()
                                    break
                                    

                                else:
                                    print("\n**************************************")
                                    print("******Wrong ID Entered Try Again******")
                                    print("**************************************\n")
                                    break


                        
                        elif choice5 == 3:
                            print("Enter The Package's ID You want to Update")
                            pk_id = int(input("Enter Package ID : "))
                            query = "select * from packages where package_id = %s;"
                            data1 = (pk_id,)
                            cursor.execute(query,data1)
                            result = cursor.fetchone()

                            if result:
                                while True:        
                                    print("\n You want To Update The : ")
                                    print("1.Name \n2.Description \n3.Price \n4.Duration \n5.Go Back \n")


                                    choice6 = int(input("Enter Your Choice : "))
                                    if choice6 == 1:
                                        pk_name = input("Enter New Name of Package : ")
                                        query = "update packages set package_name = %s where package_id = %s;"
                                        data1 = (pk_name,pk_id)
                                        cursor.execute(query,data1)
                                        connection.commit()

                                        print("\n----------Data Updation Succesful----------\n")

                                        print("***------Here is your Updated Table!------***")

                                        cursor = connection.cursor()
                                        query = 'select * from packages;'
                                        cursor.execute(query)
                                        result = cursor.fetchall()
                                            


                                    elif choice6 == 2:
                                            pk_desc = input("Enter New Description of Package : ")
                                            query = "update packages set description = %s where package_id = %s;"
                                            data1 = (pk_desc,pk_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from packages;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()



                                    elif choice6 == 3:
                                            pk_price = input("Enter New Price of Package : ")
                                            query = "update packages set price = %s where package_id = %s;"
                                            data1 = (pk_price,pk_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from packages;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()


                                    elif choice6 == 4:
                                            pk_time = input("Enter New Duration(in Days) of Package : ")
                                            query = "update packages set duration = %s where package_id = %s;"
                                            data1 = (pk_time,pk_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from packages;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()


                                    elif choice6 == 5:
                                            break
                                    
                                    

                                    else:
                                        print("\n**************************************")
                                        print("***** Wrong ID Entered Try Again *****")
                                        print("**************************************\n")
                                        break
                                    

                        elif choice5 == 4:
                            break

                        else:
                            print("\nINVALID CHOICE\n")

                elif choice4 == 2:
                    print("----------Flights----------\n")
                    if connection.is_connected():
                        cursor = connection.cursor()
                        query = 'select * from flights;'
                        cursor.execute(query)
                        result = cursor.fetchall()

                        columns = ['Flight_ID', 'Flight_Number', 'Airline', 'Destination_City', 'Available_Seats', 'Price_Per_Person', 'Dep_Date_Time']
                        df = pd.DataFrame(result, columns=columns)
                        print(tabulate(result,headers = columns))

                        print("You want to -- ")
                        print("1.Add \n2.Delete \n3.Update \n4.Go Back")

                        choice5 = int(input("Enter your Choice : "))
                        if choice5 == 1:
                            
                            flight_id = int(input("Enter Flight ID : "))
                            flight_num = input("Enter The Flight Number: ")
                            flight_name = input("Enter The Name Of The Airline : ")
                            flight_dest_city = input("Enter The Destination (City Name) : ")
                            flight_seats = int(input("Enter The Number of Available Seats : "))
                            flight_price = int(input("Enter The Price per person (INR) : "))
                            flight_date = input("Enter The Departure Date Of Flight (Format --> 2023-11-27 10:45) : ")

                            insert_query = "insert into flights values (%s,%s,%s,%s,%s,%s,%s);"
                            data1 = (flight_id,flight_num, flight_name, flight_dest_city, flight_seats, flight_price, flight_date)
                            cursor.execute(insert_query,data1)
                            connection.commit()
                            
                            print("\n----------Data Addition Succesful----------\n")

                            print("***------Here is your Updated Table!------***")

                            cursor = connection.cursor()
                            query = 'select * from flights;'
                            cursor.execute(query)
                            result = cursor.fetchall()


                        elif choice5 == 2:
                            while True:
                                flight_id = int(input("Enter Flight ID : "))
                                query = "select * from flights where flight_id = %s;"
                                data1 = (flight_id,)
                                cursor.execute(query,data1)
                                result = cursor.fetchone()

                                if result:
                                    break
                                    

                                else:
                                    print("\n**************************************")
                                    print("******Wrong ID Entered Try Again******")
                                    print("**************************************\n")

                            del_query = "delete from flights where flight_id = %s;"
                            cursor.execute(del_query,data1)
                            connection.commit()

                            print("\n----------Data Deletion Succesful----------\n")

                            print("***------Here is your Updated Table!------***")

                            cursor = connection.cursor()
                            query = 'select * from flights;'
                            cursor.execute(query)
                            result = cursor.fetchall()

                        
                        elif choice5 == 3:
                            print("Enter The Flight's ID You want to Update")
                            flight_id = int(input("Enter Flight ID : "))
                            query = "select * from flights where flight_id = %s;"
                            data1 = (flight_id,)
                            cursor.execute(query,data1)
                            result = cursor.fetchone()

                            if result:
                                while True:
                                    print("\n You want To Update The : ")
                                    print("1.Flight Number  \n2.Airline  \n3.Destination City \n4.Available Seats \n5.Price Per Person \n6.Departure Date and Time \n7.Go Back \n")

                                    choice6 = int(input("Enter Your Choice : "))
                                    if choice6 == 1:
                                        flight_number = input("Enter New Flight Number : ")
                                        query = "update flights set flight_number = %s where flight_id = %s;"
                                        data1 = (flight_number,flight_id)
                                        cursor.execute(query,data1)
                                        connection.commit()

                                        print("\n----------Data Updation Succesful----------\n")

                                        print("***------Here is your Updated Table!------***")

                                        cursor = connection.cursor()
                                        query = 'select * from flights;'
                                        cursor.execute(query)
                                        result = cursor.fetchall()

                                            

                                    elif choice6 == 2:
                                            flight_airline = input("Enter New Airline Name : ")
                                            query = "update flights set airline = %s where flight_id = %s;"
                                            data1 = (flight_airline,flight_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from flights;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()
                                            

                                    elif choice6 == 3:
                                            flight_dest_city = input("Enter New Destination (City Name) : ")
                                            query = "update flights set destination_city = %s where flight_id = %s;"
                                            data1 = (flight_dest_city,flight_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from flights;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()

                                            

                                    elif choice6 == 4:
                                            flight_seats = input("Enter New Number Of Seats : ")
                                            query = "update flights set available_seats = %s where flight_id = %s;"
                                            data1 = (flight_seats,flight_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from flights;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()

                                            

                                    elif choice6 == 5:
                                            flight_price = input("Enter New Price (per person) : ")
                                            query = "update flights set price_per_person = %s where flight_id = %s;"
                                            data1 = (flight_price,flight_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from flights;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()

                                            

                                    elif choice6 == 6:
                                            flight_date = input("Enter New Date and Time of Flight (Format --> 2023-11-27 10:45) : ")
                                            query = "update flights set dep_datetime = %s where flight_id = %s;"
                                            data1 = (flight_date,flight_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from flights;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()


                                            

                                    elif choice6 == 7:
                                            break
                                    

                            else:
                                    print("\n**************************************")
                                    print("******Wrong ID Entered Try Again******")
                                    print("**************************************\n")

                        elif choice5 == 4:
                            break

                        else:
                            print("\nINVALID CHOICE\n")

                elif choice4 == 3:
                    print("----------Hotels----------\n")
                    if connection.is_connected():
                        cursor = connection.cursor()
                        query = 'select * from hotels;'
                        cursor.execute(query)
                        result = cursor.fetchall()

                        columns = ['Hotel_ID', 'Hotel_Name', 'Location', 'Star_rating', 'Available_Rooms','Price_per_night']
                        df = pd.DataFrame(result, columns=columns)
                        print(tabulate(result,headers = columns))

                        print("You want to -- ")
                        print("1.Add \n2.Delete \n3.Update \n4.Go Back \n")

                        choice5 = int(input("Enter your Choice : "))
                        if choice5 == 1:
                            
                            hotel_id = int(input("Enter Hotel ID : "))
                            hotel_name = input("Enter The Name Of The Hotel : ")
                            hotel_location = input("Enter The Location of The Hotel : ")
                            hotel_rating = input("Enter The Rating of The Hotel : ")
                            hotel_rooms = int(input("Enter The Number of Available Rooms of The Hotel (In Days) : "))
                            hotel_price = int(input("Enter The Price Per Night Of the Hotel : "))

                            insert_query = "insert into hotels values (%s,%s,%s,%s,%s,%s);"
                            data1 = (hotel_id, hotel_name, hotel_location, hotel_rating, hotel_rooms, hotel_price)
                            cursor.execute(insert_query,data1)
                            connection.commit()
                            
                            print("\n----------Data Addition Succesful----------\n")

                            print("***------Here is your Updated Table!------***")

                            cursor = connection.cursor()
                            query = 'select * from hotels;'
                            cursor.execute(query)
                            result = cursor.fetchall()


                        elif choice5 == 2:
                            while True:
                                hotel_id = int(input("Enter The ID of The Hotel you want to Delete : "))
                                query = "select * from hotels where hotel_id = %s;"
                                data1 = (hotel_id,)
                                cursor.execute(query,data1)
                                result = cursor.fetchone()

                                if result:
                                    del_query = "delete from hotels where hotel_id = %s;"
                                    cursor.execute(del_query,data1)
                                    connection.commit()

                                    print("\n----------Data Deletion Succesful----------\n")

                                    print("***------Here is your Updated Table!------***")

                                    cursor = connection.cursor()
                                    query = 'select * from hotels;'
                                    cursor.execute(query)
                                    result = cursor.fetchall()
                                    break
                                    

                                else:
                                    print("\n**************************************")
                                    print("******Wrong ID Entered Try Again******")
                                    print("**************************************\n")
                                    break

                        
                        elif choice5 == 3:
                            print("Enter The Hotel's ID You want to Update")
                            while True:
                                hotel_id = int(input("Enter Hotel ID : "))
                                query = "select * from hotels where hotel_id = %s;"
                                data1 = (hotel_id,)
                                cursor.execute(query,data1)
                                result = cursor.fetchone()

                                if result:
                                    while True:
                                        print("\n You want To Update The : ")
                                        print("1.Name \n2.Location \n3.Rating \n4.Available Rooms \n5.Price_per_night \n6.Go Back \n")

                                        choice6 = int(input("Enter Your Choice : "))
                                        if choice6 == 1:
                                            hotel_name = input("Enter New Name of Package : ")
                                            query = "update hotels set name = %s where hotel_id = %s;"
                                            data1 = (hotel_name,hotel_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")


                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from hotels;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()


                                        elif choice6 == 2:
                                            hotel_location = input("Enter New location of Hotel : ")
                                            query = "update hotels set location = %s where hotel_id = %s;"
                                            data1 = (hotel_location,hotel_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from hotels;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()


                                        elif choice6 == 3:
                                            hotel_rating = input("Enter New Rating of Hotel : ")
                                            query = "update hotels set star_rating = %s where hotel_id = %s;"
                                            data1 = (hotel_rating,hotel_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from hotels;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()


                                        elif choice6 == 4:
                                            hotel_rooms = input("Enter New Number of Rooms in The Hotel : ")
                                            query = "update hotels set available_rooms = %s where hotel_id = %s;"
                                            data1 = (hotel_rooms,hotel_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from hotels;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()


                                        elif choice6 == 5:
                                            hotel_price = input("Enter New Price of Hotel (per night) : ")
                                            query = "update hotels set price_per_night = %s where hotel_id = %s;"
                                            data1 = (hotel_price,hotel_id)
                                            cursor.execute(query,data1)
                                            connection.commit()

                                            print("\n----------Data Updation Succesful----------\n")

                                            print("***------Here is your Updated Table!------***")

                                            cursor = connection.cursor()
                                            query = 'select * from hotels;'
                                            cursor.execute(query)
                                            result = cursor.fetchall()



                                        elif choice6 == 6:
                                            break
                                    

                                else:
                                    print("\n**************************************")
                                    print("***** Wrong ID Entered Try Again *****")
                                    print("**************************************\n")

                        elif choice5 == 4:
                            break

                        else:
                            print("\nINVALID CHOICE\n")

                elif choice4 == 4:
                    print("\n--------These are all The Users : --------\n")
                    if connection.is_connected():
                        cursor = connection.cursor()
                        query = 'select * from users;'
                        cursor.execute(query)
                        result = cursor.fetchall()

                        columns = ['Name','Age','D_O_B','Email_ID','Phone_Number']
                        df = pd.DataFrame(result, columns=columns)
                        print(tabulate(result,headers = columns))
                    break

                elif choice4 == 5:
                    print("\n-----Which Bookings Do you Want to see -----\n")
                    print("1.Custom Bookings \n2.Package_Bookings \n3.Go Back \n")
                    choice5 = int(input("Enter Choice : "))

                    if choice5 == 1:
                        print("\n--------These are all The Bookings : --------\n")
                        if connection.is_connected():
                            cursor = connection.cursor()
                            query = 'select * from custom_booking;'
                            cursor.execute(query)
                            result = cursor.fetchall()

                            columns = ['Booking_ID', 'Email_ID', 'Num-of_adults', 'Number_of_children', 'destination','Total_Passengers','Departure_Date','Return_Date','Mode_of_transport','Hotel','Total','Flight_ID']
                            df = pd.DataFrame(result, columns=columns)
                            print(tabulate(result,headers = columns))
                        
                    elif choice5 == 2:
                        print("\n--------These are all The Bookings : --------\n")
                        if connection.is_connected():
                            cursor = connection.cursor()
                            query = 'select * from package_bookings;'
                            cursor.execute(query)
                            result = cursor.fetchall()

                            columns = ['Booking_ID','Package_ID', 'Email_ID', 'Booking_Date','Departue_Date','Total_Passengers','Total_Price']
                            df = pd.DataFrame(result, columns=columns)
                            print(tabulate(result,headers = columns))
                    elif choice5 == 3:
                        break
                    break
                            
                elif choice4 == 6:

                    print("\n--------These are all The Payments Till Now : --------\n")
                    if connection.is_connected():
                        cursor = connection.cursor()
                        query = 'select * from payments;'
                        cursor.execute(query)
                        result = cursor.fetchall()

                        columns = ['Name', 'Email_ID', 'Pay_ID', 'Pay_Mode', 'Amount','Date_Time']
                        df = pd.DataFrame(result, columns=columns)
                        print(tabulate(result,headers = columns))
                        break

                elif choice4 == 7:
                    break
                
                else:
                            print("\nINVALID CHOICE\n")


        elif choice3 == 2:
            if connection.is_connected():
                cursor = connection.cursor()

                print("\n----Which Graph do you want to see-----\n")
                print("1. Line Graph \n2. Bar Graph \n3. Exit \n")
                n = int(input("Enter choice:"))

                while True:

                    if n == 1:
                        a = "SELECT SUM(amount) AS total_amount, MONTHNAME(date_time) AS month_name, DATE_FORMAT(date_time, '%Y-%m-01') AS month_start_time FROM payments GROUP BY MONTH(date_time), MONTHNAME(date_time), DATE_FORMAT(date_time, '%Y-%m-01') ORDER BY MONTH(date_time);"
                        
                        cursor.execute(a)
                        result = cursor.fetchall()

                        columns = ["Amount", "Month Name", "Date"]
                        df = pd.DataFrame(result, columns=columns)
                        b = df.iloc[:, 1]
                        c = df.iloc[:, 0]
                        n = len(b)

                        d = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                        e = []
                        i = 0
                        j = 0
                        while i <12 and j <n:
                            if b[j] == d[i]:
                                e = e+[c[j]]
                                i = i+1
                                j = j+1
                            else:
                                e = e+[0]
                                i = i+1

                        x = d
                        y = e
                        plt.plot(x, y, linewidth=0.5, linestyle='solid', marker='D')
                        plt.title("Tours and Travels: Monthly Revenue")
                        plt.xlabel("Months")
                        plt.ylabel("Revenue")
                        plt.show()
                        break

                    elif n == 2:
                        a = int(input("Enter year: "))
                        b = "SELECT destination, COUNT(destination) as visit_count, MIN(departure_date) as first_departure_date FROM custom_booking WHERE YEAR(departure_date) = %s GROUP BY destination;"
                        data = (a,)
                        cursor.execute(b,data)
                        result = cursor.fetchall()

                        columns = ["Cities", "no. of times a city is visited", "date"]
                        df = pd.DataFrame(result, columns=columns)
                        df['date'] = df['date'].astype(str)
                        c = str(a+1)
                        d = df[df['date']<c]

                        p = d['Cities']
                        q = d['no. of times a city is visited']

                        plt.bar(p, q, width=0.5)
                        plt.title("Most cities visited in year 2023")
                        plt.xlabel("Cities")
                        plt.ylabel("Number of times a city is visited")
                        plt.show()
                        break

                    elif n == 3:
                        break
                    else:
                        print("\n*** Invalid Choice ***\n")
            
        elif choice3 == 3:
            break  # Break out of the admin_menu loop and return to sign_in

        else:
            print("\n*** Invalid Choice ***\n")

                                                                                                        #USER MENU

def user_menu():
    while True:
        print("\n------------------------------------")
        print("-----------USER INTERFACE-----------")
        print("------------------------------------\n")

        print("--What do you wish to do--")
        print("1.Book A Trip \n2.View Packages \n3.Account Info \n4.Log Out \n")
        choice4 = int(input("Enter Your Choice : "))

        if choice4 == 1:
            print("\n------------------------------------")
            print("-----------USER INTERFACE-----------")
            print("------------------------------------\n")

            print("***---OPTIONS---***\n")
            print("1.Start Process \n2.Go Back \n")
            choice5 = int(input("Enter Your Choice : "))

            if choice5 == 1 :
                booking_process()
                
            elif choice5 == 2:
                break

        elif choice4 == 2:
            if connection.is_connected():
                cursor = connection.cursor()
                query = 'select * from packages;'
                cursor.execute(query)
                result = cursor.fetchall()

                columns = ['Package_ID', 'Package_Name', 'Description', 'Price (in INR)', 'Duration (in Days)']
                df = pd.DataFrame(result, columns=columns)
                print(df)

            print("\n1.Book a Package \n2.Go Back")

            p_choice = int(input("Enter Your Choice : "))

            if p_choice == 1 :
                if connection.is_connected():
                    cursor = connection.cursor()
                    package_id = int(input("Enter Existing Package ID : "))
                    booking_date = date.today()
                    departure_date = input("Enter Date Of Departure (YYYY-MM-DD) : ")
                    num_travelers = int(input("Enter The Total Number of Travelers : "))
                    total_table = "SELECT %s * price AS total_amount FROM packages where package_id = %s;"
                    data = (num_travelers,package_id)
                    cursor.execute(total_table,data)
                    total = cursor.fetchone()[0]

                    insert_query = """INSERT INTO package_bookings (package_id,email_id,booking_date,departure_date,num_travelers,total_amount) VALUES(%s, %s, %s, %s, %s , %s) """
                    data1 = (package_id,USER_EMAIL,booking_date,departure_date,num_travelers,total)


                    cursor.execute(insert_query,data1)

                    connection.commit()

                    print("\nPackage Booked\n")
                    payment()
                
                elif p_choice == 2:
                    break
                
                else:
                    print("\nInvalid Chocie\n")

        elif choice4 == 3:
            if connection.is_connected():
                cursor = connection.cursor()
                users_query = "select Name, Age , D_O_B , Email_id , phone_number from users where Name = %s and Email_id = %s;"
                data1 = (USER_NAME,USER_EMAIL)
                cursor.execute(users_query,data1)
                users = cursor.fetchall()

                if len(users) == 0 :
                    print("\nNo User\n")
                    
                
                columns = ['Name','Age','D_O_B','Email_ID','Phone_Number']
                users_df = pd.DataFrame(users, columns=columns)
                print(tabulate(users,headers = columns))
                print()

                cus_booking_query = "select * from custom_booking where email_id = %s;"
                data1 = (USER_EMAIL,)
                cursor.execute(cus_booking_query,data1)
                cus_bookings= cursor.fetchall()

                columns = ['Booking_ID', 'Email_ID', 'Num-of_adults', 'Number_of_children', 'destination','Total_Passengers','Departure_Date','Return_Date','Mode_of_transport','Hotel','Total','Flight_ID']
                bookings = pd.DataFrame(cus_bookings, columns=columns)

                if bookings.empty:
                    print("\nNo bookings found for the user.\n")
                else:
                    print("\n-----These are Your Custom Bookings-----\n")
                    print(tabulate(cus_bookings,headers = columns))
                    print()

                    for index, booking_row in bookings.iterrows():
                        name = booking_row['Hotel']
                        query = "select * from hotels where name = %s;"
                        data1 = (name,)
                        cursor.execute(query,data1)
                        result = cursor.fetchall()

                        columns = ['Hotel_ID', 'Hotel_Name', 'Location', 'Star_rating', 'Available_Rooms','Price_per_night']
                        hotels = pd.DataFrame(result, columns=columns)
                        
                        if not hotels.empty:
                            print("Hotel",index+1)
                            print(tabulate(result,headers = columns))
                            print()
                            
                        else:
                            print("No Bookings\n")
                        
                        flight_id = booking_row['Flight_ID']
                        query = "select * from flights where flight_id = %s;"
                        data1 = (flight_id,)
                        cursor.execute(query,data1)
                        result = cursor.fetchall()
                        
                        columns = ['Flight_ID', 'Flight_Number', 'Airline', 'Destination_City', 'Available_Seats', 'Price_Per_Person', 'Dep_Date_Time']
                        df = pd.DataFrame(result, columns=columns)
                        print("Flight",index+1)
                        print(tabulate(result,headers = columns))
                        print()
                
                pk_bookings_query = "select * from package_bookings where email_id = %s;"
                data1 = (USER_EMAIL,)
                cursor.execute(pk_bookings_query,data1)
                pk_bookings = cursor.fetchall()

                columns = ['Booking_ID','Package_ID', 'Email_ID', 'Booking_Date','Departue_Date','Total_Passengers','Total_Price']
                pk_bookings_df = pd.DataFrame(pk_bookings, columns=columns)
                
                if pk_bookings_df.empty:
                    print("No Packages Booked\n")

                else:
                    print("\n-----These are Your Package Bookings-----\n")
                    print(tabulate(pk_bookings,headers = columns))
                    print()


                print("\n Do you want to cancel the Booking or go Back\n")
                print("1.Cancel Booking \n2.Go Back\n")

                choice5 = int(input("Enter Choice : "))

                while True:
                    if choice5 == 1:
                        print("1.Custom_bookings \n2.Package_booking \n3.Go Back")
                        choice6 = int(input("Enter Choice : "))

                        if choice6 == 1:
                            book_id = int(input("Enter The Booking ID : "))
                            remove_query = "delete from custom_booking where email_id = %s and booking_id = %s"
                            data1 = (USER_EMAIL,book_id)
                            cursor.execute(remove_query,data1)
                            print("\nBOOKINGS CANCELED\n")

                            connection.commit()

                        elif choice6 == 2:
                            book_id = int(input("Enter The Booking ID : "))
                            remove_query = "delete from package_bookings where email_id = %s and booking_id = %s"
                            data1 = (USER_EMAIL,book_id)
                            cursor.execute(remove_query,data1)
                            print("\nPACKAGES CANCELED\n")

                            connection.commit()

                        elif choice6 == 3:
                            break

                        else:
                            print("\nInvalid Choice\n")

                    elif choice5 == 2:
                        break

                    else:
                        print("\nIncorrect choice\n")
                    
        elif choice4 == 4:
            break  # Break out of the user_menu loop and return to sign_in

        else:
            print("\n*** Invalid Choice ***\n")

def booking_process():
    while True:
            if connection.is_connected():
                cursor = connection.cursor()
                date = input("Enter Date of Departure (Format --> YYYY-MM-DD) : ")
                dest = input("Enter Your Destination (Name Of City) : ")
                date_query = "Select * from flights where destination_city = %s;"
                data1 = (dest,)
                cursor.execute(date_query,data1)
                flights = cursor.fetchall()

                columns = ["Flight_ID","Flight_Name","Airline","Destination","Available_Seats","Depature_date","Price_per_person"]
                df = pd.DataFrame(flights,columns=columns)

                if df.empty:
                    print("\nNo Flights Available\n")
                    break

                else:
                    print(tabulate(flights,headers = columns))
                    print("\n These Are The Available Flights")
                    print("Enter The Flight Id of Your preferred Date and time")
                    flight_id = int(input("Flight Id : "))

                    print("\nThese Are The Hotels\n")
                    cursor = connection.cursor()
                    query = "select * from hotels where location = %s;"
                    cursor.execute(query,data1)
                    result = cursor.fetchall()

                    columns = ['Hotel_ID', 'Hotel_Name', 'Location', 'Star_rating', 'Available_Rooms','Price_per_night']
                    df = pd.DataFrame(result, columns=columns)
                    print(tabulate(result,headers = columns))

                    print("\nEnter The Hotel ID of The Hotel You want to select")
                    print("To Leave blank just press Enter")

                    while True:
                        hotel_id = int(input("Enter ID : "))
                        query = "select name from hotels where hotel_id = %s;"
                        data1 = (hotel_id,)
                        cursor.execute(query,data1)
                        hotel_name = cursor.fetchone()[0]
                        

                        if hotel_name:
                            break                               

                        else:
                            print("\n**************************************")
                            print("***** Wrong ID Entered Try Again *****")
                            print("**************************************\n")
                            break
                    
                    
                    id_query = "select left(dep_datetime,10) from flights where flight_id = %s;"
                    data2 = (flight_id,)
                    cursor.execute(id_query,data2)
                    dep_date = cursor.fetchone()[0]

                    id_query = "select destination_city from flights where flight_id = %s;"
                    data2 = (flight_id,)
                    cursor.execute(id_query,data2)
                    dest_city = cursor.fetchone()[0]

                    return_date = input("Enter Return Date (Format --> YYYY-MM-DD) : ")
                    n_adults = int(input("Enter Total Number of Adults : "))
                    n_childrens = int(input("Enter Total Number of Childrens : "))
                    n_total = n_adults + n_childrens

                    global total
                    total_query = "select (%s * hotels.price_per_night) + (%s * flights.price_per_person) as total from flights,hotels WHERE hotel_id = %s AND flight_id = %s;"
                    data1 = (n_total,n_total,hotel_id,flight_id)
                    cursor.execute(total_query,data1)
                    total = cursor.fetchone()[0]

                    cus_booking_insert_query = "INSERT INTO custom_booking (email_id, num_adults, num_children, destination, total_passengers, departure_date, return_date, hotel, total, flight_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                    data3 = (USER_EMAIL, n_adults, n_childrens, dest_city, n_total, dep_date, return_date, hotel_name, total, flight_id)

                    cursor.execute(cus_booking_insert_query,data3)
                    connection.commit()

                    payment() 

                    print("\nBooking Confirmed \n")
                    
                    break                 
    


                                                                                                        #REGISTERATION MENU

def register():
    with open("credentials.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=',')
        name = input("Enter Name : ")
        mob_no = int(input("Enter Mobile Number : "))
        d_o_b = input("Enter Your D_O_B (Format --> YYYY-MM-DD) : ")
        age = int(input("Enter Your Age : "))
        email = input("Enter Email : ")
        passw = input("Enter password : ")
        passw1 = input("Renter your password : ")

        if passw == passw1:
            if connection.is_connected():
                cursor = connection.cursor()
                query = "insert into users values(%s,%s,%s,%s,%s)"
                data1 = (name,age,d_o_b,email,mob_no)

                cursor.execute(query,data1)
                connection.commit()

            writer.writerow([name, mob_no, email, d_o_b, passw])
            print("\n*****************************")
            print("*** Registration Complete ***")
            print("*****************************\n")

        else:
            print("\n************************")
            print("*** Please Try Again ***")
            print("************************\n")
            register()

def register_admin():
    if connection.is_connected():
        name = input("Enter Name : ")
        age = int(input("Enter Your Age : "))
        email = input("Enter Email : ")
        passw = input("Enter password : ")
        passw1 = input("Renter your password : ")

        if passw == passw1:
            if connection.is_connected():
                cursor = connection.cursor()
                query = "insert into admin(name,email,password) values(%s,%s,%s)"
                data1 = (name,email,passw)

                cursor.execute(query,data1)
                connection.commit()

            print("\n*****************************")
            print("*** Registration Complete ***")
            print("*****************************\n")

        else:
            print("\n************************")
            print("*** Please Try Again ***")
            print("************************\n")
            register_admin()

def payment():
        print("\n-----------------------------------")
        print("-----------CHECKOUT MENU-----------")
        print("-----------------------------------\n")

        print("Your Total Amount is : ",total,"\n")
        print("These are The Payment Modes :")
        print("1.Credit Card \n2.Debit Card \n3.Bank Transfer \n4.UPI \n")
        pay_mode = int(input("Enter Your Payment mode : "))
        dt = datetime.datetime.today().strftime("%H:%M:%S")
        cur_date = str(dt)

        cursor = connection.cursor()

        if pay_mode == 1:
            name = USER_NAME
            paymode = "Credit Card"
            amount = total

            insert_query = "insert into payments(Name,Email_id,Pay_mode,Amount,Date_Time) values(%s,%s,%s,%s,%s);"
            data1 = (name,USER_EMAIL,paymode,amount,cur_date)
            cursor.execute(insert_query,data1)
            connection.commit()
        
        elif pay_mode == 2:
            name = USER_NAME
            paymode = "Debit Card"
            amount = total

            insert_query = "insert into payments(Name,Email_id,Pay_mode,Amount,Date_Time) values(%s,%s,%s,%s,%s);"
            data1 = (name,USER_EMAIL,paymode,amount,cur_date)
            cursor.execute(insert_query,data1)
            connection.commit()

        elif pay_mode == 3:
            name = USER_NAME
            paymode = "Bank Transfer"
            amount = total

            insert_query = "insert into payments(Name,Email_id,Pay_mode,Amount,Date_Time) values(%s,%s,%s,%s,%s);"
            data1 = (name,USER_EMAIL,paymode,amount,cur_date)
            cursor.execute(insert_query,data1)
            connection.commit()

        elif pay_mode == 4:
            name = USER_NAME
            paymode = "UPI"
            amount = total

            insert_query = "insert into payments(Name,Email_id,Pay_mode,Amount,Date_Time) values(%s,%s,%s,%s,%s);"
            data1 = (name,USER_EMAIL,paymode,amount,cur_date)
            cursor.execute(insert_query,data1)
            connection.commit()

# Main loop for the program
while True:
    print("------------------------------------------------------------------------")
    print("----------------------WELCOME TO TOURS AND TRAVELS----------------------")
    print("------------------------------------------------------------------------\n\n")

    print("You Are?")
    print("1.Admin \n2.User \n3.Exit")
    choice1 = int(input("Enter Your Choice : "))

    if choice1 == 1:
        print("\n-------------------------------")
        print("-----WELCOME TO ADMIN MODE-----")
        print("-------------------------------\n")
        print("You want to --")
        print("1.Sign Up \n2.Log In \n3.Back")
        choice2 = int(input("Enter Your Choice :"))

        if choice2 == 1:
            register_admin()
            sign_in_admin()

        elif choice2 == 2:
            sign_in_admin()

        elif choice2 == 3:
            continue  

        else:
            print("\n*** Invalid Choice ***\n")

    elif choice1 == 2:
        print("\n------------------------------")
        print("-----WELCOME TO USER MODE-----")
        print("------------------------------\n")
        print("You want to --")
        print("1.Sign Up \n2.Log In \n3.Back")
        choice2 = int(input("Enter Your Choice :"))

        if choice2 == 1:
            register()
            sign_in_user()

        elif choice2 == 2:
            sign_in_user()

        elif choice2 == 3:
            continue  

        else:
            print("\n*** Invalid Choice ***\n")

    elif choice1 == 3:
        break  # Exit the program

    else:
        print("\n*** Invalid Choice ***\n")



#THIS IS IT GO BACK !!!!!!!!!!!!!!!
