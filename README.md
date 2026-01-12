# Medify

Medify
A Python-based medication reminder calendar application built with Pygame. Medify helps users track and manage their medication schedules through an intuitive visual calendar interface.

Overview
Medify is a desktop calendar application designed to help users remember when to take their medications. The application provides a clean, interactive calendar interface where users can add, view, and manage medication reminders for specific dates.

Features
Interactive Calendar View: Navigate through months with an intuitive calendar grid
Day/Month Toggle: Switch between monthly calendar view and detailed daily view
Medication Notes: Add medication reminders and notes for specific dates
Easy Navigation: Quick access buttons for today, previous month, and next month
Data Persistence: Medication reminders are saved to a local file for future reference
Clean UI: Simple, user-friendly interface built with custom Pygame widgets
Technologies Used
Python: Core programming language
Pygame: Graphics and UI framework
File I/O: Local data storage for medication reminders
Installation
Prerequisites
Python 3.x
Pygame
Setup
Clone the repository:
bash
git clone https://github.com/wytruong/Medify.git
cd Medify
Install required dependencies:
bash
pip install pygame
Run the application:
bash
python main.py
Usage
Navigating the Calendar
Month View: Click the "month" button to view the full monthly calendar
Day View: Click the "day" button or select a date to view daily medication notes
Navigation Controls:
< button: Go to previous month
> button: Go to next month
Today button: Return to current date
Adding Medication Reminders
Select a date from the calendar
Click the "Add Note" button in the day view
Type your medication reminder
The reminder will be automatically saved
Managing Reminders
View all reminders for a specific date by clicking on that date
Delete reminders using the delete button in the day view
All data is stored in data.txt for persistence
Project Structure
Medify/
├── main.py              # Main application entry point
├── calendarManager.py   # Calendar management logic
├── calendarTable.py     # Calendar grid implementation
├── dayNote.py          # Daily medication notes interface
├── widget.py           # Base widget class
├── textview.py         # Text display widget
├── button.py           # Button widget
├── setting.py          # Configuration and constants
└── data.txt            # Persistent data storage
Key Components
CalendarManager: Manages the overall calendar interface and user interactions
CalendarTable: Renders the monthly calendar grid
DayNote: Handles medication note creation and display
Widget System: Custom UI component framework built on Pygame
Data Storage
Medication reminders are stored in data.txt using a simple format:

Format: Date///Note|||Date///Note|||...
Example: January 15, 2026///Take morning medication|||January 16, 2026///Doctor appointment|||
Future Enhancements
Notification system for medication reminders
Recurring medication schedules
Multiple medication tracking per day
Export/import functionality
Mobile version
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is open source and available under the MIT License.

Author
My Truong

GitHub: @wytruong
Email: truonguyenhoangmy@gmail.com
Acknowledgments
Built as a personal project to explore Pygame and create a practical medication management tool.

