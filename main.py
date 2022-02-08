import pandas as pd
import smtplib
import openpyxl
 
my_email = "testing8065@gmail.com"

password = "12345678te"

df = pd.read_excel("./emails.xlsx")

print(df)
