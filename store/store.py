""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
        title = "Storage manager"
        exit_message = "(0) Back to main menu"
        list_options = ["(1) Show table", "(2) Add", "(3) Remove", "(4) Update", "(5) Counts by manufacturers"]
        ui.print_menu(title,list_options, exit_message)

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        file_name = "store/games.csv"
        title_list = ["id","title","manufacturer","price","stock"]
        list_titles = ["title: ", "manufacturer: ", "price: ", "stock: "]
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
            get_counts_by_manufacturers(table)
        elif option == "0":
            break

# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    count_the_manufacturers = {}
    for element in table:
        count_the_manufacturers[element[2]] = 0
    for i in table:
        for h in count_the_manufacturers.keys():
            if i[2] == h:
                count_the_manufacturers[h] += 1
    ui.print_result(count_the_manufacturers, "Manufacturer count")
    return(count_the_manufacturers)


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
