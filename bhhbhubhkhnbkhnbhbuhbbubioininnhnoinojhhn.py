# A simple system to print a congratulations message using string operations

def print_congratulations(name, achievement):
    message = f"Congratulations, {name}! You have achieved {achievement}!"
    print(message)

# Example usage
name = input("Enter the name: ")
achievement = input("Enter the achievement: ")
print_congratulations(name, achievement)