import serial
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Initialize serial communication with Arduino
ser = serial.Serial('COM3', 9600)  # Change COM port as needed

# Read data from Arduino
def read_data():
    data = ser.readline().decode().strip()
    return int(data)

# Main loop
if __name__ == "__main__":
    try:
        pendulum_data = []
        while True:
            value = read_data()
            pendulum_data.append(value)
            

    except KeyboardInterrupt:
        ser.close()
        print("Data collection stopped.")

    # Save pendulum data to a CSV file
    with open("pendulum_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Time", "Potentiometer Value"])
        for t, value in enumerate(pendulum_data):
            writer.writerow([t, value])

    # Plot the pendulum motion and save as an image
    time = np.arange(len(pendulum_data))
    plt.plot(time, pendulum_data)
    plt.xlabel("Time")
    plt.ylabel("Potentiometer Value")
    plt.title("Pendulum Motion")
    plt.grid()
    plt.savefig("pendulum_motion_plot.png")  # Save the plot as an image
    plt.show()

    print("Data saved to pendulum_data.csv")
    print("Plot saved as pendulum_motion_plot.png")



