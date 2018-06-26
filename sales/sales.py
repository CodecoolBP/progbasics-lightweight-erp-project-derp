""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
            title = "Sales manager"
            exit_message = "Back to main menu"
            list_options = ["(1) Show table", "(2) Add", "(3) Remove", "(4) Update", "(5) Cheapo game"]
            ui.print_menu(title,list_options, exit_message)
            
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            file_name = "sales/sales.csv"
            title_list = ["id","title","price","month","day","year"]
            table = data_manager.get_table_from_file(file_name)
            id_ = ''

            if option == "1":
                common.show_table(table,title_list)
            elif option == "2":
                add(table)
            elif option == "3":
                remove(table,ui.get_inputs(["ID: "], "")[0])
            elif option == "4":
                update(table,ui.get_inputs(["ID: "], "")[0])
            elif option == "5":
                get_lowest_price_item_id(table)
            elif option == "0":
                break



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    list_titles = ["month: ", "day: ", "year: ", "type: ", "amount: "]
    new_item = ui.get_inputs(list_titles, "")
    table.append(new_item)
    new_item.insert(0,common.generate_random(table))
    data_manager.write_table_to_file("sales/sales.csv", table)
    return table

def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    for line in table:
        if id_ in line:
            table.remove(line)
            data_manager.write_table_to_file("sales/sales.csv", table)
            return table


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
    for idx, line in enumerate(table):
        if id_ in line:
            temp_line = []
            for element in line:
                update_things = ui.get_inputs(["Update (" + str(element) + ") to: "], "")[0]
                temp_line.append(update_things)
            del table[idx]
            table.append(temp_line)
            break
    data_manager.write_table_to_file("sales/sales.csv", table)


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code

    lowest_price = 1000000000000000000
    for i in range(len(table)):
        if int(table[i][2]) < lowest_price:
            lowest_index = i
            lowest_price = int(table[i][2])

    ui.print_result(table[lowest_index][0], "ID of lowest priced item")
    ui.print_result(table[lowest_index][1], "ID of lowest priced item")


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
