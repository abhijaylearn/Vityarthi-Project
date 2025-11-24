# Vityarthi Project — Statement

## Problem statement
Many small hotels, guest houses, and hostels manage room inventory, customer records, and bookings using manual logs, spreadsheets, or disconnected tools. This leads to:
- Double-bookings and scheduling conflicts
- Difficulty tracking room availability and rates
- Time-consuming customer registration and lookup
- Poor record-keeping and error-prone billing preparation

This project provides a simple, reliable hotel management CLI application that centralizes rooms, customers, and bookings in a database to reduce manual errors and speed up common operations.

## Scope of the project
In scope:
- Persistent storage using a relational database (MySQL)
- Command-line interface for managing rooms, customers, and bookings
- Basic operations: add rooms, register customers, create bookings, view available rooms, and list bookings
- Room status handling (Available / Booked)
- Basic input validation and user prompts

Out of scope (for the initial version):
- Web or mobile UI
- Payment processing and invoicing
- Multi-user concurrency controls or role-based access
- Advanced reporting, analytics, or integrations with external systems
- Automated email/SMS notifications

## Target users
- Small hotel, guest house, B&B, or hostel owners/operators
- Front-desk staff and receptionists who need a lightweight booking tool
- Students and developers learning database-backed Python applications
- Project maintainers who want a minimal starting point to extend features

## High-level features
- Room management
  - Add new rooms with room number, type, price, and status
  - View available rooms
- Customer management
  - Register new customers with name, phone, and email
  - Simple customer lookup by ID
- Booking management
  - Book rooms for registered customers with check-in and check-out dates
  - Update room status to 'Booked' on successful booking
  - List all bookings with room number, customer name, and dates
- Persistence and configuration
  - Stores data in MySQL (schema: rooms, customers, bookings)
  - Configuration via database connection variables
- Usability
  - Simple interactive CLI menu for common operations
  - Clear messages for success and errors

## Assumptions & constraints
- A MySQL server is available and configured; the application expects valid DB credentials.
- The initial design focuses on simplicity and learnability rather than production-scale features (authentication, concurrency, security hardening).
- Dates are handled as simple strings in YYYY-MM-DD format in the first version; validation can be improved in future iterations.

