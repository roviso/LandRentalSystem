import datetime

def rent_land(land_data, kitta_number, customer_name, duration_months):
    for land in land_data:
        print("this is land : ",land[0],land[5])
        print("this is kitta : ",int(land[0]) == int(kitta_number) )    
        print("this is status : ",land[5] == 'Available')
        if int(land[0]) == int(kitta_number) and land[5] == 'Available':
            print("this is matched land : ",land)
            land[5] = 'Not Available'
            invoice_data = {
                "Kitta Number": kitta_number,
                "City/District": land[1],
                "Direction": land[2],
                "Area (anna)": land[3],
                "Customer Name": customer_name,
                "Rent Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Duration (months)": duration_months,
                "Total Amount": int(land[4]) * duration_months
            }
            return land_data, invoice_data
    print("\nLand is not available for rent.")
    return land_data, None

def return_land(land_data, kitta_number, customer_name):
    for land in land_data:
        if int(land[0]) == kitta_number and land[5] == 'Not Available': 
            land[5] = 'Available'
            invoice_data = {
                "Kitta Number": kitta_number,
                "City/District": land[1],
                "Direction": land[2],
                "Area (anna)": land[3],
                "Customer Name": customer_name,
                "Return Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            return land_data, invoice_data
    print("\nLand is not rented or already available.")
    return land_data, None

def display_lands(land_data):
    print("\nAvailable Lands:\n")
    headers = ["Kitta Number", "City/District", "Direction", "Area (anna)", "Price", "Status"]
    row_format = "{:<15} {:<15} {:<10} {:<10} {:<10} {:<15}"
    print(row_format.format(*headers))
    print("-" * 75)
    for land in land_data:
        print(row_format.format(*land))
