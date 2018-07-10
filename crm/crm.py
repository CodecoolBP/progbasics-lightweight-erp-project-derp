""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
            title = "CRM manager"
            exit_message = "(0) Back to main menu"
            list_options = ["(1) Show table", "(2) Add", "(3) Remove", "(4) Update", "(5) ID of longest name", "(6) subscribers"]
            ui.print_menu(title,list_options, exit_message)
            
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            file_name = "crm/customers.csv"
            title_list = ["id", "name", "email", "subscribed"]
            table = data_manager.get_table_from_file(file_name)
            list_titles = ["name: ", "email: ", "subscriber (0/1): "]
            id_ = ''

            if option == "1":
                common.show_table(table,title_list)
            elif option == "2":
                common.add(table, list_titles, file_name)
            elif option == "3":
                common.remove(table,ui.get_inputs(["ID: "], "")[0], file_name)
            elif option == "4":
                update(table,ui.get_inputs(["ID: "], "")[0])
            elif option == "5":
                get_longest_name_id(table)
            elif option == "6":
                get_subscribed_emails(table)
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
    data_manager.write_table_to_file("crm/customers.csv", table)


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """


    longest_name = len("a")
    names = []
    ids = []
    for i in range(len(table)):
        if len(table[i][1]) > longest_name:
            longest_name_index = i
            longest_name = len(table[i][1])
            names = []
            ids = []
            names.append(table[i][1])
            ids.append(table[i][0])
        elif len(table[i][1]) == longest_name:
            names.append(table[i][1])
            ids.append(table[i][0])
            
    return ui.print_result(ids, "ids of people with longest names")
    
    '''for j in range(len(table)):
        if len(table[j][1]) == longest_name:
            all_longest_names = j 
            names.append(table[all_longest_names][1])
            ids.append(table[all_longest_names][0])    
            longest_names_dict = dict(zip(names, ids))
    ui.print_result(longest_names_dict, "List of people with the longest names")'''


    
# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
        """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

    pass


# functions supports data analyser
# --------------------------------
         """

def get_name_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass


def get_name_by_id_from_table(table, id):

    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass
