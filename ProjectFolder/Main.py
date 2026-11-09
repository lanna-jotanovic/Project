def show_menu():
    print("\n--- Custom Welding Estimator ---")
    print("1. View material catalog")
    print("2. Add or update material costs")
    print("3. Generate new job quote")
    print("4. Show quote history and margin alerts")
    print("5. Run steel price simulation")
    print("6. Sales and profitability report")
    print("7. Save and exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("Coming soon")
        elif choice == "2":
            print("Coming soon")
        elif choice == "3":
            print("Coming soon")
        elif choice == "4":
            print("Coming soon")
        elif choice == "5":
            print("Coming soon")
        elif choice == "6":
            print("Coming soon")
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()