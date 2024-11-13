import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('grocery_list')

def menu(message, *arg):
    """
    Provides user a menu option for navigation.
    """
    option_num = -1
    for i in arg:
        option_num += 1
        print(f"[{option_num}] {i}")
    num_of_options = len(arg)
    #list_option = validate_data_input(menu, message, num_of_options)
    print()
    return message, num_of_options


def get_lists():
    """
    Gets and prints all worksheets/lists from the spreadsheet.
    """
    print("Your lists")
    sheet_num = 0
    for list_sheet in SHEET:
        sheet_num += 1
        print(f"[{sheet_num}]", list_sheet.title)
    num_of_options = len(SHEET.worksheets())
    # select_list = validate_data_input(menu,  "Please enter a list number: ", num_of_options) - 1
    # lists = SHEET.get_worksheet(select_list)
    return num_of_options


def get_list_item(grocery_list, entered_item):
    """
    Locates the item enetered by user from the list.
    """
    # entered = validate_data_input("item", "Enter item name: ")
    item = grocery_list.find(entered_item, in_column = 1)
    return item


def update_list(grocery_list, *args):
    """
    Adds user input items to the a list.
    """
    print(f"Adding {args[0]} to list...")
    update_list = SHEET.worksheet(grocery_list)
    update_list.append_row(args)
    print(f"{args[0]} added successfully.\n")
    

def view_list_data(list):
    """
    Shows data of selected list in a table.
    """
    # selected_list = get_lists()
    selected_list = SHEET.get_worksheet(list)
    view_data = selected_list.get_all_values()
    print()
    print(f"Viewing {selected_list.title} list")
    print(tabulate(view_data),"\n")
    return selected_list


def delete_data(data, grocery_list):
    """
    Deletes a selected data and asks user to confirmdeletion.
    """
    if data == "list":
        print(f"Are you sure you want to delete {grocery_list.title}?")
        confirm_list = menu("Please enter option number: ", "No", "Yes")
        while confirm_list != 0:
            if confirm_list == 1:
                print(f"Deleting {data}...\n")
                SHEET.del_worksheet(grocery_list)
                print(f"{data.capitalize()} successfully deleted.\n")
                break
            else:
                print("Invalid option. Please enter a number from the options.")
            confirm_list = menu("Please enter option number: ", "No", "Yes")
    else:
        try:
            cell = get_list_item(grocery_list)
            print(f"Are you sure you want to delete {cell.value}?")
            confirm_item = menu("Please enter option number: ", "No", "Yes")
            while confirm_item != 0:
                if confirm_item == 1:
                    print(f"Deleting {data}...\n")
                    grocery_list.delete_rows(cell.row)
                    print(f"{data.capitalize()} successfully deleted.\n")
                    break
                else:
                    print("Invalid option")
                confirm_item = menu("Please enter option number: ", "No", "Yes")
        except AttributeError:
            print("Sorry, item not found. Please try again.")


def create_new_list(list_name):
    """
    Adds a worksheet for a new grocery list and name it based on user input.
    Adds headings to the worksheet.
    """
    # new_list = validate_data_input("list", "Please enter a name for the list: ")
    new_worksheet = SHEET.add_worksheet(title = list_name, rows="100", cols="20")
    heading = ["Items", "Quantity", "Measurement"]
    new_worksheet.append_row(heading)
    # return new_list


def validate_data_input(*args):

    while True:
        if len(args) == 2:
            if args[0] == "qty":
                try:
                    data_input = float(input(args[1]))
                    return data_input
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            else:
                try:
                    item_input = input(args[1]).strip()
                    if len(item_input) >= 3:
                        return item_input
                    else:
                        print("Invalid input.")
                        print("Please enter atleast 3 characters.")
                except:
                    print("Invalid input.")
                    print("Please enter atleast 3 characters.")
        else:    
            try:
                select_num = int(input(args[1]))
                if select_num <= args[2] and select_num >= 0:
                    return select_num
                else:
                    print("Invalid input. Please enter a number from the options.")
            except ValueError:
                print("Invalid input. Please enter a number from the options.")


def main():
    """
    Run all program functions.
    """
    start_menu = menu("Please enter option number: ", "Exit", "Add new list", "View lists", "Delete list")
    option = validate_data_input("menu", start_menu[0], start_menu[1])
    while option != 0:
        if option == 1:
            new_grocery_list = validate_data_input("list", "Please enter a name for the list: ")
            create_new_list(new_grocery_list)
            new_list_menu = menu("Please enter option number: ", "Exit", "Add items")
            ticked = validate_data_input("menu", new_list_menu[0], new_list_menu[1])
            while ticked != 0:
                if ticked == 1:
                    item = validate_data_input("item", "Enter item name: ")
                    quantity = validate_data_input("qty", "Enter quantity: ")
                    unit_of_measurement = validate_data_input("unit", "Enter unit of measurement: ")
                    update_list(new_grocery_list, item, quantity, unit_of_measurement)
                else:
                    print("Invalid option. Please enter a number from the options.")
                ticked = menu("Please enter option number: ", "Exit", "Add items")
                ticked = validate_data_input("menu", new_list_menu[0], new_list_menu[1])
            print("Your list have been updated.\n")
        elif option == 2:
            your_lists = get_lists()
            selected_list = validate_data_input("menu",  "Please enter a list number: ", your_lists) - 1
            list_to_view = view_list_data(selected_list)
            view_list_menu = menu("Please enter option number: ", "Exit", "Add new item", "Edit an item", "Delete an item")
            to_do = validate_data_input("menu", view_list_menu[0], view_list_menu[1])
            while to_do != 0:
                if to_do == 1:
                    item = validate_data_input("item", "Enter item name: ")
                    quantity = validate_data_input("qty", "Enter quantity: ")
                    unit_of_measurement = validate_data_input("unit", "Enter unit of measurement: ")
                    update_list(list_to_view.title, item, quantity, unit_of_measurement) 
                elif to_do == 2:
                    print("Option 2 has been called")
                elif to_do == 3:
                    entered = validate_data_input("item", "Enter item name: ")
                    item_to_del = get_list_item(list_to_view, entered)
                    delete_data("item", selected_list)
                else:
                    print("Invalid input. Please enter a number from options.")
                view_list_menu = menu("Please enter option number: ", "Exit", "Add new item", "Edit an item", "Delete an item")
                to_do = validate_data_input("menu", view_list_menu[0], view_list_menu[1])
            print("Your list have been updated.\n") 
        elif option == 3:
            selected_list = view_lists()
            delete_data("list", selected_list)
        else:
            print("Invalid input. Please enter a number from options.")
        
        start_menu = menu("Please enter option number: ", "Exit", "Add new list", "View lists", "Delete list")
        option = validate_data_input("menu", start_menu[0], start_menu[1])

    print("Until next time, good bye!")


print("Welcome to your Grocery list.\n")

main()
