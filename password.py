# Import necessary modules
import hashlib
import secrets

# Define a PasswordManager class to manage user passwords
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
    def add_password(self, username, permissions, password):
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
        print("Record added to password file.")

    # Method to display all stored password records
    def retrieve_passwords(self):
        print("The available password records are:")
        # Display each password record's information
        for record in self.records:
            print(f"{record['username']}, {record['permissions']}, {record['salt']}, {record['hashed_password']}")

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
            password = input("Password: ")
            password_manager.add_password(username, permissions, password)

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
