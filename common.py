""" Common module
implement commonly used functions here
"""
import ui
import random
import data_manager
import string

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

    generated = ''.join(random.choice(string.ascii_uppercase + string.digits + 
    string.ascii_lowercase + string.punctuation) for _ in range(6))

    return generated


def show_table(table, title_list):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    
    
    ui.print_table(table, title_list)
