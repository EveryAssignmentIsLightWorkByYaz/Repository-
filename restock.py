def restock_inventory(available_items, inventory_records, current_day):
    """
    Updates the stock/restock for a given day and records the inventory changes.
    
    Parameters:
    - available_items (int): Tshirts available from the previous day.
    - inventory_records (list): Inventory records up to the previous day, where each entry is a tuple:
      (day, sales, restocked items, available items).
    - current_day (int): The day number to add as the current day.
    
    Returns:
    - int: The updated number of available items after restocking for the current day.
    """
    # *** IMPLEMENT THE RESTOCK LOGIC HERE ***
    
    # Example: Placeholder logic (replace with actual logic as needed)

    day = current_day
    inventory = inventory_records 
    items = available_items
    if day == 0:
      restock_amount = 2000
      inventory_records.append((day, 0, restock_amount, items))

    if current_day % 7 == 0:
        restock_amount = 2000 - items
        items = restock_amount + items
        inventory_records.append((day, 0, restock_amount, items))
    return items