import csv
import tui


def read_data(file_path):
    data = []

    tui.started(f"Reading data from {file_path}")

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
        tui.completed()
        return data


def run():
    athlete_data = read_data("athlete_events (2).csv")

    while True:
        selection = tui.menu()
        print(selection)
        if selection == "years":
            list_years(athlete_data)
        elif selection == "tally":
            tally_medals(athlete_data)
        elif selection == "team":
            tally_team_medals(athlete_data)
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


location_year = 9


def list_years(data):
    tui.started("listing years")
    years = set()
    for record in data:
        year = record["location year"]
        years.add(year)
    tui.display_years(years)
    tui.completed()


location_medals = 14


def tally_medals(data):
    tui.started("displaying medals")
    medals = {"gold": 0, "silver": 0, "bronze": 0}
    for record in data:
        medal = record[location_medal]
        if medal == "gold":
            medals[medal] += 1
        elif medal == "silver":
            medals[medal] += 1
        elif medal == "bronze":
            medals[medal] += 1
        else:
            break
    tui.display_medal_tally(medals)
    tui.completed()

location_teams = 6


def tally_team_medals(data):
    tui.started("teams and the total count of their medals")
    team_medals = {}
    for record in data:
        team = record[location_teams]
        medal = record[loctaion_medals]
        if medal != 'NA':

            if team in team_medals:
                team_medals[team][medal] += 1
            else:

                team_medals[team] = {"gold": 0, "silver": 0, "bronze": 0}
                team_medals[team][medal] += 1

    tui.display_team_medal_tally(team_medals)
    tui.completed()


if __name__ == "__main__":
    run()
