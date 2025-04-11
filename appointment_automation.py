from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import json, csv, time


def save_report(report):
    # Save as JSON
    with open("appointment_report.json", "w") as f:
        json.dump(report, f, indent=4)

    # Save as CSV
    with open("appointment_report.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Field", "Value"])
        for key, value in report.items():
            writer.writerow([key, value])

    print("Report saved as JSON and CSV")


def wait_and_find(by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))


# === Main Automation ===
driver = webdriver.Chrome()
driver.maximize_window()

try:
    print("Opening login page...")
    driver.get("https://katalon-demo-cura.herokuapp.com")

    # Click "Make Appointment"
    wait_and_find(By.ID, "btn-make-appointment").click()

    # Login
    wait_and_find(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()

    print("Filling out appointment form...")

    # Wait until the appointment form loads
    wait_and_find(By.ID, "appointment")

    # Fill the form
    Select(driver.find_element(By.ID, "combo_facility")).select_by_visible_text("Seoul CURA Healthcare Center")
    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.ID, "radio_program_medicaid").click()
    driver.find_element(By.ID, "txt_visit_date").send_keys("04/20/2025")
    driver.find_element(By.ID, "txt_comment").send_keys("Looking forward to this appointment.")
    driver.find_element(By.ID, "btn-book-appointment").click()

    # Confirm page loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "summary")))

    print("Appointment booked successfully!")

    # Build report
    report = {
        "Facility": "Seoul CURA Healthcare Center",
        "Readmission": "Yes",
        "Healthcare Program": "Medicaid",
        "Visit Date": "04/20/2025",
        "Comment": "Looking forward to this appointment.",
        "Status": "Appointment Booked Successfully"
    }

    # Show and save report
    print("\n=== Appointment Report ===")
    for key, value in report.items():
        print(f"{key}: {value}")
    save_report(report)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")
