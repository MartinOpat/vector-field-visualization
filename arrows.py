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

# Show the plot
mlab.show()