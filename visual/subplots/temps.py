import matplotlib.pyplot as plt


def read_data(file_path):
    # create an empty list to store the temperatures
    temps = []

    # read each temperatured and add it to the list
    with open(file_path) as file:
        for line in file:
            temps.append(float(line.strip()))

    # return the list of temperatures
    return temps


def run():
    data = read_data("temps.txt")
    fig, axs = plt.subplots(1, 2, sharey="row")

    # days to show in x-axis
    days = (1, 2, 3, 4, 5, 6, 7, 8)

    # plot line and bar chart
    axs[0].plot(days, data)
    axs[1].bar(days, data)

    # set x limits to show all days
    axs[0].set_xlim(min(days), max(days))
    axs[1].set_xlim(min(days), max(days))

    # add labels
    axs[0].set_xlabel("Day")
    axs[0].set_ylabel("Temperature")
    axs[1].set_xlabel("Day")
    # Note, no y-label needed for second subplot as the y-axis is shared

    plt.tight_layout()
    plt.show()



