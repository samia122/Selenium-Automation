# Selenium Appointment Booking Automation

This Python project uses **Selenium WebDriver** to automate the process of booking an appointment on the demo site [CURA Healthcare Service](https://katalon-demo-cura.herokuapp.com). After booking the appointment, the script generates a report in both **JSON** and **CSV** formats.

## Features

- Automates login and form submission on the CURA appointment site
- Extracts appointment details after booking
- Generates and saves a report as:
  - `appointment_report.json`
  - `appointment_report.csv`
- Uses explicit waits to ensure reliable element interaction

---

## Requirements

- Python 3.7+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- The following Python packages:
  - `selenium`

Install dependencies using pip:

```bash
pip install selenium

**## Setup**
Install ChromeDriver
Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/ and make sure it’s in your system PATH.

Clone or download this repository

Run the script:

bash
Copy
Edit
python appointment_automation.py

**## Output**
Once the appointment is successfully booked, two files will be generated in the project directory:

appointment_report.json

appointment_report.csv

Both files contain a summary of the appointment details.

**## Script Overview**
URL: https://katalon-demo-cura.herokuapp.com

Login credentials:

Username: John Doe

Password: ThisIsNotAPassword

Facility: Seoul CURA Healthcare Center

Healthcare Program: Medicaid

Visit Date: 04/20/2025

Additional Options: Hospital readmission checked, comment added

**## Customization*
You can modify:

The date or comment in the script

The selected healthcare program or facility

Add more validations or export options

**## Files Included**
appointment_automation.py – Main automation script

appointment_report.json – Generated JSON report

appointment_report.csv – Generated CSV report

