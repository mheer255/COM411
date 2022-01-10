"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here
import matplotlib.pyplot as plt
import numpy as np
from process import con_case_country_visual
from process import death_case_country_visual
from process import get_all_covid_rec
def con_case_per_country(records):
    data = con_case_country_visual(records)
    countries = data[0]
    con_case = data[1]
    # total_con_case = data[2]


    plt.title("The number of confirmed cases per \n" + "country/region",
              bbox={'facecolor': '0.8', 'pad': 5})
    # plt.pie(con_case, labels=countries)
    plt.pie(con_case)
    plt.show()
    print('')
    pass


def top_five_death(records):
    data = death_case_country_visual(records)

    countries = data[0]
    death_case = data[1]
    topcountry = []
    topdeath = []
    mixlist = []

    for x in range(len(countries)):
        list = {"country":countries[x],"deaths":int(death_case[x])}
        mixlist.append(list)
    mixlist.sort(reverse=True, key=myFunc)
    top_five = mixlist[:5]
    for i in range(5):
        topcountry.append(top_five[i]["country"])
        topdeath.append(top_five[i]["deaths"])

    plt.bar(topcountry, topdeath)
    ax = plt.gca()
    plt.bar_label(ax.containers[0])
    plt.show()
    print('')
    pass

def myFunc(e):
  return e["deaths"]


def animated_country_rec(records):


    from matplotlib.animation import FuncAnimation

    colors = ['gold', 'lightcoral', 'yellowgreen']
    explode = (0.01, 0.01, 0.01)
    labels = ['Confirmed cases', 'Deaths', 'Recovery']
    nums = get_all_covid_rec(records)
    fig, ax = plt.subplots()

    def update(num):
        ax.clear()
        ax.axis('equal')
        str_num = str(num)
        for x in range(3):
            nums[x] += str_num.count(str(x))
        ax.pie(nums, explode=explode, labels=labels, colors=colors,
               autopct='%1.1f%%', shadow=True, startangle=140)
        ax.set_title('All countries records')

    ani = FuncAnimation(fig, update, frames=range(50), repeat=True)
    plt.show()
    print('')
    pass