from read import read_file
from write import write_file, generate_invoice
from operation import rent_land, return_land, display_lands

def validate_input(prompt, input_type):
    while True:
        user_input = input(prompt)
        try:
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")


def validate_kitta(kitta_number, land_data):
    if not any(int(land[0]) == kitta_number for land in land_data):
        print("The kitta number is not available.")
        return False
    return True

def print_menu():
    print("\n" + "="*30)
    print("       Land Rental System")
    print("="*30)
    print("1. Display available lands")
    print("2. Rent land")
    print("3. Return land")
    print("4. Exit")
    print("="*30)

def main():
    file_path = 'lands.txt'
    land_data = read_file(file_path)

    while True:
        print_menu()
        choice = validate_input("Enter your choice: ", int)

        if choice == 1:
            display_lands(land_data)
        elif choice == 2:
            kitta_number = validate_input("Enter the kitta number: ", int)
            if not validate_kitta(kitta_number, land_data):
                continue
            customer_name = input("Enter the customer name: ")
            duration_months = validate_input("Enter the duration of rent (in months): ", int)
            land_data, invoice_data = rent_land(land_data, kitta_number, customer_name, duration_months)
            if invoice_data:
                invoice_file_name = f"invoice_{kitta_number}_{customer_name}.txt"
                generate_invoice(invoice_data, invoice_file_name, "rent_invoices")
                print(f"\nInvoice generated: {invoice_file_name}")
            write_file(file_path, land_data)
        elif choice == 3:
            kitta_number = validate_input("Enter the kitta number: ", int)
            if not validate_kitta(kitta_number, land_data):
                continue
            customer_name = input("Enter the customer name: ")
            land_data, invoice_data = return_land(land_data, kitta_number, customer_name)
            if invoice_data:
                invoice_file_name = f"return_invoice_{kitta_number}_{customer_name}.txt"
                generate_invoice(invoice_data, invoice_file_name, "return_invoices")
                print(f"\nReturn invoice generated: {invoice_file_name}")
            write_file(file_path, land_data)
        elif choice == 4:
            print("\nThank you for using the Land Rental System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()
