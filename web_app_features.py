print("Welcome to the Web Application Feature Selector!")
print("Please select the features you would like to have in your web application:")
print("printing to show the conflict while merging")


print("printing to show the conflict while merging")

features = []

while True:
    print("\nSelect a feature by typing its number:")
    print("1. User authentication")
    print("2. User profile management")
    print("3. Database integration")
    print("4. Payment gateway integration")
    print("5. Social media integration")
    print("6. Search functionality")
    print("7. Chat functionality")
    print("8. File upload functionality")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        features.append("User authentication")
    elif choice == '2':
        features.append("User profile management")
    elif choice == '3':
        features.append("Database integration")
    elif choice == '4':
        features.append("Payment gateway integration")
    elif choice == '5':
        features.append("Social media integration")
    elif choice == '6':
        features.append("Search functionality")
    elif choice == '7':
        features.append("Chat functionality")
    elif choice == '8':
        features.append("File upload functionality")
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")

print("\nSelected features:")
for feature in features:
    print("- " + feature)
