def remove_duplicates(file1, file2, output_file):
    # Read the emails from both files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        emails1 = set(line.strip() for line in f1)
        emails2 = set(line.strip() for line in f2)

    # Remove duplicates from file2
    non_duplicates = emails2 - emails1

    # Write non-duplicate emails to the output file
    with open(output_file, 'w') as output:
        for email in non_duplicates:
            output.write(email + '\n')

    print("Duplicates removed and new file created successfully.")

# Usage example
file1 = 'emails2.txt'
file2 = 'unique_emails.txt'
output_file = 'output.txt'

remove_duplicates(file1, file2, output_file)
