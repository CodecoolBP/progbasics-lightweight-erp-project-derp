# This module creates reports for marketing department.
# This module can run independently from other modules.
# Has no own datastructure but uses other modules.
# Avoud using the database (ie. .csv files) of other modules directly.
# Use the functions of the modules instead.

# todo: importing everything you need

# importing everything you need
import os
import ui
import common
from sales import sales
from crm import crm
import data_manager


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    while True:
        title = "Data analyser"
        exit_message = "(0) Back to main menu"
        list_options = ["(1) Last buyer name",
                        "(2) Last buyer ID",
                        "(3) Buyer name spent most and the money spent",
                        "(4) Buyer ID spent most and the money spent",
                        "(5) The most frequent buyers names",
                        "(6) The most frequent buyers IDs"]

        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        file_name = "crm/customers.csv"
        title_list = ["id", "name", "email", "subscribed"]
        table = data_manager.get_table_from_file(file_name)
        list_titles = ["name: ", "email: ", "subscriber (0/1): "]
        id_ = ''

        if option == "1":
            common.show_table(table, title_list)
        elif option == "2":
            common.add(table, list_titles, file_name)
        elif option == "3":
            common.remove(table, ui.get_inputs(["ID: "], "")[0], file_name)
        elif option == "4":
            common.update(table, ui.get_inputs(["ID: "], "")[0], file_name)
        elif option == "5":
            get_oldest_person(table)
        elif option == "6":
            get_persons_closest_to_average(table)
        elif option == "0":
            break


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        Customer name of the last buyer
    """

    pass


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """

    # your code

    pass


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.
    Returns a tuple of customer name and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer name and the sum the customer spent
    """

    # your code

    pass


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """

    # your code

    pass


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customers' name) who bought most frequently.
    Returns an ordered list of tuples of customer names and the number of their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer names and num of sales
    """

    # your code

    pass


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent.
    Returns an ordered list of tuples of customer id and the number their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer ids and num of sales
    """

    # your code

    pass
