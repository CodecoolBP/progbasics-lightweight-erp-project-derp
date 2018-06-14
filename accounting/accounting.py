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

    title = "Accounting manager"
    exit_message = "Back to main menu"
    list_options = ["show table", "add", "remove", "update"]
    ui.print_menu(title,list_options, exit_message)
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    file_name = "accounting/accounting.csv"
    title_list = ["id","title","price","month","day","year"]
    table = data_manager.get_table_from_file(file_name)

    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3"
        remove(table, id_)

    # you code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table, ["id", "month", "day", "year", "type", "amount"])
    
    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    list_titles = ["id", "month", "day", "year", "type", "amount"]
    new_item = ui.get_inputs(list_titles, "")
    table.append(new_item)
    data_manager.write_table_to_file("accounting/accounting.csv", table)
    return table
    # your code



def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    for line in table:
        if id_ in line:
            table.remove(line)
    return table

    # your code

    

def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


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
