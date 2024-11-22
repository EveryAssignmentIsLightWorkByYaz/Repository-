import os

def delete_report_if_exists(filename):
    """Deletes the specified file if it exists."""
    if os.path.isfile(filename):
        os.remove(filename)
        print(f"'{filename}' has been deleted.")
    else:
        print(f"'{filename}' does not exist.")

def delete_existing_report():
    """Deletes the inventory report if it exists."""
    file = "inventory_report_Tshirts.csv"
    delete_report_if_exists(file)
