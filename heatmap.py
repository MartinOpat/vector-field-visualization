import numpy as np
import plotly.graph_objects as go
from vectorFields import VectorField

# Create a vector field
n = 30  # Adjust grid density for faster rendering
min_val = -10
max_val = 10
vf = VectorField(n, min_val, max_val)

# Set the vector field (Swirl in this case)
# vf.set_radial(strength=1)
# vf.set_swirl(strength=1)
# vf.set_lin_flow(strength=10)
vf.set_turbulent(strength=1)

# Compute the magnitude of the vector field at each point
magnitude = vf.get_field_magnitude()

# Create the volume plot using Plotly
fig = go.Figure(data=go.Volume(
    x=vf.x.flatten(), 
    y=vf.y.flatten(), 
    z=vf.z.flatten(),
    value=magnitude.flatten(),
    opacity=0.2,
    # isomin=np.min(magnitude),
    # isomax=np.max(magnitude),
    colorscale='Jet',
    surface_count=15,
    # caps=dict(x_show=False, y_show=False, z_show=False)
))

# Update layout for the axes and colorbar
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',

        # Corner
        camera=dict(
            eye=dict(x=1.25, y=1.25, z=1.25)
        )

        # Top
        # camera=dict(
        #     eye=dict(x=0, y=0, z=2)
        # )
    ),
    # title="Vector Field Magnitude Volume",
)

# Add red dot at (-8, 8, 5)
fig.add_trace(go.Scatter3d(
    x=[8], y=[-8], z=[5],
    mode='markers',
    marker=dict(size=5, color='green')
))

# Display vector field data at red dot
print("Vector field at (-8, 8, 5):")
vf_at_point = vf.get_field_at_point(8, -8, 5)
print("Magnitude:", vf_at_point[0])
print("Direction:", vf_at_point[1])

# vals:

# Magnitude: 9.474918388989025
# Direction: (np.float64(5.172413793103448), np.float64(-4.482758620689655), np.float64(-6.551724137931034))
# Goes through the y-x plane

# Magnitude: 6.844632152165244
# Direction: (np.float64(4.482758620689655), np.float64(5.172413793103448), np.float64(0.0))
# Goes through the y-z plane

# Magnitude: 10.0
# Direction: (np.float64(10.0), np.float64(0.0), np.float64(0.0))
# Goes through the z-y plane

# Magnitude: 0.4061714941387695
# Direction: (np.float64(0.11883834604086019), np.float64(0.322731711647935), np.float64(0.21609482283939008))
# Goes through the z-y plane

# Show the interactive plot
fig.show()

# Save the plot as a png
fig.write_image("vector_field_magnitude_volume.png")

