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
            exit_message = "Back to main menu"
            list_options = ["(1) Show table", "(2) Add", "(3) Remove", "(4) Update", "(5) ID of longest name", "(6) subscribers"]
            ui.print_menu(title,list_options, exit_message)
            
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            file_name = "crm/customers.csv"
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
                get_longest_name_id(table)
            elif option == "6":
                get_subscribed_emails(table)
            elif option == "0":
                break

    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    list_titles = ["month: ", "day: ", "year: ", "type: ", "amount: "]
    new_item = ui.get_inputs(list_titles, "")
    table.append(new_item)
    new_item.insert(0,common.generate_random(table))
    data_manager.write_table_to_file("crm/customers.csv", table)
    return table
    # your code

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
            data_manager.write_table_to_file("crm/customers.csv", table)
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

    # your code

    
    for i in range(len(table)):
        longest_name = len("")
        if len(table[i][1]) > longest_name:
            longest_name_index = i
            longest_name = len(table[i][1])
   # ui.print_result(table[longest_name_index][0], "ID")
            '''for j in range(len(table)):
                longest_names = []
                if len(table[j][1]) == longest_name:
                    samesies = table[j][1]
                    longest_names.append(samesies)
            ui.print_result(longest_names, "all names")'''
    
# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
    subscribers = []
    subscribed = 0
    for line in range(len(table)):
        if int(table[line][3]) > subscribed:
            subscriber_index = line
            subscriber_name = str(table[line][1])
            subscriber_mail = str(table[line][2])
            subscriber_info = subscriber_name, subscriber_mail
            ui.print_result(subscriber_info, " ")
            #subscribers.append(subscriber_info)
  
    ''' for line in table:
        if "1" in line[3]:'''
            