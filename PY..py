import re

# Input and Output file names
input_file = "input.txt"
output_file = "emails.txt"

try:
    # Open and read the text file
    with open(input_file, "r") as file:
        content = file.read()

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Find email addresses
    emails = re.findall(email_pattern, content)

    
    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"Success! {len(emails)} email addresses extracted.")
    print(f"Saved to '{output_file}'")

except FileNotFoundError:
    print("Error: Input file not found.")
except Exception as e:
    print("An error occurred:", e)
