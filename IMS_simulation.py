from restock import restock_inventory
from sales import daily_sales

def simulate_day(current_day, available_items, inventory_records):
    """Simulates restocking and sales for a single day."""
    available_items = restock_inventory(available_items, inventory_records, current_day)
    return daily_sales(available_items, inventory_records, current_day)

def run_simulation(total_days, inventory_records):
    """Runs the simulation for the specified number of days."""
    available_items = 2000
    for day in range(total_days):
        available_items = simulate_day(day, available_items, inventory_records)
