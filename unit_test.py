import csv
from utils import delete_existing_report
from report_generation import generate_report
from IMS_simulation import run_simulation

def read_report(file):
    """Reads the CSV report and returns the header and data rows."""
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = list(reader)
    return header, data

def validate_day_range(day, file):
    """Validates that the day is within the expected range (0 to 49)."""
    if not (0 <= day <= 49):
        print(f"Error: Day {day} out of range in file {file}")
        return False
    return True

def validate_units(units, max_value, file, day):
    """Validates that units are within the allowed maximum value."""
    if int(units) > max_value:
        print(f"Error: Units exceed {max_value} in file {file} on day {day}")
        return False
    return True

def check_report_correctness():
    file = "inventory_report_Tshirts.csv"
    header, data = read_report(file)
    
    total_restocked, total_sold = 0, 0
    restock_days = set()
    
    for row in data:
        day_str, sold_units, restocked_units, remaining_units = row
        day = int(day_str)
        
        # Validate day and units
        if not (validate_day_range(day, file) and
                validate_units(restocked_units, 2000, file, day) and
                validate_units(remaining_units, 2000, file, day)):
            return
        
        # Update totals and track restock days
        total_restocked += int(restocked_units)
        total_sold += int(sold_units)
        if int(restocked_units) > 0:
            restock_days.add(day)
    
    # Check for missing restocks on expected days
    for expected_restock_day in range(7, 51, 7):
        if expected_restock_day not in restock_days:
            print(f"Error: Missing restock on day {expected_restock_day} in file {file}")
            return
    
    # Verify if totals match
    last_remaining_units = int(data[-1][3])
    if total_restocked - total_sold - last_remaining_units != 0:
        print(f"Error: Totals do not match in file {file}")
        return
    
    print(f"ALL CHECKS PASSED :) for file {file}")

def report_check():
    """Deletes the old report, runs a new simulation, and checks the report correctness."""
    total_days = 50
    inventory_records = []
    delete_existing_report()
    inventory_records.clear()
    run_simulation(total_days, inventory_records)
    generate_report(inventory_records)
    check_report_correctness()
