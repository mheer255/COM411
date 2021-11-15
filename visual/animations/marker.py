import matplotlib.pyplot as plt
import matplotlib.animation as animation

line = None

def animate(frame):
  global line
  line.set_data(frame, frame)

def run():
  global line
  fig, ax = plt.subplots()
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 10)
  line, = ax.plot([], [], 'ro')
  simple_animation = animation.FuncAnimation( fig, animate, frames = 10, interval = 1000)
  plt.show()

run()