from datetime import datetime
import random
import pandas as pd
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# Email credentials
my_email = os.getenv("EMAIL", "")
password = os.getenv("EMAIL_PASSWORD", "")

# Get today's date and month
today = datetime.now()
today_tuple = (today.day, today.month)

# Read birthday from the csv file
data = pd.read_csv("birthdays.csv")
data_dict = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in data.iterrows()}

# Check if someone has their birthday today
if today_tuple in data_dict:
    birthday_person = data_dict[today_tuple]

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    # Sending the email
    message = f"Subject:Happy Birthday!\n\n{content}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(my_email, password)
            conn.sendmail(
                from_addr = my_email,
                to_addrs= birthday_person["email"],
                msg = message
            )

        print("Email sent!")
    except Exception as e:
        print("Failed to send email:")
        print(e)