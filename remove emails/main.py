def get_unique_emails(file1, file2, output_file):
    # Read emails from the first file
    with open(file1, 'r') as f1:
        emails1 = set(f1.read().lower().splitlines())

    # Read emails from the second file
    with open(file2, 'r') as f2:
        emails2 = set(f2.read().lower().splitlines())

    # Find the common emails in both files
    common_emails = emails1.intersection(emails2)

    # Remove the common emails from both sets
    unique_emails1 = emails1 - common_emails
    unique_emails2 = emails2 - common_emails

    # Remove emails containing "tomorri", "aol", and "wix"
    filter_words = ["tomorri", "aol", "wix", "imprint", "leadrouter"]
    unique_emails1 = set(email for email in unique_emails1 if not any(word in email for word in filter_words))
    unique_emails2 = set(email for email in unique_emails2 if not any(word in email for word in filter_words))

    # Write the unique emails to the output file
    with open(output_file, 'w') as output:
        for email in unique_emails1:
            output.write(email + '\n')
        for email in unique_emails2:
            output.write(email + '\n')

    print(f"Unique emails written to {output_file}.")


# Usage example
file1 = 'emails1.txt'
file2 = 'emails2.txt'
output_file = 'unique_emails.txt'

get_unique_emails(file1, file2, output_file)
