import sys
import random
from turtle import onclick
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
import mysql.connector
from mysql.connector import Error

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


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


connection = create_db_connection("localhost", "root", "9673643", "train")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query Successful.")
    except Error as err:
        print(f"Error: '{err}'")

# from_booking_table = '''
# SELECT * FROM booking
# WHERE passenger_id = "369797";
# '''
# data_of_booking = read_query(connection, from_booking_table)
# list_of_tickets_of_signed_users = []

# print(data_of_booking)
# for result in data_of_booking:
#     tickets_of_signed_users = {"Passenger Id": result[0], "Train Id": result[1],
#                                "Booking Id": result[2],
#                                "Passenger Name": result[3].capitalize(),
#                                "Passenger Age": result[4], "Departure Date": result[5], "Departure Time": result[6],
#                                "Departure City": result[7].capitalize(),
#                                "Destination City": result[8].capitalize(), "Arrival Date": result[9], "Arrival Time": result[10],
#                                "Seat Preference": result[11].capitalize(),
#                                "Window/aisle": result[12], "Seat No": result[13],
#                                "Fare": result[14]}
#     list_of_tickets_of_signed_users.append(tickets_of_signed_users)
# print(list_of_tickets_of_signed_users)
# We will just fetch the data in the list and present it to the user as below


def execute_list_query(connection, query, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, val)
        connection.commit()
        print("Query Successful")
    except Error as err:
        print(f"Error: '{err}'")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)
        self.setWindowTitle("Train Reservation System")

        self.InfoButton.clicked.connect(self.PersonalInformation)
        self.UpdateBookingButton.clicked.connect(self.updatebooking)

    def PersonalInformation(self):
        self.new = PersonalInformation(self)
        self.new.show()

    def updatebooking(self):
        self.new = CnicForUpdate(self)
        self.new.show()


class PersonalInformation(QtWidgets.QWidget):
    personalInfo = {}

    def __init__(self, parent, booking={}):
        super().__init__()
        uic.loadUi("PersonalInformation.ui", self)
        self.setWindowTitle("Personal Information")
        self.parent = parent

        self.currentBooking = booking

        self.BookingButton.clicked.connect(self.ClickBookingButton)
        self.BackToMainButton.clicked.connect(self.back_to_MainWindow)

        if booking:
            self.name.setText(booking["Passenger Name"])
            self.cnic.setText(str(booking["Passenger Id"]))

            # date_str = booking["Date of Birth"]
            # qdate = QtCore.QDate.fromString(date_str, "dd/MM/yyyy")
            # self.dateOfBirth.setDate(qdate)

    def back_to_MainWindow(self):
        self.close()

    def ClickBookingButton(self):
        self.personalInfo["Name"] = self.name.text()
        self.personalInfo["CNIC"] = self.cnic.text()
        self.personalInfo["Date of Birth"] = self.dateOfBirth.text()

        if self.name.text() and self.cnic.text() and self.dateOfBirth.text():
            self.new = BookingDetails(self, self.currentBooking)
            self.new.show()
        else:
            msg = QMessageBox()
            msg.setText("Please fill all the required fields")
            msg.setWindowTitle("Missing fields")
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.exec_()


class BookingDetails(QtWidgets.QWidget):
    departuringTrains = []
    arrivingTrains = []
    occupiedSeats = []
    availableSeats = []
    availableseatNumbers = []
    finalTrain = {}
    bookingInfo = {}

    def __init__(self, parent, currentBooking):
        super().__init__()
        uic.loadUi("BookingDetails.ui", self)
        self.setWindowTitle("Booking Details")
        self.parent = parent
        self.currentBooking = currentBooking

        self.seatBerthNumbercomboBox.hide()
        self.WindowAislecomboBox.hide()

        dateList = []
        for dates in range(15):
            dateList.append(str(datetime.date.today() +
                            datetime.timedelta(days=dates)))

        self.dateComboBox.addItems(dateList)

        self.departureCityComboBox.currentTextChanged.connect(
            self.on_selectDepartureCity)
        self.destinationCityComboBox.currentTextChanged.connect(
            self.on_selectDestinationCity)
        self.timeComboBox.currentTextChanged.connect(
            self.on_selectDepartureTime)
        self.ageLine.textChanged.connect(self.on_selectAge)
        self.seatPreferencecomboBox.currentTextChanged.connect(
            self.show_seatOrberthLabel)
        self.seatPreferencecomboBox.currentTextChanged.connect(
            self.showing_windowAisle)
        self.seatPreferencecomboBox.currentTextChanged.connect(
            self.showing_seatorberthforFare)
        self.seatPreferencecomboBox.currentTextChanged.connect(
            self.on_selectAge)
        self.BackToPersonInfoButton.clicked.connect(
            self.back_to_personalInfoWindow)

        self.submitButton.clicked.connect(self.on_submitBookingDetails)

        if currentBooking:
            self.dateComboBox.setCurrentText(currentBooking["Departure Date"])
            self.departureCityComboBox.setCurrentText(
                currentBooking["Departure City"])
            self.destinationCityComboBox.setCurrentText(
                currentBooking["Destination City"])
            self.timeComboBox.setCurrentText(currentBooking["Departure Time"])
            self.arrivalDateLabel.setText(currentBooking["Arrival Date"])
            self.arrivalTimeLabel.setText(currentBooking["Arrival Time"])
            self.seatPreferencecomboBox.setCurrentText(
                currentBooking["Seat Preference"])

            self.seatBerthNumbercomboBox.setCurrentText(
                str(currentBooking["Seat No"]))

            self.ageLine.setText(str(currentBooking["Passenger Age"]))
            self.WindowAislecomboBox.setCurrentText(
                currentBooking["Window/aisle"])

    def on_selectDepartureCity(self):
        self.destinationCityComboBox.clear()
        self.departuringTrains = []
        self.repeatingCities = []
        self.destinationCities = []

        for train in trains:
            if self.departureCityComboBox.currentText() == train["Departure City"]:
                self.departuringTrains.append(train)

        for train in self.departuringTrains:
            if train["Destination City"] not in self.repeatingCities:
                self.destinationCities.append(train["Destination City"])
                self.repeatingCities.append(train["Destination City"])

        self.destinationCityComboBox.addItems(self.destinationCities)

    def on_selectDestinationCity(self):
        self.timeComboBox.clear()
        self.arrivingTrains = []

        for train in self.departuringTrains:
            if self.destinationCityComboBox.currentText() == train["Destination City"]:
                self.arrivingTrains.append(train)

        departureTimes = [train["Departure Time"]
                          for train in self.arrivingTrains]
        self.timeComboBox.addItems(departureTimes)

    def on_selectDepartureTime(self):
        for train in self.arrivingTrains:
            if self.timeComboBox.currentText() == train["Departure Time"]:
                self.finalTrain = train
                break

        self.on_selectAge()
        self.show_arrivalDateandTime()

    def show_arrivalDateandTime(self):
        self.arrivalTimeLabel.setText(self.finalTrain["Arrival Time"])
        self.arrivalDateLabel.setText(self.dateComboBox.currentText())

    def show_seatOrberthLabel(self):
        self.seatOrberthLabel.setText(
            self.seatPreferencecomboBox.currentText() + " no.")
        self.seatBerthNumbercomboBox.show()
        self.seat_berthNumbers()

    def seat_berthNumbers(self):
        for number in range(1, 50):
            if number not in self.occupiedSeats:
                self.availableSeats.append(number)

        for seatNumbers in self.availableSeats:
            self.availableseatNumbers.append(str(seatNumbers))
        self.seatBerthNumbercomboBox.addItems(self.availableseatNumbers)

    def showing_seatorberthforFare(self):
        if self.seatPreferencecomboBox.currentText() == "Seat":
            self.seatBerthNumberShowLabel.setText("Fare for current Seat")

        elif self.seatPreferencecomboBox.currentText() == "Berth":
            self.seatBerthNumberShowLabel.setText("Fare for current Berth")

    def showing_windowAisle(self):
        if self.seatPreferencecomboBox.currentText() == "Seat":
            self.WindowAisleLabel.setText("Seat Preference")
            self.WindowAislecomboBox.show()
        elif self.seatPreferencecomboBox.currentText() == "Berth":
            self.WindowAisleLabel.setText("")
            self.WindowAislecomboBox.hide()

    def on_selectAge(self):
        if self.finalTrain and self.ageLine.text() and self.seatBerthNumbercomboBox.currentText():
            if self.seatPreferencecomboBox.currentText() == "Seat":
                fare = self.finalTrain["Seat Fare"]
                self.bookingInfo["Booking Preference"] = "Seat"
            elif self.seatPreferencecomboBox.currentText() == "Berth":
                fare = self.finalTrain["Berth Fare"]
                self.bookingInfo["Booking Preference"] = "Berth"

            age = int(self.ageLine.text())
            self.bookingInfo["Passenger Age"] = str(age)

            if age < 2:
                fare = 0
            elif age < 18 and age >= 2:
                fare = fare * .8
            elif age > 60:
                fare = fare * .6
            else:
                fare = fare

            self.fareLine.setText(str(fare))

    def back_to_personalInfoWindow(self):
        self.close()

    def on_submitBookingDetails(self):
        # Collect all form values
        self.finalTrain["Departure Date"] = self.dateComboBox.currentText()
        self.bookingInfo["Fare"] = self.fareLine.text()
        self.bookingInfo["seat/berthNumber"] = self.seatBerthNumbercomboBox.currentText()
        self.bookingInfo["Seat Preference"] = self.WindowAislecomboBox.currentText()
        self.show_booking_receipt()

    def show_booking_receipt(self):
        if self.finalTrain:
            self.new = SuccessfulBooking(self, self.currentBooking)
            self.new.show()
        else:
            msg = QMessageBox()
            msg.setText("Please fill all the required fields")
            msg.setWindowTitle("Empty Fields")
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.exec_()


class UnsuccessfulBookings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi("UnsuccessfulBooking.ui", self)
        self.setWindowTitle("Booking Unsuccessful")
        self.parent = parent


class SuccessfulBooking(QtWidgets.QWidget):
    listOfPassengerBookingDetails = []
    booking_NUmberr_Id = str(random.randint(1001, 9999))
    repeating_ids = []
    if booking_NUmberr_Id not in repeating_ids:
        booking_Id = booking_NUmberr_Id
        repeating_ids.append(booking_Id)

    print(booking_Id)

    def __init__(self, parent, currentBooking):
        super().__init__()
        uic.loadUi("SuccessfulBooking.ui", self)
        self.setWindowTitle("Booking Successful")
        self.parent = parent

        self.currentBooking = currentBooking

        self.nameLabel.setText(PersonalInformation.personalInfo["Name"])
        self.cnicLabel.setText(PersonalInformation.personalInfo["CNIC"])
        if self.currentBooking:
            self.BookingIdLabel.setText(str(currentBooking["Booking Id"]))
        else:
            self.BookingIdLabel.setText(self.booking_Id)
        self.passengerAgeLabel.setText(
            BookingDetails.bookingInfo["Passenger Age"])
        self.trainIdLabel.setText(parent.finalTrain["ID"])
        self.departureDateLabel.setText(parent.finalTrain["Departure Date"])
        self.departureTimeLabel.setText(parent.finalTrain["Departure Time"])
        self.departureCityLabel.setText(parent.finalTrain["Departure City"])
        self.destinationCityLabel.setText(
            parent.finalTrain["Destination City"])
        self.arrivalDateLabel.setText(parent.finalTrain["Departure Date"])
        self.arrivalTimeLabel.setText(parent.finalTrain["Arrival Time"])
        self.seatberthLabel.setText(
            BookingDetails.bookingInfo["Booking Preference"])
        self.seatberthLabel_2.setText(
            BookingDetails.bookingInfo["Booking Preference"]+" no.")

        self.WnidowOrAisleLabel.setText(
            BookingDetails.bookingInfo["Seat Preference"])
        self.seatberthNumber.setText(
            BookingDetails.bookingInfo["seat/berthNumber"])
        self.fareLabel.setText(BookingDetails.bookingInfo["Fare"])

        self.backToBookingButton.clicked.connect(self.back_to_BookingDetails)
        self.SaveBookingDetailsButton.clicked.connect(
            self.savingPassengerDetails)

    def savingPassengerDetails(self):
        self.listOfPassengerBookingDetails.clear()
        self.listOfPassengerBookingDetails.append(self.cnicLabel.text())
        id = self.cnicLabel.text()
        self.listOfPassengerBookingDetails.append(self.trainIdLabel.text())
        self.listOfPassengerBookingDetails.append(self.BookingIdLabel.text())
        b_id = self.BookingIdLabel.text()

        self.listOfPassengerBookingDetails.append(
            (self.nameLabel.text()).capitalize())
        name = self.nameLabel.text().capitalize()
        self.listOfPassengerBookingDetails.append(
            self.passengerAgeLabel.text())
        age = self.passengerAgeLabel.text()
        self.listOfPassengerBookingDetails.append(
            self.departureDateLabel.text())
        self.listOfPassengerBookingDetails.append(
            self.departureTimeLabel.text())
        self.listOfPassengerBookingDetails.append(
            self.departureCityLabel.text().capitalize())
        self.listOfPassengerBookingDetails.append(
            self.destinationCityLabel.text().capitalize())
        self.listOfPassengerBookingDetails.append(self.arrivalDateLabel.text())
        self.listOfPassengerBookingDetails.append(self.arrivalTimeLabel.text())
        self.listOfPassengerBookingDetails.append(
            self.seatberthLabel.text().capitalize())
        self.listOfPassengerBookingDetails.append(
            self.WnidowOrAisleLabel.text().capitalize())
        self.listOfPassengerBookingDetails.append(self.seatberthNumber.text())
        self.listOfPassengerBookingDetails.append(self.fareLabel.text())
        self.passengerBookingDetails = tuple(
            self.listOfPassengerBookingDetails)
        self.list1 = [self.passengerBookingDetails]

        if self.currentBooking:
            update_booking = '''
            INSERT INTO booking (passenger_id, train_id, booking_id, passenger_name, passenger_age, departure_date, departure_time, departure_city, destination_city, arrival_date, arrival_time, seat_preference, window_aisle, seat_no, fare)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            '''
            delete_booking = f'''
            DELETE FROM booking 
            WHERE passenger_id = {id} AND booking_id = {b_id};
            '''
            execute_query(connection, delete_booking)
            execute_list_query(connection, update_booking, self.list1)

        else:
            q1 = '''
            SELECT user_id FROM user;
            '''
            users_in_db = []
            passenger_id = read_query(connection, q1)
            print(passenger_id)
            print(id)
            for ids in passenger_id:
                users_in_db.append(ids[0])
            print(users_in_db)
            if id not in users_in_db:
                add_data_in_user = '''
                INSERT INTO user (user_id, user_name, age)
                VALUES (%s, %s, %s)
                '''
                val = [(id, name, age)]
                execute_list_query(connection, add_data_in_user, val)
            add_data_in_booking = '''
            INSERT INTO booking (passenger_id, train_id, booking_id, passenger_name, passenger_age, departure_date, departure_time, departure_city, destination_city, arrival_date, arrival_time, seat_preference, window_aisle, seat_no, fare)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            execute_list_query(connection, add_data_in_booking, self.list1)

        self.on_click_saving_button()

    def on_click_saving_button(self):
        global currentBooking
        currentBooking = self.passengerBookingDetails
        self.new = ClosingWindow(self)
        self.new.show()
        self.parent.close()
        self.parent.parent.close()

    def back_to_BookingDetails(self):
        self.close()


class ClosingWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi("ClosingWindow.ui", self)
        self.setWindowTitle("Closing Windows")
        self.parent = parent

        self.ExitButton.clicked.connect(self.exit_allWindows)

    def exit_allWindows(self):
        self.parent.close()
        self.close()


class CnicForUpdate(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi("CnicForUpdate.ui", self)
        self.setWindowTitle("Cnic For Update")
        self.parent = parent

        self.OpenBookingButton.clicked.connect(self.on_click_OpenBooking)
        self.BackButton.clicked.connect(self.on_clickBackButton)
        self.OpenBookingButton.setEnabled(False)
        self.CnicUpdateLinedit.textChanged.connect(self.enabling_button)

    def enabling_button(self):
        if self.CnicUpdateLinedit.text():
            self.OpenBookingButton.setEnabled(True)
        else:
            self.OpenBookingButton.setEnabled(False)

    def on_clickBackButton(self):
        self.close()

    def on_click_OpenBooking(self):
        cnic = self.CnicUpdateLinedit.text()

        from_booking_table = f'''
            SELECT * FROM booking
            WHERE passenger_id = {cnic};
        '''

        data_of_booking = read_query(connection, from_booking_table)

        global list_of_tickets_of_signed_users

        list_of_tickets_of_signed_users = []

        for result in data_of_booking:
            tickets_of_signed_users = {"Passenger Id": result[0], "Train Id": result[1],
                                       "Booking Id": result[2],
                                       "Passenger Name": result[3].capitalize(),
                                       "Passenger Age": result[4], "Departure Date": result[5], "Departure Time": result[6],
                                       "Departure City": result[7].capitalize(),
                                       "Destination City": result[8].capitalize(), "Arrival Date": result[9], "Arrival Time": result[10],
                                       "Seat Preference": result[11].capitalize(),
                                       "Window/aisle": result[12], "Seat No": result[13],
                                       "Fare": result[14]}
            list_of_tickets_of_signed_users.append(tickets_of_signed_users)

        print(list_of_tickets_of_signed_users)

        if list_of_tickets_of_signed_users:
            self.new = PreviousBookings(self)
            self.new.show()
            self.close()
        else:
            self.new = NoBooking(self)
            self.new.show()


class NoBooking(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi("NoBooking.ui", self)
        self.setWindowTitle("No Booking")
        self.parent = parent

        self.BackButton.clicked.connect(self.on_clickBackButton)

    def on_clickBackButton(self):
        self.close()


class PreviousBookings(QtWidgets.QWidget):
    cancellingBookingID = ''

    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi("PreviousBookings.ui", self)
        self.setWindowTitle("My Previous Bookings")
        self.parent = parent
        self.UpdateButton.clicked.connect(self.on_click_updateButton)
        self.CancelButton.clicked.connect(self.on_click_cancelButton)
        self.BookingIdlineEdit.setHidden(True)
        self.UpdateBookingButton.setHidden(True)
        self.CancelBookingButton.setHidden(True)
        self.UpdateBookingButton.clicked.connect(
            self.on_clickUpdateBookingButton)
        self.CancelBookingButton.clicked.connect(
            self.on_clickCancelBookingButton)
        self.Back_button.clicked.connect(self.on_click_back_button)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)

        for userdata in list_of_tickets_of_signed_users:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(
                rowPosition, 0, QTableWidgetItem(str(userdata["Booking Id"])))
            self.tableWidget.setItem(
                rowPosition, 1, QTableWidgetItem(userdata["Passenger Name"]))
            self.tableWidget.setItem(
                rowPosition, 2, QTableWidgetItem(userdata["Departure Date"]))
            self.tableWidget.setItem(
                rowPosition, 3, QTableWidgetItem(userdata["Departure City"]))
            self.tableWidget.setItem(
                rowPosition, 4, QTableWidgetItem(userdata["Destination City"]))
            self.tableWidget.setItem(
                rowPosition, 5, QTableWidgetItem(userdata["Seat Preference"]))
            # self.tableWidget.setItem(rowPosition, 6, QTableWidgetItem(userdata["Seat No"]))
            self.tableWidget.setItem(
                rowPosition, 6, QTableWidgetItem(str(userdata["Fare"])))

    def on_click_updateButton(self):
        self.AskBookingIdLabel.setText(
            "Enter Booking ID for updating that booking ")
        self.BookingIdlineEdit.show()
        self.UpdateBookingButton.show()
        self.CancelBookingButton.setHidden(True)

    def on_click_cancelButton(self):
        self.AskBookingIdLabel.setText(
            "Enter Booking ID for cancelling that booking ")
        self.BookingIdlineEdit.show()
        self.CancelBookingButton.show()
        self.UpdateBookingButton.setHidden(True)

    def on_clickUpdateBookingButton(self):
        for booking in list_of_tickets_of_signed_users:
            if self.BookingIdlineEdit.text() == str(booking["Booking Id"]):
                # print("Available")
                self.open_bookingdetails()
                break
        else:
            msg = QMessageBox()
            msg.setText("Please enter correct booking ID.")
            msg.setWindowTitle("Incorrect ID")
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.exec_()

    def on_clickCancelBookingButton(self):
        self.cancellingBookingID = self.BookingIdlineEdit.text()
        for booking in list_of_tickets_of_signed_users:
            if self.BookingIdlineEdit.text() == str(booking["Booking Id"]):
                booking_id = str(booking["Booking Id"])
                delete_booking = f'''
                DELETE FROM booking
                WHERE booking_id = {booking_id};
                '''
                execute_query(connection, delete_booking)
                self.new = CancelledBookings(self)
                self.new.show()
                break
        else:
            msg = QMessageBox()
            msg.setText("Please enter correct booking ID.")
            msg.setWindowTitle("Incorrect ID")
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.exec_()

    def on_click_back_button(self):
        self.close()

    def open_bookingdetails(self):
        id = self.BookingIdlineEdit.text()
        for booking in list_of_tickets_of_signed_users:
            if id == str(booking["Booking Id"]):
                self.new = PersonalInformation(self, booking)
                self.new.show()
                break
        else:
            msg = QMessageBox()
            msg.setText("Please enter correct booking ID.")
            msg.setWindowTitle("Incorrect ID")
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.exec_()


class CancelledBookings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi("CancelledBookings.ui", self)
        self.setWindowTitle("Booking Cancel")
        self.parent = parent
        self.ExitButton.clicked.connect(self.Exit_button_function)

        id = self.parent.cancellingBookingID

        for booking in list_of_tickets_of_signed_users:
            if id == str(booking["Booking Id"]):
                name = booking["Passenger Name"]
                CNIC = booking["Passenger Id"]
                fare = booking["Fare"]
                half_fare = booking["Fare"]*0.5
                break

        self.ShowCancelDetailsLabel.setText(
            f"Booking ID {id} on the name of {name} and \nCNIC {CNIC} has been Cancelled")
        self.totalFare.setText(str(f"{fare}"))
        self.RefundLabel.setText(str(f"{half_fare}"))

    def Exit_button_function(self):
        self.close()
        self.parent.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
