import numpy as np
import plotly.graph_objects as go
from vectorFields import VectorField  # Assuming this is your custom class

# Create a vector field
n = 50  # Adjust grid density as needed
min_val = -10
max_val = 10
vf = VectorField(n, min_val, max_val)

# Set the vector field (Swirl, Turbulent, or any other)
# vf.set_radial(strength=1)
# vf.set_swirl(strength=1)
# vf.set_lin_flow(strength=10)
vf.set_turbulent(strength=1)

# Generate the vector components and magnitude
X, Y, Z = vf.x, vf.y, vf.z
U, V, W = vf.u, vf.v, vf.w

# Compute the magnitude of the vector field for coloring the tubes
magnitude = np.sqrt(U**2 + V**2 + W**2)

# Define seeding points for the streamlines
# We'll seed across a grid within the field to get more streamlines
seed_x, seed_y, seed_z = np.meshgrid(np.linspace(min_val + 2, max_val - 2, 10),
                                     np.linspace(min_val + 2, max_val - 2, 10),
                                     np.linspace(min_val + 2, max_val - 2, 10))

# Flatten the seed arrays to pass them to the Streamtube plot
seed_x = seed_x.flatten()
seed_y = seed_y.flatten()
seed_z = seed_z.flatten()

# Create a Streamtube plot
fig = go.Figure(data=go.Streamtube(
    x=X.flatten(), y=Y.flatten(), z=Z.flatten(),
    u=U.flatten(), v=V.flatten(), w=W.flatten(),
    starts=dict(x=seed_x, y=seed_y, z=seed_z),
    colorscale='Viridis',
    cmin=magnitude.min(),
    cmax=magnitude.max(),
    sizeref=0.3,
    showscale=True,
    colorbar=dict(title='Magnitude'),
    maxdisplayed=100
))

# Customize the layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis',

        # Corner
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.5)
        )

        # Top
        # camera=dict(
        #     eye=dict(x=0, y=0, z=2)
        # )
    ),
    # title="3D Vector Field Visualization with Streamtubes (Magnitude Coloring)"
)

# Add red dot at (-8, 8, 5)
fig.add_trace(go.Scatter3d(
    x=[8], y=[-8], z=[5],
    mode='markers',
    marker=dict(size=5, color='red')
))

# Show the interactive plot
fig.show()

# Save the plot as a png
fig.write_image("vector_field_magnitude_volume.png")
