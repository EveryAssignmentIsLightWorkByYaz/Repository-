import random
import csv
import os
from IMS_simulation import run_simulation
from report_generation import generate_report
from unit_test import report_check

def display_menu():
    """Displays the main menu options to the user."""
    print("\nMenu:")
    print("1. Generate Report")
    print("2. Report Check")
    print("3. Exit")

def handle_choice(choice, total_days, inventory_records):
    """Handles user choices from the menu."""
    if choice == '1':
        run_simulation(total_days, inventory_records)
        generate_report(inventory_records)
        print("Report generated successfully.")
    elif choice == '2':
        report_check()
        print("Report check completed.")
    elif choice == '3':
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def main():
    total_days = 50
    inventory_records = []
    running = True

    while running:
        display_menu()
        user_input = input("Enter your choice: ")
        running = handle_choice(user_input, total_days, inventory_records)

if __name__ == "__main__":
    main()
