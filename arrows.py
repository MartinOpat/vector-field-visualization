from vectorFields import VectorField

# Display the vector field in 3D in an interactive plot using glyphs (arrows)

import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab

# Create a vector field
n = 10
min_val = -10
max_val = 10
vf = VectorField(n, min_val, max_val)

# Set the vector field
# vf.set_radial(strength=1)
# vf.set_swirl(strength=1)
# vf.set_lin_flow(strength=10)
vf.set_turbulent(strength=10)

# Create the plot
fig = mlab.figure(size=(1600, 1200))
quiver = mlab.quiver3d(vf.x, vf.y, vf.z, vf.u, vf.v, vf.w, mode='arrow', scale_factor=0.2, scalars=vf.get_field_magnitude(), color=(0,0,1))

# Add axes with labels and scale, and adjust font size
axes = mlab.axes(quiver, xlabel='X', ylabel='Y', zlabel='Z', color=(0.7, 0.7, 0.7))
axes.label_text_property.font_size = 1  # Smaller font size
axes.title_text_property.font_size = 1  # Smaller font size

# Increase the number of grid lines
axes.axes.x_axis_visibility = True
axes.axes.y_axis_visibility = True
axes.axes.z_axis_visibility = True
axes.axes.number_of_labels = 5  # More detailed grid

# Add red dot at (-8, 8, 5)
mlab.points3d(8, -8, 5, color=(1, 0, 0), scale_factor=0.5)

# Display vector field data at red dot
print("Vector field at (-8, 8, 5):")
vf_at_point = vf.get_field_at_point(8, -8, 5)
print("Magnitude:", vf_at_point[0])
print("Direction:", vf_at_point[1])


# vals:

# Magnitude: 9.622504486493764
# Direction: (np.float64(-5.555555555555555), np.float64(7.777777777777779), np.float64(1.1111111111111107))
# Goes through the edge parallel to z-axis

# Magnitude: 9.558139185602919
# Direction: (np.float64(-7.777777777777779), np.float64(-5.555555555555555), np.float64(0.0))
# Goes through the y-z plane

# Magnitude: 10.0
# Direction: (np.float64(10.0), np.float64(0.0), np.float64(0.0))
# Goes through the z-y plane

# Magnitude: 12.674671572798026
# Direction: (np.float64(9.979850059904724), np.float64(4.002022112211837), np.float64(6.710716152057211))
# Goes through the z-y plane


# Show the plot
mlab.show()