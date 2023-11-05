import sheets
import mailing
import time
import re

def main_function():
    config_sheet = 'config_sheet'
    src_sheet = 'src_sheet'
    sheet_url = 'https://docs.google.com/spreadsheets/d/1v6I0vzFhXfGZCOlQYm7C-TVaw8OnmkGKwSRGzESyUqw/edit?usp=sharing'
    contacts = sheets.get_contacts(config_sheet,src_sheet,sheet_url)
    # print(contacts)
    count = sheets.get_contact_row(contacts[0],config_sheet,src_sheet,sheet_url)
    # count = 335
    for contact in contacts:
        if contact != {}:
            print(contact)
            contact_row = count
            print(contact_row)
            emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", contact['email id'])
            for email in emails:
                contact['email id'] =  email
                mailing.send_mail(name='default name',to_email=contact['email id'],fromEmail='connect.edcnitd@gmail.com',subject="Invitation to Quiz-a-preneur at E-Summit 2023 by Entrepreneurship Development Cell, NIT Durgapur.")
                print('mail sent to '+contact['email id'])
                if len(emails) > 1:
                    print("sleep 4 seconds")
                    time.sleep(4)
            sheets.mail_success(config_sheet,src_sheet,sheet_url,contact_row)
            print("sheet updated")
            print("sleep 2.5 seconds")
            time.sleep(2.5)
        count+=1

main_function()