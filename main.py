from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pickle
import time
import tkinter as tk
from tkinter import messagebox

EMAIL = ""
PASSWORD = ""
PHONE = ""
JOB_ID = ""
LOCATION = ""

def valid_inputs():
    global EMAIL, PASSWORD, PHONE, JOB_ID, LOCATION

    EMAIL = email_entry.get()
    PASSWORD = password_entry.get()
    PHONE = phone_entry.get()
    JOB_ID = job_id_entry.get() or ""
    LOCATION = location_entry.get() or ""

    if not EMAIL or not PASSWORD or not PHONE:
        messagebox.showerror("Error", "Email, Password and Phone number are mandatory fields!!")
        return False

    if "@" not in EMAIL or "." not in EMAIL:
        messagebox.showerror("Error", "Enter a valid email address!!")
        return False

    if not PHONE.isdigit() or len(PHONE) != 10:
        messagebox.showerror("Error", "Enter a valid phone number!!")
        return False

    return True

def abort_application(driver):
    try:
        close_btn = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_btn.click()
        time.sleep(1)

        discard_btn = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
        discard_btn.click()
        time.sleep(1)
        print("Application aborted")

        save_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_btn.click()
        print("Saving the job")
    except NoSuchElementException:
        print("No such element found!")

def check_addition_fields(driver):
    try:
        additional_fields = driver.find_elements(
            By.XPATH,
                      "//form//*[@aria-expanded='false']"
        )
        if additional_fields:
            return True
    except Exception as e:
        print(f"Error checking additional fields: {e}")
    return False


def start_application():
    if not valid_inputs():
        return
    global EMAIL, PASSWORD, PHONE, JOB_ID, LOCATION

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    driver.maximize_window()

    try:
        email_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        sign_in_btn = driver.find_element(By.CLASS_NAME, "btn__primary--large")

        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)
        sign_in_btn.click()

        input("Solve the CAPTCHA if needed and press Enter")

        cookies = driver.get_cookies()
        with open("linkedin_cookies.pkl", "wb") as cookie_file:
            pickle.dump(cookies, cookie_file)

        driver.get("https://www.linkedin.com")
        with open("linkedin_cookies.pkl", "rb") as cookie_file:
            cookies = pickle.load(cookie_file)
            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.get(f"https://www.linkedin.com/jobs/search/?keywords={JOB_ID}&location={LOCATION}")
        time.sleep(2)

        easy_apply_btn = driver.find_element(By.XPATH, "//button[text()='Easy Apply']")
        easy_apply_btn.click()

        listings = driver.find_elements(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul')

        for job in listings:
            job.click()
            time.sleep(2)

            try:
                # Job Page
                apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
                apply_btn.click()
                time.sleep(2)

                # Page - 1
                phone_num = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
                if phone_num.get_attribute('value') == "":
                    phone_num.send_keys(PHONE)

                next_btn_1 = driver.find_element(By.CLASS_NAME, "artdeco-button--2")
                next_btn_1.click()
                time.sleep(2)

                # Page - 2
                if check_addition_fields(driver):
                    abort_application(driver)
                    continue

                try:
                    review_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Review')]")
                    review_button.click()
                    time.sleep(2)
                except NoSuchElementException:
                    print("Job application more than 3 pages! Skipping.")
                    abort_application(driver)
                    continue

                # Page - 3
                submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit application')]")
                submit_btn.click()
                print("Application submitted successfully!")

            except NoSuchElementException:
                print("No application button, skipped.")
                continue

    except Exception as e:
        print(f"An error occurred during application: {e}")

# Tkinter GUI
root = tk.Tk()
root.title("LinkedIn Easy Apply Automation")

tk.Label(root, text="Email:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Phone (10 digits):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Job ID:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
job_id_entry = tk.Entry(root, width=30)
job_id_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Location:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
location_entry = tk.Entry(root, width=30)
location_entry.grid(row=4, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Start Application", command=start_application)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()


