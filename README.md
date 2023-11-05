# Setting up Sheet Mailer
1. Create a service account and download the credentials into a service_account.json file
2. Create a config worksheet in your google sheets with two columns, field and column respectively
3. Add a 'status','email' field to all records to show status of mailing and store emails
4. Modify settings in the main.py file like password etc and start mailing