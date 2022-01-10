"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""
import time

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""
from tui import progress
# TODO: Your code here
def total_number_records(records):
    from tui import total_records
    t_rec = len(records)
    total_records(t_rec)
pass
def rec_by_serial(records):
    from tui import serial_number
    from tui import display_record
    getlist = []
    sn = serial_number()
    for i in range(len(records)):
        # time.sleep(0.001)
        progress('Data Processing ',((i/len(records))*100))
        if int(sn) == int(records[i][0]):
            getlist = records[i]
            # progress('Data Processing',100)
    print('')
    display_record(getlist)
    # print(getlist)
pass
def rec_by_obdate(records):
    from tui import observation_dates
    from tui import display_records
    getlist = []
    od = observation_dates()
    for i in range(len(records)):
        progress('Data Processing ', ((i / len(records)) * 100))
        if records[i][1] in od:
            getlist.append(records[i])
    print('')
    display_records(getlist)
pass
def rec_by_country(records):
    from tui import serial_number
    from tui import display_records
    getlist = []
    sn = input("Enter a country Name for a records:")
    for i in range(len(records)):
        progress('Data Processing ', ((i / len(records)) * 100))
        # print(sn.lower())
        if sn.lower() == records[i][3].lower():
            getlist.append(records[i])
    print('')
    display_records(getlist)
pass
def rec_summarise(records):

    from tui import smurize_menu
    from tui import total_no_of

    data = smurize_menu()
    total_no_of(records,data)
    #display_records(records)
pass
def con_case_country_visual(records):
    con_case_by_country = []
    total_con_case = 0
    country = []
    data = []
    for i in range(len(records)):
        if records[i][3] not in country:
            country.append(records[i][3])

    for i in range(len(country)):
        cur_country_count = 0
        for j in range(len(records)):
            progress('Data Processing ', ((j / len(records)) * 100))
            if country[i].lower() == records[j][3].lower():
                cur_country_count += int(records[i][5])
                total_con_case += int(records[i][5])
        con_case_by_country.append(cur_country_count)
    data.append(country)
    data.append(con_case_by_country)
    data.append([total_con_case])
    return data

def death_case_country_visual(records):
    death_case_by_country = []
    total_death_case = 0
    country = []
    data = []
    for i in range(len(records)):
        if records[i][3] not in country:
            country.append(records[i][3])

    for i in range(len(country)):

        cur_country_count = 0
        for j in range(len(records)):
            progress('Data Processing ', ((j / len(records)) * 100))
            if country[i].lower() == records[j][3].lower():
                cur_country_count += int(records[j][6])
                total_death_case += int(records[j][6])
        death_case_by_country.append(cur_country_count)
    data.append(country)
    data.append(death_case_by_country)
    data.append([total_death_case])
    return data

def get_all_covid_rec(records):
    total_confirmed_case = 0
    total_death_case = 0
    total_recover_case = 0
    data = []
    for j in range(len(records)):
        progress('Data Processing ', ((j / len(records)) * 100))
        total_confirmed_case += int(records[j][5])
        total_death_case += int(records[j][6])
        total_recover_case += int(records[j][7])
    data.append(total_confirmed_case)
    data.append(total_death_case)
    data.append(total_recover_case)
    return data