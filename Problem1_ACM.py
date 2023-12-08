class AccessControlMatrix:
    def __init__(self, roles, resources):
        self.roles = roles
        self.resources = resources
        self.matrix = {role: {resource: False for resource in resources} for role in roles}

    def grant_permission(self, role, resource):
        if role in self.roles and resource in self.resources:
            self.matrix[role][resource] = True

        else:
            print("Invalid role or resource")

    def check_permission(self, role, resource):
        if role in self.roles and resource in self.resources:
            return self.matrix[role][resource]
        else:
            return False


# Example usage with user input
roles = ["Client", "Premium Client", "Financial Advisor", "Financial Planner", 
         "Investment Analyst", "Technical Support", "Teller", "Compliance Officer"]
resources = ["View Account Balance", 
             "View Investment Portfolio", 
             "View Financial Advisor Contact Details", 
             "View Financial Planner and Investment Analyst Contact Details", 
             "Modify Investment Portfolio", 
             "Validate Modifications to Investment Portfolio", 
             "View Money Market Instruments", 
             "View Private Consumer Instruments", 
             "View Derivatives Trading", 
             "View Interest Instruments", 
             "View Client Information", 
             "Access System in Business Hours"]

acm = AccessControlMatrix(roles, resources)

# Granting permissions for Client Role
acm.grant_permission("Client", "View Account Balance")
acm.grant_permission("Client", "View Investment Portfolio")
acm.grant_permission("Client", "View Financial Advisor Contact Details")

# Granting permissions for Premium Client Role
acm.grant_permission("Premium Client", "View Account Balance")
acm.grant_permission("Premium Client", "View Investment Portfolio")
acm.grant_permission("Premium Client", "View Financial Advisor Contact Details")
acm.grant_permission("Premium Client", "View Financial Planner and Investment Analyst Contact Details")
acm.grant_permission("Premium Client", "Modify Investment Portfolio")

# Granting permissions for Financial Advisor Role
acm.grant_permission("Financial Advisor", "View Account Balance")
acm.grant_permission("Financial Advisor", "View Investment Portfolio")
acm.grant_permission("Financial Advisor", "Modify Investment Portfolio")
acm.grant_permission("Financial Advisor", "View Private Consumer Instruments")

# Granting permissions for Financial Planner Role
acm.grant_permission("Financial Planner", "View Account Balance")
acm.grant_permission("Financial Planner", "View Investment Portfolio")
acm.grant_permission("Financial Planner", "Modify Investment Portfolio")
acm.grant_permission("Financial Planner", "View Money Market Instruments")
acm.grant_permission("Financial Planner", "View Private Consumer Instruments")

# Granting permissions for Investment Analyst Role
acm.grant_permission("Investment Analyst", "View Account Balance")
acm.grant_permission("Investment Analyst", "View Investment Portfolio")
acm.grant_permission("Investment Analyst", "Modify Investment Portfolio")
acm.grant_permission("Investment Analyst", "View Money Market Instruments")
acm.grant_permission("Investment Analyst", "View Private Consumer Instruments")
acm.grant_permission("Investment Analyst", "View Derivatives Trading")
acm.grant_permission("Investment Analyst", "View Interest Instruments")

# Granting permissions for Technical Support Role
acm.grant_permission("Technical Support", "View Client Information")

# Granting permissions for Teller Role
acm.grant_permission("Teller", "Access System in Business Hours")

# Granting permissions for Compliance Officer Role
acm.grant_permission("Compliance Officer", "Validate Modifications to Investment Portfolio")

while True:
    user_role = input("Enter your role (type 'exit' to end): ")
    
    if user_role.lower() == 'exit':
        break

    user_resource = input(f"Hello {user_role}, what would you like to access?: ")

    # Granting permissions based on user input
    if acm.check_permission(user_role, user_resource):
        print(f"{user_role} has permission to access {user_resource}.")
    else:
        print(f"{user_role} does not have permission to access {user_resource}.")

        # Prompt user to input a different resource
        new_resource = input(f"{user_role}, please enter a different resource: ")
        if acm.check_permission(user_role, new_resource):
            print(f"{user_role} now has permission to access {new_resource}.")
        else:
            print(f"{user_role} does not have permission to access {new_resource}.")

print("Program exited.")