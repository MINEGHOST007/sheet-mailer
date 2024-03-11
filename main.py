import sheets
import mailing
import time
import re

def main_function():
    config_sheet = 'config'
    src_sheet = 'SRC'
    sheet_url = 'https://docs.google.com/spreadsheets/d/1BJLMMgfHEC0VugZa3LqhLsFJwiT2y9ahaZKyA3IUQCQ/edit#gid=1507014642'
    contacts = sheets.get_contacts(config_sheet,src_sheet,sheet_url)
    print(contacts)
    count = 2
    for contact in contacts:
        if contact != {}:
            print(contact)
            contact_row = count
            print(contact_row)
            emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", contact['email'])
            for email in emails:
                contact['email'] =  email
                mailing.send_mail(name='default name',to_email=contact['email'],fromEmail='edc.nitdurgapur.official@gmail.com',subject="Invitation to Participate in Quiz-a-Preneur Event at E-Summit, NIT Durgapur")
                print('mail sent to '+contact['email'])
                if len(emails) > 1:
                    print("sleep 4 seconds")
                    time.sleep(4)
            sheets.mail_success(config_sheet,src_sheet,sheet_url,contact_row)
            print("sheet updated")
            print("sleep 2.5 seconds")
            time.sleep(2.5)
        count+=1

main_function()