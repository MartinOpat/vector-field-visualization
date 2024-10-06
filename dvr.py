from vectorFields import VectorField
from mayavi import mlab
import numpy as np

# Create a vector field
n = 10
min_val = -10
max_val = 10
vf = VectorField(n, min_val, max_val)


# Set the vector field
vf.set_radial(strength=1)
# vf.set_swirl(strength=1)
# vf.set_lin_flow(strength=1)
# vf.set_turbulent(strength=1)

# Create the dvr plot
magnitude = vf.get_field_magnitude()
fig = mlab.figure(size=(1600, 1200))
src = mlab.pipeline.scalar_field(magnitude)
vol = mlab.pipeline.volume(src, vmin=0, vmax=max(1, np.max(magnitude)))
mlab.colorbar(title='Magnitude', orientation='vertical')
mlab.view(azimuth=45, elevation=60, distance=15)

# Add axes with labels and scale, and adjust font size
axes = mlab.axes(vol, xlabel='X', ylabel='Y', zlabel='Z', color=(0.7, 0.7, 0.7))
axes.label_text_property.font_size = 2  # Smaller font size
axes.title_text_property.font_size = 4  # Smaller font size

# Increase the number of grid lines
axes.axes.x_axis_visibility = True
axes.axes.y_axis_visibility = True
axes.axes.z_axis_visibility = True
# axes.axes.number_of_labels = 0  # More detailed grid

# Add red dot at (-8, 8, 5)
mlab.points3d(9, 2, 6, color=(1, 0, 0), scale_factor=0.5)

# Show the plot
mlab.show()