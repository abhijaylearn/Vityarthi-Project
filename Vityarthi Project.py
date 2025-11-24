import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abc123",
    database="hotel_management"
)
cursor = db.cursor()

def add_room(number, rtype, price):
    sql = "INSERT INTO rooms (room_number, room_type, price) VALUES (%s, %s, %s)"
    cursor.execute(sql, (number, rtype, price))
    db.commit()
    print("Room added successfully!")


def add_customer(name, phone, email):
    sql = "INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, phone, email))
    db.commit()
    print("Customer registered successfully!")


def book_room(room_id, customer_id, check_in, check_out):
    cursor.execute("UPDATE rooms SET status='Booked' WHERE room_id=%s", (room_id,))
    sql = "INSERT INTO bookings (room_id, customer_id, check_in, check_out) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (room_id, customer_id, check_in, check_out))
    db.commit()
    print("Room booked successfully!")


def view_available_rooms():
    cursor.execute("SELECT * FROM rooms WHERE status='Available'")
    rooms = cursor.fetchall()
    print("\nAvailable Rooms:")
    for room in rooms:
        print(room)


def view_bookings():
    cursor.execute("""
        SELECT b.booking_id, r.room_number, c.name, b.check_in, b.check_out
        FROM bookings b
        JOIN rooms r ON b.room_id = r.room_id
        JOIN customers c ON b.customer_id = c.customer_id
    """)
    bookings = cursor.fetchall()

    print("\nBookings:")
    for b in bookings:
        print(b)


def main():
    while True:
        print("\n---- HOTEL MANAGEMENT SYSTEM ----")
        print("1. Add Room")
        print("2. Add Customer")
        print("3. Book Room")
        print("4. View Available Rooms")
        print("5. View Bookings")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            number = input("Room Number: ")
            rtype = input("Room Type: ")
            price = float(input("Price: "))
            add_room(number, rtype, price)

        elif choice == "2":
            name = input("Customer Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_customer(name, phone, email)

        elif choice == "3":
            room_id = int(input("Room ID: "))
            customer_id = int(input("Customer ID: "))
            check_in = input("Check-In Date (YYYY-MM-DD): ")
            check_out = input("Check-Out Date (YYYY-MM-DD): ")
            book_room(room_id, customer_id, check_in, check_out)

        elif choice == "4":
            view_available_rooms()

        elif choice == "5":
            view_bookings()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
