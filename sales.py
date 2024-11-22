import random

def daily_sales(available_items, inventory_records, current_day):
    """
    Updates sales data for a given day and records the inventory changes.
    
    Parameters:
    - available_items (int): The number of T-shirts available at the start of the day.
    - inventory_records (list): A list of inventory records up to the previous day, where each entry is a tuple:
      (day, sales, restocked items, available items).
    - current_day (int): The day number to process as the current day.
    
    Returns:
    - int: The updated number of available items after sales for the current day.
    
    The function also updates the `inventory_records` list with the sales data for the current day.
    """
    # *** IMPLEMENT THE SALES LOGIC HERE ***
    day = current_day
    inventory = inventory_records 
    items = available_items 
    if day % 7 != 0:
        amount_to_sell = random.randint(0,200)
        items = items - amount_to_sell
        inventory_records.append((day, amount_to_sell, 0, items))
    return items
