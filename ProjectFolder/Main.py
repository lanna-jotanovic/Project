# Materials inventory dictionary with starting stock and costs
materials = {
    "2_inch_pipe": {"cost_per_ft": 2.75, "stock_ft": 1500, "min_margin": 0.35},
    "2_78_inch_pipe": {"cost_per_ft": 3.85, "stock_ft": 800, "min_margin": 0.35},
    "sucker_rod": {"cost_per_ft": 1.95, "stock_ft": 2000, "min_margin": 0.35}
}

# Displays all materials in the dictionary with their details
def view_materials():
    print("\n--- Material Catalog ---")
    for item, details in materials.items():
        print(f"Item: {item}")
        print(f"  - Cost per ft: ${details['cost_per_ft']:.2f}")
        print(f"  - Stock (ft): {details['stock_ft']}")
        print(f"  - Min Margin: {details['min_margin'] * 100}%")
        print("-" * 30)

# Displays the main menu options
def show_menu():
    print("\n--- Ironclad Custom Welding Estimator ---")
    print("1. View material catalog")
    print("2. Add or update material costs (Coming soon)")
    print("3. Generate new job quote (Coming soon)")
    print("4. Show quote history & margin alerts (Coming soon)")
    print("5. Run steel price simulation (Coming soon)")
    print("6. Sales & profitability report (Coming soon)")
    print("7. Save and exit")

# Runs the main program loop
def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            view_materials()
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