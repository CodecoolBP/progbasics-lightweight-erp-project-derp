""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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
        None"""
    while True:
        title = "Accounting manager"
        exit_message = "(0) Back to main menu"
        list_options = ["(1) Show table", "(2) Add", "(3) Remove", "(4) Update", "(5) Max profits"]
        ui.print_menu(title, list_options, exit_message)

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        file_name = "accounting/items.csv"
        title_list = ["id", "month", "day", "year", "type", "amount"]
        table = data_manager.get_table_from_file(file_name)
        list_titles = ["month: ", "day: ", "year: ", "type: ", "amount: "]
        id_ = ''

        if option == "1":
            common.show_table(table, title_list)
        elif option == "2":
            common.add(table, list_titles, file_name)
        elif option == "3":
            common.remove(table, ui.get_inputs(["ID: "], "")[0], file_name)
        elif option == "4":
            update(table, ui.get_inputs(["ID: "], "")[0])
        elif option == "5":
            which_year_max(table)
        elif option == "0":
            break
    

def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    for idx, i in enumerate(table):
        if id_ in i:
            temp_i = []
            for element in i:
                update_things = ui.get_inputs(["Update (" + str(element) + ") to: "], "")[0]
                temp_i.append(update_things)
            del table[idx]
            table.append(temp_i)
            break
    data_manager.write_table_to_file("accounting/items.csv", table)


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code

    old_year_profits = 0
    new_year_profits = 0
    for i in table:
        if i[3] == "2016" and i[4] == "in":
            new_year_profits += int(i[5])
        elif i[3] == "2016" and i[4] == "out":
            new_year_profits -= int(i[5])
        elif i[3] == "2015" and i[4] == "in":
            old_year_profits += int(i[5])
        elif i[3] == "2015" and i[4] == "out":
            old_year_profits -= int(i[5])
    if new_year_profits > old_year_profits:
        highest_profits = 2016
        return ui.print_result(highest_profits, "Year with highest profit")
    elif old_year_profits > new_year_profits:
        highest_profits = 2015
        return ui.print_result(highest_profits, "Year with highest profit")
            



def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
