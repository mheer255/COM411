"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 10: Import required modules
# TODO: Your code here
import csv
import json
import sys
import time
from datetime import datetime

from tui import welcome
from tui import error
from tui import progress
from tui import menu
from tui import total_records
from tui import serial_number
from tui import observation_dates
from tui import display_record
from tui import display_records

from process import total_number_records
from process import rec_by_serial
from process import rec_by_obdate
from process import rec_by_country
from process import rec_summarise


from visual import con_case_per_country
from visual import top_five_death
from visual import animated_country_rec

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
covid_records = list()


def run():
    try:
        # Task 12: Call the function welcome of the module 'tui'.
        # This will display our welcome message when the program is executed.
        # TODO: Your code here
        welcome()

        # Task 13: Load the data.
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
        # operation has started.
        # - Load the data. Each line in the file should be a record in the list 'covid_records'.
        # You should appropriately handle the case where the file cannot be found or loaded.
        # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
        # been loaded and that the data loading operation has completed.
        # TODO: Your code here

        file = open("data/covid_19_data.csv")
        reader = csv.reader(file)
        lines = len(list(reader))-1
        with open("data/covid_19_data.csv") as file:
            csv_reader = csv.reader(file)
            headings = next(csv_reader)
            count =0
            for values in csv_reader:
                # time.sleep(0.01)    # to check loading process
                count += 1
                p_val = (count/lines)*100
                progress('Data Loading ', p_val)
                covid_records.append(values)
            print()
        total_number_records(covid_records)

        # for i in range(101):
        #     progress('Loading ', int(i))


        variant = 0
        while True:
            print("")

            # Task 14: Using the appropriate function in the module 'tui', display a menu of options
            # for the different operations that can be performed on the data (menu variant 0).
            # Assign the selected option to a suitable local variable
            # TODO: Your code here
            if variant == 0:
                variant = menu(variant)
            # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
            # - Use the appropriate function in the module tui to display a message to indicate that the data processing
            # operation has started.
            # - Process the data (see below).
            # - Use the appropriate function in the module tui to display a message to indicate that the data processing
            # operation has completed.
            #
            # To process the data, do the following:
            # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
            # (menu variant 1).
            # - Check what option has been selected
            #
            #   - If the user selected the option to retrieve an individual record by serial number then
            #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
            #       has started.
            #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
            #       display it.
            #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
            #       completed.
            #
            #   - If the user selected the option to retrieve (multiple) records by observation dates then
            #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
            #       process has started.
            #       - Use the appropriate function in the module 'process' to retrieve records with
            #       - Use the appropriate function in the module 'tui' to display the retrieved records.
            #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
            #       process has completed.
            #
            #   - If the user selected the option to group records by country/region then
            #       - Use the appropriate function in the module 'tui' to indicate that the grouping
            #       process has started.
            #       - Use the appropriate function in the module 'process' to group the records
            #       - Use the appropriate function in the module 'tui' to display the groupings.
            #       - Use the appropriate function in the module 'tui' to indicate that the grouping
            #       process has completed.
            #
            #   - If the user selected the option to summarise the records then
            #       - Use the appropriate function in the module 'tui' to indicate that the summary
            #       process has started.
            #       - Use the appropriate function in the module 'process' to summarise the records.
            #       - Use the appropriate function in the module 'tui' to display the summary
            #       - Use the appropriate function in the module 'tui' to indicate that the summary
            #       process has completed.
            # TODO: Your code here
            elif variant == 1:
                print("")
                psoption = menu(variant)
                if psoption == 1:
                    rec_by_serial(covid_records)
                if psoption == 2:
                    rec_by_obdate(covid_records)
                if psoption == 3:
                    rec_by_country(covid_records)
                if psoption == 4:
                    rec_summarise(covid_records)
                variant = 0


            # Task 21: Check if the user selected the option for visualising data.
            # If so, then do the following:
            # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
            # has started.
            # - Visualise the data by doing the following:
            #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
            #   - call the appropriate function in the module 'visual'
            # - Use the appropriate function in the module 'tui' to display a message to indicate that the
            # data visualisation operation has completed.
            # TODO: Your code here
            elif variant == 2:
                con_case_per_country(covid_records)
                top_five_death(covid_records)
                animated_country_rec(covid_records)
                variant = 0

            # Task 25: Check if the user selected the option for exporting data.  If so, then do the following:
            # - Use the appropriate function in the module 'tui' to retrieve the type of data to be exported.
            # - Check what option has been selected
            #
            # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
            # - Export the data (see below)
            # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
            #
            # To export the data, you should demonstrate the application of OOP principles including the concepts of
            # abstraction and inheritance.  You should create suitable classes with appropriate methods.
            # You should use these to write the records (either all or only those for a specific country/region) to a JSON file.
            # TODO: Your code here
            elif variant == 3:
                totalrows = len(open('data/covid_19_data.csv').readlines())-1
                with open("data/covid_19_data.csv") as file1:
                    csvRead = csv.DictReader(file1)
                    timestr = time.strftime("%Y%m%d-%H%M%S")

                    mydata = {}
                    filename = f'jsonFilename{timestr}.csv'
                    cnt = 0
                    for rows in csvRead:
                        cnt += 1
                        progress('Exporting Process ', ((cnt / totalrows ) * 100))
                        mykey = rows['SNo']
                        mydata[mykey] = rows

                with open(filename, 'w', encoding='utf-8') as jsonfile:
                    jsonfile.write(json.dumps(mydata, indent=4))
                variant = 0

            # Task 26: Check if the user selected the option for exiting the program.
            # If so, then break out of the loop
            # TODO: Your code here
            elif variant == 4:
                break

            # Task 27: If the user selected an invalid option then use the appropriate function of the
            # module tui to display an error message
            # TODO: Your code here
            else:
                print("Please choose correct option ")
                variant = 0
    except Exception as e:
        error(e)
    pass  # can remove


if __name__ == "__main__":
    run()
