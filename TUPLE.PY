# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
city = input("Enter your city: ")
japanese_level = input("Enter your Japanese level (Beginner/Intermediate/Advanced): ")

# Store in a tuple
user_info = (name, age, gender, city, japanese_level)

# Display information
print("\nUser Information:")
print(f"Name: {user_info[0]}")
print(f"Age: {user_info[1]}")
print(f"Gender: {user_info[2]}")
print(f"City: {user_info[3]}")
print(f"Japanese Level: {user_info[4]}")
