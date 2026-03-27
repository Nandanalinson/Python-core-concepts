email_id = input('enter your email id : ')

print(f"valid" if email_id.endswith("gmail.com") and "@" in email_id else "not valid")