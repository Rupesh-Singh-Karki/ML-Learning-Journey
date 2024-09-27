#2
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

#   1.Matplotlib Object Oriented Method

# 1.
# # Create Figure (empty canvas)
# fig = plt.figure()

# # Add set of axes to figure
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

# # Plot on that set of axes
# axes.plot(x, y, 'b')
# axes.set_xlabel('Set X Label') # Notice the use of set_ to begin methods
# axes.set_ylabel('Set y Label')
# axes.set_title('Set Title')

# 2.
# Creates blank canvas
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
# Positioned at 10% from the left and bottom of the figure, occupying 80% of the figure's 
# width and height.
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes (graph kai ander graph)
# Positioned within the larger plot, starting 20% from the left and 50% from the bottom,
#  and taking up 40% of the figure's width and 30% of its height.
# //better way of doing subplot
# Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title');

plt.show()