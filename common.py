""" Common module
implement commonly used functions here
"""
import ui
import random
import data_manager


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    generated = []
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()+=[]'
    for i in range(8):
        generated.append(random.choice(chars))
    generated = "".join(generated)
    return generated


def show_table(table, title_list):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, title_list)


def add(table, list_titles, csv_file):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_item = ui.get_inputs(list_titles, " ")
    table.append(new_item)
    new_item.insert(0, generate_random(table))
    data_manager.write_table_to_file(csv_file, table)
    return table


def remove(table, id_, file_name):
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
            data_manager.write_table_to_file(file_name, table)
            return table


def update(table, id_, file_name):
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
    data_manager.write_table_to_file(file_name, table)
