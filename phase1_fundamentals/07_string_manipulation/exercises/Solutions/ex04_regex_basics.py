"""
Use re.findall/re.sub to extract emails or phone numbers from text.
"""
import re

data = """Company Contact Directory

If you have any questions, please contact our team.

Sales Department
Email: sales@techworld.com
Phone: +1-555-123-4567

Customer Support
Email: support.help@techworld.com
Phone: (555) 987-6543

Human Resources
Email: hr_team@techworld.com
Phone: 555-222-8899

Regional Manager
Name: Sarah Johnson
Email: sarah.johnson@techworld.com
Mobile: +1 555 444 7788

Engineering Team
Lead: David Lee
Email: david.lee@techworld.com
Phone: 5551234567

Intern Coordinator
Email: intern-office@techworld.com
Backup Email: interns2026@gmail.com
Emergency Contact: +1 (555) 888-9911

Please do not share these contact details outside the organization.
For urgent issues, email support.help@techworld.com or call +1-555-123-4567."""

def main():
    print(f"Original data: {data}")

    # Email Pattern:
    # [\w\.-]+      -> Match one or more letters, digits, '_', '.', or '-'
    # @             -> Match the '@' symbol
    # [\w\.-]+      -> Match one or more letters, digits, '_', '.', or '-'
    email_pattern = r"[\w\.-]+@[\w\.-]+"

    # Phone Number Pattern:
    # [\+\d\-\(\) ] -> Match '+', digits, '-', '(', ')', or spaces
    # {10,}         -> Match a sequence of at least 10 of the above characters
    phone_pattern = r"[\+\d\-\(\) ]{10,}"

    # Find all emails and phone numbers
    emails = re.findall(email_pattern, data)
    phones = re.findall(phone_pattern, data)

    print("Test for finding emails and phone numbers")
    print("-"*40)
    print("Emails Found:")
    print(emails)

    print("\nPhone Numbers Found:")
    print(phones)

    # Redact emails and phone numbers
    print("\nTest for redacting emails and phone numbers")
    print("-" * 40)
    redact_data = re.sub(email_pattern, "[REDACTED EMAIL]", data)
    redact_data = re.sub(phone_pattern, "[REDACTED PHONE]", redact_data)

    print(redact_data)


if __name__ == "__main__":
    main()
