import smtplib

my_email = "saddad0618@gmail.com"
password = "foqs qgdz fcjd mvul"


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=item_name_string
    )
