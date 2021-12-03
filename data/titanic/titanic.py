import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...")
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)

        print("Done!")


def display_menu():
    print ("Please select one of the following options:"
           "\n[1] Display the names of all passengers"
           "\n[2] Display the number of passengers that survived"
           "\n[3] Display the number of passengers per gender"
           "\n[4] Display the number of passengers per age group"
           "\n[5] Display the number of survivors per age group")

    response = int(input())
    return response


def display_passenger_names():
    print("the name of the passengers are...")
    for record in records:
     passenger_name = record[3]
     print(f"{passenger_name}")


def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status == int(record[1])
        if survival_status == 1:
            num_survived = (num_survived + 1)
            print(f"{num_survived} passengers survived")


def display_passengers_per_gender():
    female = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender == 'male':
         males += 1
        elif gender == 'female':
             female += 1
        else:
            print("")
            print(f"females:{females}, males: {males}")


def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in records:
        if records[5] != "":
            age = float(record[5])
            if age < 18:
               children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"children: {children}, adults: {adults}, elderly:{elderly}")


def display_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    ch_survived = 0
    ad_survived = 0
    el_survived = 0

    for record in records:
        if record[5] != "":
            age = float(records[5])
            if age < 18:
                children += 1
            elif age < 65:




               survival_status = int(record[1])
            if survival_status == 1 and age < 18:
                ch_survived += 1
            elif survival_status == 1 and age < 65:
                ad_survived += 1
            elif survival_status == 1 and age > 65:
                el_survived += 1
    print(f"children: {ch_survived}/{children}, adults: {ad_survived}/{adults}, elderly: {el_survived}/{elderly}")


def run():
    load_data('titanic.csv')
    num_records = len(records)
    print(f"successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"you have selected option: {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_age_group()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("error!option not recognised ")


if __name__ == "__main__":
    run()