import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
L = 1.0   # Length of the pendulum (m)

# Differential equation for the simple pendulum
def pendulum(t, y):
    theta, omega = y
    dydt = [omega, -(g / L) * np.sin(theta)]
    return dydt

# Initial conditions (angle and angular velocity)
y0 = [np.pi / 4, 0]

# Time span for integration
t_span = [0, 10]  # From t=0 to t=10 seconds

# Solve the differential equation
sol = solve_ivp(pendulum, t_span, y0, t_eval=np.linspace(t_span[0], t_span[1], 1000))

# Plot the angular displacement
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], label="Angle (θ)")
plt.xlabel("Time (s)")
plt.ylabel("Angle (radians)")
plt.title("Simple Pendulum Motion")
plt.grid()
plt.legend()
plt.show()
