import mailbox
import csv
import re

def extract_emails_from_mbox(mbox_file, output_file):
    mbox = mailbox.mbox(mbox_file)
    email_set = set()

    # Regex to extract email addresses
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')

    for message in mbox:
        # Extract email addresses from 'From' field
        from_field = message['From']
        if from_field:
            emails = email_pattern.findall(from_field)
            email_set.update(emails)
        
        # Extract email addresses from 'To' field
        to_field = message['To']
        if to_field:
            emails = email_pattern.findall(to_field)
            email_set.update(emails)

    # Write extracted email addresses to a CSV file
    with open(output_file, mode='w', newline='') as csvfile:
        email_writer = csv.writer(csvfile)
        email_writer.writerow(['Email'])
        for email in email_set:
            email_writer.writerow([email])

# Example usage
extract_emails_from_mbox('2007-2009.mbox/mbox', 'emails.csv')
