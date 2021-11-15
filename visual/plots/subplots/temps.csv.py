import matplotlib.pyplot as plt
import csv


def read_data():
    with open('visual/subplots/temps.csv') as file:
        csv_reader = csv.reader(file)

        # extract headers
        line = next(csv_reader)
        weeks = [week.strip() for week in line]

        # extract temperature data
        data = {weeks[0]: [], weeks[1]: []}

        for line in csv_reader:
            data[weeks[0]].append(float(line[0].strip()))
            data[weeks[1]].append(float(line[1].strip()))

    return data


def run():
    data = read_data()
    weeks = list(data.keys())

    fig, axs = plt.subplots(2, 1)

    ax_index = 0
    for week in weeks:
        axs[ax_index].plot(range(len(data[week])), data[week])
        ax_index += 1

    plt.tight_layout()
    plt.show()


run()
