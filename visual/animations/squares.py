import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
boxes = []

def init():
  global boxes
  boxes.append({'x': [3, 3, 4, 4, 3], 'y': [3, 4, 4, 3, 3]})
  boxes.append({'x': [2, 2, 5, 5, 2], 'y': [2, 5, 5, 2, 2]})
  boxes.append({'x': [1, 1, 6, 6, 1], 'y': [1, 6, 6, 1, 1]})

def animate(frame):
  global boxes, ax
  box_index = frame % 3
  ax.set_xlim(0, 7)
  ax.set_ylim(0, 7)
  ax.plot(boxes[box_index]['x'], boxes[box_index]['y'])

def run():
  global fig
  squares_animation = animation.FuncAnimation(fig,
                                              animate,
                                              frames = 3,
                                              interval = 1000,
                                              init_func = init)
  plt.show()

run()