# Import necessary modules
import re
import hashlib
import secrets

# Define a PasswordManager class to manage user passwords and enforce password policies
class PasswordManager:
    # Constructor to initialize the PasswordManager with a file path (default is "passwords.txt")
    def __init__(self, file_path="passwords.txt"):
        self.file_path = file_path
        # Load existing password records from the specified file
        self.records = self.load_records()

    # Method to load password records from a file, returning an empty list if the file is not found
    def load_records(self):
        try:
            with open(self.file_path, "r") as file:
                # Read lines from the file and convert each line (dictionary) using eval
                lines = file.readlines()
                return [eval(line) for line in lines]
        except FileNotFoundError:
            return []

    # Method to save password records to the specified file
    def save_records(self):
        with open(self.file_path, "w") as file:
            # Write each password record as a string to the file
            for record in self.records:
                file.write(str(record) + "\n")

    # Method to add a new password record to the manager
    def add_password(self, username, permissions):
        while True:
            password = input("Enter a password: ")
            # Check the password against the proactive password checker
            password_policy_result = self.check_password_policy(password, username)
            if password_policy_result == "Password meets the specified policy.":
                break
            else:
                print(password_policy_result)

        # Generate a random salt value using the secrets module
        salt = secrets.randbits(128)
        # Combine the salt and password, then hash the result using SHA-256
        salted_password = str(salt) + password
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
        # Create a dictionary representing the new password record
        record = {
            "username": username,
            "permissions": permissions,
            "salt": salt,
            "hashed_password": hashed_password
        }
        # Add the new record to the list of records and save the updated records to the file
        self.records.append(record)
        self.save_records()
        # Display a message indicating that the record has been added
        print("Record added to the password file.")

    # Method to display all stored password records
    def retrieve_passwords(self):
        print("The available password records are:")
        for record in self.records:
            print(f"{record['username']}, {record['permissions']}, {record['salt']}, {record['hashed_password']}")

    # Method to check if a password meets specified complexity requirements
    def check_password_policy(self, password, user_id):

        if len(password) < 8 or len(password) > 12:
            return "Password must be between 8 and 12 characters."

        if not self.meets_complexity_requirements(password):
            return "Password must include at least one upper-case letter, one lower-case letter, one numerical digit, and one special character."

        if self.is_weak_password(password):
            return "Common weak passwords are not allowed."

        if self.is_common_number(password):
            return "Passwords matching common numbers are not allowed."

        if password == user_id:
            return "Password must not match the user ID."

        return "Password meets the specified policy."

    # Method to check if a password meets specified complexity requirements
    def meets_complexity_requirements(self, password):
        return all(condition(password) for condition in [
            lambda x: any(c.isupper() for c in x),
            lambda x: any(c.islower() for c in x),
            lambda x: any(c.isdigit() for c in x),
            lambda x: any(c in '!@#$%?*' for c in x)
        ])

    # Method to check if a password is in a list of common weak passwords
    def is_weak_password(self, password):
        weak_passwords = ['password1', 'qwerty123', '12345678', '987654321']
        return password.lower() in weak_passwords

    # Method to check if a password matches a common number pattern
    def is_common_number(self, password):
        return bool(re.match(r'\d{8}', password))

# Main function to execute the password manager program
def main():
    print("Finvest Holdings Password File System")
    # Create an instance of the PasswordManager class
    password_manager = PasswordManager()

    # Main loop to interact with the user until they choose to exit
    while True:
        print("Please choose one of the following operations:")
        print("Type A to add a new record.\nType R to retrieve stored records.\nType E to exit")

        # Prompt the user for their choice
        choice = input("Type: ")

        # Check the user's choice and perform the corresponding operation
        if choice == "A":
            print("Adding a record")
            # Prompt the user for username, permissions, and password, then add a new record
            username = input("Username: ")
            print("Client, Premium Client, Financial Advisor, Financial Planner, Investment Analyst, Technical Support, Teller, Compliance Officer")
            permissions = input("Choose one of the above permissions: ")
            password_manager.add_password(username, permissions)

        elif choice == "R":
            # Display all stored password records
            password_manager.retrieve_passwords()

        elif choice == "E":
            # Exit the program
            print("Exiting the program.")
            break

        else:
            # Display an error message for invalid input
            print("Invalid input. Please try again.")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
