from vectorFields import VectorField
from mayavi import mlab
import numpy as np

# Create a vector field
n = 10
min_val = -10
max_val = 10
vf = VectorField(n, min_val, max_val)


# Set the vector field
# vf.set_radial(strength=1)
# vf.set_swirl(strength=1)
# vf.set_lin_flow(strength=1)
vf.set_turbulent(strength=1)

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

# Add red dot at (9, 2, 6)
mlab.points3d(9, 2, 6, color=(1, 0, 0), scale_factor=0.5)

# Display vector field data at red dot
print("Vector field at (9, 2, 6):")
vf_at_point = vf.get_field_at_point(9, 2, 6)
print("Magnitude:", vf_at_point[0])
print("Direction:", vf_at_point[1])

# vals:

# Magnitude: 11.915339216404009
# Direction: (np.float64(-5.555555555555555), np.float64(10.0), np.float64(3.333333333333334))
# Goes through the x-y plane

# Magnitude: 11.439589045541112
# Direction: (np.float64(-10.0), np.float64(-5.555555555555555), np.float64(0.0))
# Goes through the y-z plane

# Magnitude: 1.0
# Direction: (np.float64(1.0), np.float64(0.0), np.float64(0.0))
# Goes through the y-z plane

# Magnitude: 0.819129798231796
# Direction: (np.float64(0.23417802337228433), np.float64(0.7457266977658984), np.float64(0.24500198358356462))
# Goes through the x-z plane


# Show the plot
mlab.show()