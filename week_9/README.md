IT Helpdesk Ticket Registration System

Purpose of the Application

This application was built for the IT Support team of City University Malaysia.
Every day, students report technical issues such as LMS login problems, WiFi
connection issues, printer malfunctions, and password reset requests. Before a
technician can investigate an issue, a helpdesk ticket must be created. This
program provides a simple, modular way to register a new ticket, assign it a
priority level, automatically route it to the correct technician, and display
a formatted ticket summary.

Tech Stack


Language: Python 3
Structure: Modular Python (separate files for logic and display)
Modules used: Only Python's built-in standard features (no external
libraries required)


Project Structure

week_9/
├── main.py      # Entry point, runs the program
├── ticket.py    # Handles ticket creation and technician assignment
├── display.py   # Handles formatting and printing the ticket
└── README.md    # Project documentation

How the Technician Assignment Works

Based on the priority level entered by the user, the ticket is automatically
assigned to the person in charge:

PriorityTechnicianHighAhmadMediumSitiLowAli

Every new ticket is created with a status of Pending.

How to Use


Make sure Python 3 is installed on your computer.
Open a terminal and navigate to the week_9 folder.
Run the program:


   python main.py


When prompted, enter the following details:

Student Name
Student ID
Issue
Location
Priority (High/Medium/Low)



The program will display a formatted helpdesk ticket, including the
automatically assigned technician and ticket status.


Example

=== IT Helpdesk Ticket ===
Student Name : izzad
Student ID : 12345678910
Issue : blue screen pc
Location : lab 101 level 1
Priority (High/Medium/Low): High

========== HELPDESK TICKET ==========
Student Name : izzad
Student ID   : 12345678910
Issue        : blue screen pc
Location     : lab 101 level 1
Priority     : High
Technician   : Ahmad
Status       : Pending
========================================

Demonstration

Record a short screen recording (video or GIF) showing the program being run
from start to finish, including entering ticket details and viewing the final
ticket summary, and attach it alongside this README.