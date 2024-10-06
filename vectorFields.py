import numpy as np

class VectorField:
    def __init__(self, n, min_val, max_val):
        self.n = n
        self.min_val = min_val
        self.max_val = max_val

        self.x = np.linspace(min_val, max_val, n)
        self.y = np.linspace(min_val, max_val, n)
        self.z = np.meshgrid(self.x, self.y)
        self.x, self.y, self.z = np.meshgrid(self.x, self.y, self.x)

        self.u = np.zeros((n, n))
        self.v = np.zeros((n, n))
        self.w = np.zeros((n, n))

    def set_radial(self, strength=1):
        self.u = strength * self.x
        self.v = strength * self.y
        self.w = strength * self.z

    def set_swirl(self, strength=1):
        r = np.sqrt(self.x**2 + self.y**2)
        r = np.where(r == 0, 1e-10, r)
        self.u = -strength * self.y / r**1.5
        self.v = strength * self.x / r**1.5
        self.w = np.zeros_like(self.z)

    def set_lin_flow(self, strength=1):
        self.u = np.ones_like(self.z) * strength
        self.v = np.zeros_like(self.z) * strength
        self.w = np.zeros_like(self.z) * strength

    def set_turbulent(self, strength=1):
        self.u = strength * np.random.rand(self.n, self.n, self.n)
        self.v = strength * np.random.rand(self.n, self.n, self.n)
        self.w = strength * np.random.rand(self.n, self.n, self.n)

    def get_field_grid(self):
        return self.x, self.y, self.z
    
    def get_field_values(self):
        return self.u, self.v, self.w
    
    def get_field_magnitude(self):
        return np.sqrt(self.u**2 + self.v**2 + self.w**2)
