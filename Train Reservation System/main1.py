import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
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


connection = create_db_connection("localhost", "root", "1212", "train")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


from_booking_table = '''
SELECT * FROM booking
WHERE passenger_id = "369797";
'''
data_of_booking = read_query(connection, from_booking_table)
list_of_tickets_of_signed_users = []
for result in data_of_booking:
    tickets_of_signed_users = {"Passenger Id": result[0], "Train Id": result[1],
                               "Passenger Name": result[2].capitalize(),
                               "Passenger Age": result[3], "Departure City": result[4].capitalize(),
                               "Destination City": result[5].capitalize(),
                               "Seat Preference": result[6].capitalize(),
                               "Window/aisle": result[7], "Fare": result[8]}
    list_of_tickets_of_signed_users.append(tickets_of_signed_users)
print(list_of_tickets_of_signed_users)
# We will just fetch the data in the list and present it to the user as below


def execute_list_query(connection, query, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, val)
        connection.commit()
        print("Query Successful")
    except Error as err:
        print(f"Error: '{err}'")

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


currentBooking = []


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
        self.new = PersonalInformation(self, currentBooking)
        self.new.show()


class PersonalInformation(QtWidgets.QWidget):
    personalInfo = {}
    currentBooking = []

    def __init__(self, parent, currentBooking = []):
        super().__init__()
        uic.loadUi("PersonalInformation.ui", self)
        self.setWindowTitle("Personal Information")
        self.parent = parent
        self.currentBooking = currentBooking

        self.BookingButton.clicked.connect(self.ClickBookingButton)
        self.BackToMainButton.clicked.connect(self.back_to_MainWindow)

        if self.currentBooking:
            self.name.setText(self.personalInfo["Name"])
            self.cnic.setText(self.personalInfo["CNIC"])

            date_str = self.personalInfo["Date of Birth"]
            qdate = QtCore.QDate.fromString(date_str, "dd/MM/yyyy")
            self.dateOfBirth.setDate(qdate)

    def back_to_MainWindow(self):
        self.close()

    def ClickBookingButton(self):
        self.personalInfo["Name"] = self.name.text()
        self.personalInfo["CNIC"] = self.cnic.text()
        self.personalInfo["Date of Birth"] = self.dateOfBirth.text()


        self.new = BookingDetails(self, self.currentBooking)
        self.new.show()



class BookingDetails(QtWidgets.QWidget):
    departuringTrains = []
    arrivingTrains = []
    occupiedSeats=[]
    availableSeats=[]
    availableseatNumbers=[]
    finalTrain = {}
    bookingInfo = {}

    def __init__(self, parent, currentBooking):
        super().__init__()
        uic.loadUi("BookingDetails.ui", self)
        self.setWindowTitle("Booking Details")
        self.parent = parent

        dateList = []
        for dates in range(15):
            dateList.append(str(datetime.date.today() + datetime.timedelta(days=dates)))




        self.dateComboBox.addItems(dateList)

        self.departureCityComboBox.currentTextChanged.connect(self.on_selectDepartureCity)
        self.destinationCityComboBox.currentTextChanged.connect(self.on_selectDestinationCity)
        self.timeComboBox.currentTextChanged.connect(self.on_selectDepartureTime)
        self.ageLine.textChanged.connect(self.on_selectAge)
        self.seatPreferencecomboBox.currentTextChanged.connect(self.show_seatOrberthLabel)
        self.seatPreferencecomboBox.currentTextChanged.connect(self.showing_seatorberthforFare)
        self.seatPreferencecomboBox.currentTextChanged.connect(self.on_selectAge)
        self.BackToPersonInfoButton.clicked.connect(self.back_to_personalInfoWindow)

        self.submitButton.clicked.connect(self.on_submitBookingDetails)

        if currentBooking:
            self.dateComboBox.setCurrentText(currentBooking[4])
            self.departureCityComboBox.setCurrentText(currentBooking[6])
            self.destinationCityComboBox.setCurrentText(currentBooking[7])
            self.timeComboBox.setCurrentText(currentBooking[5])
            self.arrivalDateLabel.setText(currentBooking[8])
            self.arrivalTimeLabel.setText(currentBooking[9])
            self.seatPreferencecomboBox.setCurrentText(currentBooking[10])
            self.seatBerthNumbercomboBox.setCurrentText(currentBooking[11])
            self.ageLine.setText(currentBooking[2])

    def on_selectDepartureCity(self):
        self.destinationCityComboBox.clear()
        self.departuringTrains = []

        for train in trains:
            if self.departureCityComboBox.currentText() == train["Departure City"]:
                self.departuringTrains.append(train)

        destinationCities = [train["Destination City"] for train in self.departuringTrains]
        self.destinationCityComboBox.addItems(destinationCities)

    def on_selectDestinationCity(self):
        self.timeComboBox.clear()
        self.arrivingTrains = []

        for train in self.departuringTrains:
            if self.destinationCityComboBox.currentText() == train["Destination City"]:
                self.arrivingTrains.append(train)

        departureTimes = [train["Departure Time"] for train in self.arrivingTrains]
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
        self.seatOrberthLabel.setText(self.seatPreferencecomboBox.currentText() + " no.")
        self.seat_berthNumbers()

    def seat_berthNumbers(self):
        for number in range(50):
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


    def on_selectAge(self):
        if self.finalTrain and self.ageLine.text() and self.seatBerthNumbercomboBox.currentText():
            if self.seatPreferencecomboBox.currentText() == "Seat":
                fare = self.finalTrain["Seat Fare"]
                self.bookingInfo["Booking Preference"] = "Seat"
            elif self.seatPreferencecomboBox.currentText() == "Berth":
                fare = self.finalTrain["Berth Fare"]
                self.bookingInfo["Booking Preference"] = "Berth"

            age = int(self.ageLine.text())
            self.bookingInfo["Passenger Age"]=str(age)

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

        personalInfo = self.parent.personalInfo
        bookingInfo = self.finalTrain

        try:

            pass
        except:
            # Error Modal
            # self.new = ErrorModal()
            # self.new.show()

            self.new = UnsuccessfulBookings(self)
            self.new.show()
            pass
        else:
            self.new = SuccessfulBooking(self)
            self.new.show()
            # Success Modal
            pass


class UnsuccessfulBookings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi("UnsuccessfulBooking.ui", self)
        self.setWindowTitle("Booking Unsuccessful")
        self.parent = parent


class SuccessfulBooking(QtWidgets.QWidget):
    listOfPassengerBookingDetails = []

    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi("SuccessfulBooking.ui", self)
        self.setWindowTitle("Booking Successful")
        self.parent = parent

        self.nameLabel.setText(PersonalInformation.personalInfo["Name"])
        self.cnicLabel.setText(PersonalInformation.personalInfo["CNIC"])
        self.passengerAgeLabel.setText(BookingDetails.bookingInfo["Passenger Age"])
        self.trainIdLabel.setText(parent.finalTrain["ID"])
        self.departureDateLabel.setText(parent.finalTrain["Departure Date"])
        self.departureTimeLabel.setText(parent.finalTrain["Departure Time"])
        self.departureCityLabel.setText(parent.finalTrain["Departure City"])
        self.destinationCityLabel.setText(parent.finalTrain["Destination City"])
        self.arrivalDateLabel.setText(parent.finalTrain["Departure Date"])
        self.arrivalTimeLabel.setText(parent.finalTrain["Arrival Time"])
        self.seatberthLabel.setText(BookingDetails.bookingInfo["Booking Preference"])
        self.seatberthLabel_2.setText(BookingDetails.bookingInfo["Booking Preference"]+" no.")
        self.seatberthNumber.setText(BookingDetails.bookingInfo["seat/berthNumber"])
        self.fareLabel.setText(BookingDetails.bookingInfo["Fare"])

        self.backToBookingButton.clicked.connect(self.back_to_BookingDetails)
        self.SaveBookingDetailsButton.clicked.connect(self.savingPassengerDetails)

    def savingPassengerDetails(self):
        self.listOfPassengerBookingDetails.clear()
        self.listOfPassengerBookingDetails.append(self.cnicLabel.text())
        self.listOfPassengerBookingDetails.append(self.trainIdLabel.text())
        self.listOfPassengerBookingDetails.append(self.BookingIdLabel.text())
        self.listOfPassengerBookingDetails.append((self.nameLabel.text()).capitalize())
        self.listOfPassengerBookingDetails.append(self.passengerAgeLabel.text())
        # self.listOfPassengerBookingDetails.append(self.departureDateLabel.text())
        # self.listOfPassengerBookingDetails.append(self.departureTimeLabel.text())
        self.listOfPassengerBookingDetails.append(self.departureCityLabel.text().capitalize())
        self.listOfPassengerBookingDetails.append(self.destinationCityLabel.text().capitalize())
        # self.listOfPassengerBookingDetails.append(self.arrivalDateLabel.text())
        # self.listOfPassengerBookingDetails.append(self.arrivalTimeLabel.text())
        self.listOfPassengerBookingDetails.append(self.seatberthLabel.text().capitalize())
        self.listOfPassengerBookingDetails.append(self.WnidowOrAisleLabel.text().capitalize())
        self.listOfPassengerBookingDetails.append(self.seatberthNumber.text())
        self.listOfPassengerBookingDetails.append(self.fareLabel.text())
        self.passengerBookingDetails = tuple(self.listOfPassengerBookingDetails)
        self.list1 = [self.passengerBookingDetails]

        add_data_in_booking = '''
        INSERT INTO booking (passenger_id, train_id, booking_id, passenger_name, passenger_age, departure_city, destination_city, seat_preference, window_aisle, seat_no, fare)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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

        # self.BacktoReceipt.clicked.connect(self.back_to_BookingReceipt)
        self.ExitButton.clicked.connect(self.exit_allWindows)

    # def back_to_BookingReceipt(self):
    # self.close()

    def exit_allWindows(self):
        self.parent.close()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

