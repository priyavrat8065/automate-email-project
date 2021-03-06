import pandas as pd
import smtplib
import openpyxl
from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv(Path.home()/"environment-variables"/"config.env.txt")
my_email = "testing8065@gmail.com"

password = os.getenv("password")

df = pd.read_excel("./emails.xlsx")

recipient_email_ids = df['email_id'].to_list()

for email_id in recipient_email_ids:
    print(f"Send email to {email_id}")
    email_subject = input("Type email Subject\n")
    email_header = input(f"Type email header. For ex Hello/Dear <name of the person>,\n")
    email_body = input(f"Type the email body\n")
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email_id, msg=f"Subject:{email_subject}\n\n"
                        f"{email_header}\n\n{email_body}\n\nFrom Priyavrat")

connection.close()




