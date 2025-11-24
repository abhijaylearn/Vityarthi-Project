# Vityarthi-Project

A simple console-based Hotel Management System written in Python that uses MySQL to store rooms, customers, and bookings. The script provides basic operations such as adding rooms, registering customers, booking rooms, and viewing available rooms and bookings.

This repository contains a minimal example using the mysql-connector-python driver and demonstrates how to interact with a MySQL database using parameterized queries.

---

## Features

- Add room (room number, type, price)
- Register customer (name, phone, email)
- Book a room for a customer (check-in / check-out)
- View available rooms
- View bookings with joined room and customer info

---

## Prerequisites

- Python 3.8+
- MySQL server
- pip

Required Python package:
- mysql-connector-python

Install the requirement:
```bash
pip install mysql-connector-python
```

---

## Database setup

Create the database and required tables in your MySQL server. Example SQL:

```sql
CREATE DATABASE IF NOT EXISTS hotel_management;
USE hotel_management;

CREATE TABLE IF NOT EXISTS rooms (
  room_id INT AUTO_INCREMENT PRIMARY KEY,
  room_number VARCHAR(50) NOT NULL,
  room_type VARCHAR(50),
  price DECIMAL(10,2),
  status VARCHAR(20) DEFAULT 'Available'
);

CREATE TABLE IF NOT EXISTS customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  phone VARCHAR(30),
  email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS bookings (
  booking_id INT AUTO_INCREMENT PRIMARY KEY,
  room_id INT NOT NULL,
  customer_id INT NOT NULL,
  check_in DATE NOT NULL,
  check_out DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (room_id) REFERENCES rooms(room_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

---

## Configuration

The example script connects with hard-coded connection parameters:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abc123",
    database="hotel_management"
)
```

For production or shared environments, do NOT hard-code credentials. Use environment variables or a configuration file. Example (using environment variables):

```python
import os
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    passwd=os.getenv("DB_PASS", ""),
    database=os.getenv("DB_NAME", "hotel_management")
)
```

Set environment variables before running:
```bash
export DB_HOST=localhost
export DB_USER=root
export DB_PASS=yourpassword
export DB_NAME=hotel_management
```

---

## Running the script

1. Save the provided Python code into a file, e.g. `hotel.py`.
2. Ensure the database is created and tables exist (see Database setup).
3. Install dependencies: `pip install mysql-connector-python`
4. Run the script:
```bash
python hotel.py
```

You will see an interactive menu:

1. Add Room
2. Add Customer
3. Book Room
4. View Available Rooms
5. View Bookings
6. Exit

Follow the prompts to perform operations.

---

## Example usage

- Add Room:
  - Room Number: 101
  - Room Type: Deluxe
  - Price: 1200.00

- Add Customer:
  - Customer Name: John Doe
  - Phone: 1234567890
  - Email: john@example.com

- Book Room:
  - Room ID: 1
  - Customer ID: 1
  - Check-In Date (YYYY-MM-DD): 2025-12-01
  - Check-Out Date (YYYY-MM-DD): 2025-12-05

- View Available Rooms
- View Bookings

---

## Security & Notes

- Never store database passwords directly in source code for real projects.
- Use parameterized queries (the example uses them) to avoid SQL injection.
- Add input validation and date parsing in production code.
- Add error handling around DB operations to handle connection failures and query errors gracefully.
- Consider using an ORM (like SQLAlchemy) for more advanced projects.

---

## Possible Improvements

- Add room search and filtering (by price, type).
- Add cancellation and booking status.
- Add user authentication for staff.
- Add a web UI (Flask, FastAPI) instead of a console UI.
- Add unit tests and CI.

---

## Contributing

If you'd like to contribute, please:
- Fork the repository
- Create a branch for your feature or bugfix
- Open a pull request with a clear description of changes

---

## License

This project is provided as-is. Add a license file (e.g., MIT) if you want to specify reuse terms.
