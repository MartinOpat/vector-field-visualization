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
# vf.set_swirl(strength=10)
vf.set_lin_flow(strength=10)
# vf.set_turbulent(strength=1)

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
    ),
    title="Vector Field Magnitude Volume",
)

# Show the interactive plot
fig.show()
