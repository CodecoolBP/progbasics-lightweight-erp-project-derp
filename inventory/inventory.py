""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    while True:
            title = "Inventory manager"
            exit_message = "(0) Back to main menu"
            list_options = ["(1) Show table", "(2) Add", "(3) Remove", "(4) Update", "(5) Available items"]
            ui.print_menu(title,list_options, exit_message)
            
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            file_name = "inventory/inventory.csv"
            title_list = ["id","name","manufacturer","purchase year","durability"]
            list_titles = ["name: ", "manufacturer: ", "purchase year: ", "durability: "]
            table = data_manager.get_table_from_file(file_name)
            
            id_ = ''

            if option == "1":
               common.show_table(table,title_list)
            elif option == "2":
                common.add(table, list_titles, file_name)
            elif option == "3":
                common.remove(table,ui.get_inputs(["ID: "], "")[0], file_name)
            elif option == "4":
                common.update(table,ui.get_inputs(["ID: "], "")[0], file_name)
            elif option == "5":
                get_available_items(table)
            elif option == "0":
                break


# special functions:
# ------------------

def get_available_items(table):
    '''
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    '''

    # your code

    list_of_durables = []
    for line in table:
        if int(line[3]) + int(line[4]) >= 2017:
            durable_platforms = line
            
            list_of_durables.append(durable_platforms)
    ui.print_result(list_of_durables, "Items within durability range \n")
    return list_of_durables


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code

