import csv

def write_csv_report(filename, data):
    """Writes the provided data to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def generate_report(inventory_records):
    """Generates a report of inventory activity."""
    header = [("Day", "Sold Units", "Restocked Units", "Available Units")]
    report_data = header + inventory_records
    write_csv_report('inventory_report_Tshirts.csv', report_data)
