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

# Adds a new material or updates an existing one with basic input validation
def add_or_update_material():
    print("\n--- Add or Update Material ---")
    item_name = input("Enter material name (e.g., 3_inch_pipe): ").strip().lower()
    
    # Input validation for cost using standard loops and string checks
    cost_input = input("Enter cost per foot ($): ")
    while not cost_input.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter numbers only.")
        cost_input = input("Enter cost per foot ($): ")
    cost = float(cost_input)
            
    # Input validation for stock quantity using .isdigit()
    stock_input = input("Enter stock quantity in feet: ")
    while not stock_input.isdigit():
        print("Invalid input. Please enter whole numbers only.")
        stock_input = input("Enter stock quantity in feet: ")
    stock = int(stock_input)
            
    # If the item already exists, update it; otherwise, add it as new
    if item_name in materials:
        materials[item_name]["cost_per_ft"] = cost
        materials[item_name]["stock_ft"] += stock
        print(f"Success! Updated existing item '{item_name}' with new cost and added {stock} ft to stock.")
    else:
        materials[item_name] = {"cost_per_ft": cost, "stock_ft": stock, "min_margin": 0.35}
        print(f"Success! Added new item '{item_name}' to the catalog.")

# Displays the main menu options
def show_menu():
    print("\n--- Ironclad Custom Welding Estimator ---")
    print("1. View material catalog")
    print("2. Add or update material costs")
    print("3. Generate new job quote")
    print("4. Show quote history & margin alerts")
    print("5. Run steel price simulation")
    print("6. Sales & profitability report")
    print("7. Save and exit")

# Runs the main program loop
def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            view_materials()
        elif choice == "2":
            add_or_update_material()
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