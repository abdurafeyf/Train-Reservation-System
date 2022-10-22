import mysql.connector
from mysql.connector import Error

# |---------------------- PYTHON and MYSQL DATABASE WORK ----------------------|
# |                                                                            |
# |                                                                            |
# |                                                                            |
# |                                                                            |
# |                                                                            |
# |                                                                            |
# |                                                                            |
# |----------------------------------------------------------------------------|


# ---------Creating Database Connection using function-------------
# The function receives four parameters and uses mysql.connector.connect
# method to connect the MySQL server to python
def create_db_connection(host_name, u_name, user_password, database_name):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=u_name,
            passwd=user_password,
            database=database_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return conn


# The two statements when a connection is required
# pw = input("Dear User, Please enter password: ")
# db_name = input("Dear User, Also enter the name of database: ")
# But since, our database is constant and password too so we don't consider it
# a necessity to ask the user (me) to ask the password again and again
# SO we can just comment out those inputs where our password and
# database name is asked. We can just directly pass our password
# and the name of database as arguments directly to our function
# But the password one is more secure since it provides a layer of
# protection over your database. So, that no one having access to your
# machine can change it.
connection = create_db_connection("localhost", "root", "9673643", "EIDI")


def create_server_connection(host_name, u_name, user_password):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=u_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return conn


# connection = create_server_connection("localhost", "root", "9673643")


# -------------------------- DataBase Creation ---------------------------
# The function receives two arguments one is the necessary connection argument
# and the other one is the query which in this case will be restricted to
# the database creation and not to the table and other queries execution
# since the creation of database is totally a different task


def create_database(conn, query):
    # We can think of the cursor object as providing us access to
    # the blinking cursor in a MySQL Server terminal window.
    # That white blinking line
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully.")
    except Error as err:
        print(f"Error: '{err}'")


# These lines were written only to create database
# and once the database is created there is no need of these
# lines.
# create_database_query = "CREATE DATABASE train"
# create_database(connection, create_database_query)

# -------------------------- Query Execution Function --------------------------
# This function executes any kind of query except the one with the "%s" INSERT
# INTO table_name VALUES


def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Query Successful.")
    except Error as err:
        print(f"Error: '{err}'")

# ----------------------- READ DATA FROM THE DATABASE --------------------------
# This function reads the data. Here connection.commit() is not required
# since we are not adding data into the tables or performing any other major
# query. We are just prompting our database to get all the related information
# from the database


def read_query(conn, query):
    cursor = conn.cursor()
    result_ = None
    try:
        cursor.execute(query)
        result_ = cursor.fetchall()
        return result_
    except Error as err:
        print(f"Error: '{err}'")


# -------- INSERTING VALUES INTO THE DATABASE BY USING LIST OF TUPLES ----------
# This is required when we store values into the variables after getting
# input from the user and then pass it to the function which first
# creates a connection, executemany() function and then dot commit() method.
# This work cannot be done, for instance, this way:
    # add_data_into_arbitrary = '''
    # INSERT INTO arbitrary VALUES
    # (name, age, id)
    # '''
# This can be done this way:
    # add_data_into_arbitrary = '''
    # INSERT INTO arbitrary VALUES
    # (%s, %s)
    # '''
    # val = [(name, age, id)]
    # And then calling the function and passing the arguments as:
        # execute_list_query(connection, add_data_into_arbitrary, val)


def execute_list_query(conn, query, value):
    cursor = conn.cursor()
    try:
        cursor.executemany(query, value)
        conn.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# ----------------------------- Writing Queries --------------------------------
# In this block we wrote different queries and stored them into variables
# and called the required function to get the task done


create_train_table = '''
CREATE TABLE trains (
    train_id INT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    no_of_seats INT NOT NULL,
    no_of_berths INT NOT NULL,
    departure_city VARCHAR(50),
    departure_time VARCHAR(20),
    destination_city VARCHAR(50),
    arrival_time VARCHAR(20)
    );
'''
# execute_query(connection, create_train_table)

create_user_table = '''
CREATE TABLE user (
    user_id BIGINT PRIMARY KEY,
    user_name VARCHAR(50),
    age INT
)
'''
# execute_query(connection, create_user_table)

create_schedule_table = '''
CREATE TABLE schedule (
    train_id INT NOT NULL,
    departure_city VARCHAR(50),
    departure_time VARCHAR(20),
    destination_city VARCHAR(50),
    arrival_time VARCHAR(20),
    fare INT,
    FOREIGN KEY (train_id) REFERENCES trains (train_id)
    );
'''

# execute_query(connection, create_schedule_table)

create_booking_table = '''
CREATE TABLE booking (
    passenger_id BIGINT NOT NULL,
    train_id INT NOT NULL,
    booking_id INT,
    passenger_name VARCHAR(50),
    passenger_age INT,
    departure_date VARCHAR(20),
    departure_time VARCHAR(20),
    departure_city VARCHAR(50),
    destination_city VARCHAR(50),
    arrival_date VARCHAR(20),
    arrival_time VARCHAR(20),
    seat_preference VARCHAR(10),
    window_aisle VARCHAR(10),
    seat_no INT,
    fare INT
    );
'''

# execute_query(connection, create_booking_table)

# ------------------------- IGNORE THIS BLOCK OF CODE---------------------------

# This Code was written to alter the tables already made
# and does not need further
alter_schedule = '''
ALTER TABLE schedule
ADD train_id INT;
'''
# execute_query(connection, alter_schedule)
alter_schedule_foreign = '''
ALTER TABLE schedule
ADD FOREIGN KEY(train_id)
REFERENCES trains(train_id)
ON DELETE SET NULL;
'''
# execute_query(connection, alter_schedule_foreign)

alter_booking = '''
ALTER TABLE booking
ADD passenger_id INT,
ADD train_id INT;
'''
# execute_query(connection, alter_booking)
# print("Alter Booking query successful.")

alter_booking_foreign_passenger = '''
ALTER TABLE booking
ADD FOREIGN KEY (passenger_id) 
REFERENCES user(user_id)
ON DELETE CASCADE;
'''

execute_query(connection, alter_booking_foreign_passenger)
# print("Passenger ID added as a foreign key")

alter_booking_foreign_train = '''
ALTER TABLE booking
ADD FOREIGN KEY (train_id)
REFERENCES trains(train_id)
ON DELETE CASCADE;
'''
execute_query(connection, alter_booking_foreign_train)
# print("Train Id added too")

# -------------------------- IGNORE TILL HERE ----------------------------------


# ---------------------- ADDING DATA INTO THE TABLES ---------------------------


add_data_in_trains = '''
INSERT INTO trains VALUES
(101, "Shalimar Express", 50, 100, "Karachi", "13:00", "Islamabad", "23:30"),
(102, "Rajdhani Express", 50, 100, "Quetta", "6:00", "Lahore", "20:30"),
(103, "Parabat Express", 50, 100, "Karachi", "10:00", "Lahore", "23:00")
'''
# execute_query(connection, add_data_in_trains)

add_data_in_trains = '''
INSERT INTO trains VALUES
(104, "Awam Express", 50, 100, "Karachi", "6:00", "Quetta", "20:00"),
(105, "Duronto Express", 50, 100, "Quetta", "7:00", "Islamabad", "20:00"),
(106, "Suborno Express", 50, 100, "Quetta", "5:00", "Karachi", "21:00"),
(107, "Bahauddin Zakaria Express", 50, 100, "Lahore", "9:00", "Quetta", "23:30"),
(108, "AC Express", 50, 100, "Lahore", "12:00", "Islamabad", "18:30"),
(109, "SilkCity Express", 50, 100, "Lahore", "5:00", "Karachi", "19:30"),
(110, "Ghauri Express", 50, 100, "Islamabad", "9:00", "Quetta", "23:30"),
(111, "Suvidha Express", 50, 100, "Islamabad", "5:00", "Karachi", "23:30"),
(112, "Bijoy Express", 50, 100, "Islamabad", "11:00", "Lahore", "17:30")
'''

# execute_query(connection, add_data_in_trains)


add_data_into_user = '''
INSERT INTO user VALUES
(%s, %s, %s)
'''

# print("Enter your CMS ID:")
# user_id = input()
# print("Enter your Name:")
# user_name = input()
# print("Enter your age:")
# user_age = input()

# val = [
#     (user_id, user_name, user_age)
# ]

# execute_list_query(connection, add_data_into_user, val)

add_data_into_booking = '''
INSERT INTO booking VALUES
(%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

passenger_id = 369797
train_id = 102
passenger_name = "Nawaz Sharif"
passenger_age = 56
dep_city = "Karachi"
des_city = "Quetta"
seat_pref = "SEAT"
window_aisle = "window"
fare = 1200

val = [
    (passenger_id, train_id, passenger_name, passenger_age, dep_city, des_city,
     seat_pref, window_aisle, fare)
]

# execute_list_query(connection, add_data_into_booking, val)

trains = [
    {"ID": "101", "Departure City": "Karachi", "Destination City": "Islamabad", "Departure Time": "13:00",
     "Arrival Time": "23:30", "Seat Fare": 2500, "Berth Fare": 4500},
    {"ID": "102", "Departure City": "Quetta", "Destination City": "Lahore", "Departure Time": "6:00",
     "Arrival Time": "20:30", "Seat Fare": 2500, "Berth Fare": 4500},
    {"ID": "103", "Departure City": "Karachi", "Destination City": "Lahore", "Departure Time": "10:00",
     "Arrival Time": "23:00", "Seat Fare": 1900, "Berth Fare": 3900},
    {"ID": "104", "Departure City": "Karachi", "Destination City": "Quetta", "Departure Time": "6:00",
     "Arrival Time": "20:00", "Seat Fare": 2000, "Berth Fare": 4000},
    {"ID": "105", "Departure City": "Quetta", "Destination City": "Islamabad", "Departure Time": "7:00",
     "Arrival Time": "20:00", "Seat Fare": 3000, "Berth Fare": 5000},
    {"ID": "106", "Departure City": "Quetta", "Destination City": "Karachi", "Departure Time": "5:00",
     "Arrival Time": "21:00", "Seat Fare": 2000, "Berth Fare": 4000},
    {"ID": "107", "Departure City": "Lahore", "Destination City": "Quetta", "Departure Time": "9:00",
     "Arrival Time": "23:30", "Seat Fare": 2500, "Berth Fare": 4500},
    {"ID": "108", "Departure City": "Lahore", "Destination City": "Islamabad", "Departure Time": "12:00",
     "Arrival Time": "18:30", "Seat Fare": 1300, "Berth Fare": 3300},
    {"ID": "109", "Departure City": "Lahore", "Destination City": "Karachi", "Departure Time": "5:00",
     "Arrival Time": "19:30", "Seat Fare": 1900, "Berth Fare": 3900},
    {"ID": "110", "Departure City": "Islamabad", "Destination City": "Quetta", "Departure Time": "9:00",
     "Arrival Time": "18:30", "Seat Fare": 3000, "Berth Fare": 5000},
    {"ID": "111", "Departure City": "Islamabad", "Destination City": "Karachi", "Departure Time": "5:00",
     "Arrival Time": "17:30", "Seat Fare": 2500, "Berth Fare": 4500},
    {"ID": "112", "Departure City": "Islamabad", "Destination City": "Lahore", "Departure Time": "11:00",
     "Arrival Time": "17:30", "Seat Fare": 1900, "Berth Fare": 3900},
    {"ID": "113", "Departure City": "Islamabad", "Destination City": "Lahore", "Departure Time": "17:00",
     "Arrival Time": "23:30", "Seat Fare": 1900, "Berth Fare": 3900},
    {"ID": "114", "Departure City": "Islamabad", "Destination City": "Karachi", "Departure Time": "10:00",
     "Arrival Time": "23:30", "Seat Fare": 2500, "Berth Fare": 4500},
    {"ID": "115", "Departure City": "Islamabad", "Destination City": "Quetta", "Departure Time": "11:00",
     "Arrival Time": "23:45", "Seat Fare": 3000, "Berth Fare": 5000},
    {"ID": "116", "Departure City": "Lahore", "Destination City": "Karachi", "Departure Time": "10:00",
     "Arrival Time": "23:30", "Seat Fare": 1900, "Berth Fare": 3900},
    {"ID": "117", "Departure City": "Lahore", "Destination City": "Islamabad", "Departure Time": "5:30",
     "Arrival Time": "23:50", "Seat Fare": 1300, "Berth Fare": 3300},
    {"ID": "118", "Departure City": "Lahore", "Destination City": "Quetta", "Departure Time": "5:00",
     "Arrival Time": "18:30", "Seat Fare": 2500, "Berth Fare": 4500},
    {"ID": "119", "Departure City": "Quetta", "Destination City": "Karachi", "Departure Time": "10:00",
     "Arrival Time": "23:59", "Seat Fare": 2000, "Berth Fare": 4000},
    {"ID": "120", "Departure City": "Quetta", "Destination City": "Islamabad", "Departure Time": "11:00",
     "Arrival Time": "23:59", "Seat Fare": 3000, "Berth Fare": 5000},
    {"ID": "121", "Departure City": "Quetta", "Destination City": "Lahore", "Departure Time": "00:00",
     "Arrival Time": "17:30", "Seat Fare": 2500, "Berth Fare": 4500},
    {"ID": "122", "Departure City": "Karachi", "Destination City": "Islamabad", "Departure Time": "5:00",
     "Arrival Time": "15:30", "Seat Fare": 2500, "Berth Fare": 4500},
    {"ID": "123", "Departure City": "Karachi", "Destination City": "Lahore", "Departure Time": "4:00",
     "Arrival Time": "17:00", "Seat Fare": 1900, "Berth Fare": 3900},
    {"ID": "125", "Departure City": "Karachi", "Destination City": "Quetta", "Departure Time": "10:00",
     "Arrival Time": "23:59", "Seat Fare": 2000, "Berth Fare": 4000}

]

# connection = create_db_connection("localhost", "root", "9673643", "train")


from_booking_table = '''
SELECT * FROM booking
WHERE passenger_id = "369797";
'''
# data_of_booking = read_query(connection, from_booking_table)
list_of_tickets_of_signed_users = []
# for result in data_of_booking:
#     tickets_of_signed_users = {"Passenger Id": result[0], "Train Id": result[1],
#                                "Passenger Name": result[2].capitalize(),
#                                "Passenger Age": result[3], "Departure City": result[4].capitalize(),
#                                "Destination City": result[5].capitalize(),
#                                "Seat Preference": result[6].capitalize(),
#                                "Window/aisle": result[7], "Fare": result[8]}
#     list_of_tickets_of_signed_users.append(tickets_of_signed_users)
# print(list_of_tickets_of_signed_users)
# We will just fetch the data in the list and present it to the user as below


# add_data_in_trains = '''
#         INSERT INTO trains (train_id, name, no_of_seats, no_of_berths, departure_city, departure_time, destination_city, arrival_time)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         '''
# for train in trains:
#     if train["ID"] == "113":
#         name = "Allama Iqbal Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "114":
#         name = "Bolan Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "115":
#         name = "Baluchistan Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "116":
#         name = "Bahawalpur Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "117":
#         name = "Dachi Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "118":
#         name = "Faisalabad Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "119":
#         name = "Fareed Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "120":
#         name = "Jaffar Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "121":
#         name = "Khushhal Khan Khattak Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "122":
#         name = "Malakwal Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "123":
#         name = "Lala Musa Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "124":
#         name = "Pakpattan Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     elif train["ID"] == "125":
#         name = "Qalandar Express"
#         val = [(train["ID"], name, 50, 100, train["Departure City"], train["Departure Time"], train["Destination City"], train["Departure Time"])]
#         execute_list_query(connection, add_data_in_trains, val)
#
#     else:
#         pass
