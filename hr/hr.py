""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
            title = "HR manager"
            exit_message = "(0) Back to main menu"
            list_options = ["(1) Show table", "(2) Add", "(3) Remove", "(4) Update", "(5) Oldest Person", "(6) Age closest to average"]
            ui.print_menu(title,list_options, exit_message)
            
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            file_name = "hr/persons.csv"
            title_list = ["id", "name", "birthyear"]
            table = data_manager.get_table_from_file(file_name)
            list_titles = ["name: ", "birth year: "]
            id_ = ''

            if option == "1":
                common.show_table(table,title_list)
            elif option == "2":
                common.add(table, list_titles, file_name)
            elif option == "3":
                remove(table,ui.get_inputs(["ID: "], "")[0])
            elif option == "4":
                update(table,ui.get_inputs(["ID: "], "")[0])
            elif option == "5":
                get_oldest_person(table)
            elif option == "6":
                get_persons_closest_to_average(table)
            elif option == "0":
                break


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
            data_manager.write_table_to_file("hr/persons.csv", table)
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
    data_manager.write_table_to_file("hr/persons.csv", table)


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    max_age = 2018
    
    for i in range(len(table)):
        if int(table[i][2]) < max_age:
            oldest_index = i
            max_age = int(table[i][2])
            oldies = []
            oldies.append(table[i][1])
        elif int(table[i][2]) == max_age:
            oldies.append(table[i][1])

    return  ui.print_result(oldies, max_age)

def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code

    age_sum = 0
    date_of_birth = []
    date_of_birth_subtract = []
    name_of_people = []
  
    for i in range(len(table)):
        age_sum = age_sum + int(table[i][2])
        name_of_people.append(table[i][1])
        date_of_birth.append(table[i][2])
    average = age_sum / len(table)

    for i in date_of_birth:
        i = int(i) - average
        date_of_birth_subtract.append(i)

    minimum=1000
    name=name_of_people[0]
    for i in range(len(date_of_birth)):
        x = abs(int(average)-int(date_of_birth[i]))
        if x < minimum:
            minimum = x
            name = name_of_people[i]
    ui.print_result(name,"The name of the person closest to the average: \n")
