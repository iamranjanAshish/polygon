import numpy as np
import matplotlib.pyplot as plt
import argparse

plt.style.use('fivethirtyeight')
parser = argparse.ArgumentParser()

parser.add_argument('-sides', type=int)
args = parser.parse_args()

alpha = np.linspace(0,2*np.pi,747) # Circular Angle

def polygon(sides):

    # Check
    if sides < 3:
        if sides < 0:
            raise ValueError('Sides cannot be negative')
        else:
            raise ValueError('Number of sides must at least be 3')
        
    # Parameters & Variables
    initial_x = -1.0
    x_values = []
    y_values = []
    internal_angle = ((sides-2)*180/sides)
    internal_angle_rd = np.deg2rad(internal_angle)
    theta = internal_angle_rd/2
    delta_theta = internal_angle_rd/(sides - 2)
    new_theta = internal_angle_rd/2

    # Intersection Calculator
    def intersection(x):
        while x < 1:
            if (x**2 + (np.tan(new_theta)*(x + 1))**2 - 1) < 0:
                x = x + 1e-5
                if x == 1 or x > 1:
                    x_values.append(1)
                    y_values.append(0)
                    break
            elif -25e-6 <= (x**2 + (np.tan(new_theta)*(x + 1))**2 - 1) <= 25e-6:
                x_values.append(x)
                y_values.append(np.tan(new_theta)*(x + 1))
                x = x + 1e-5
            else:
                break
        return None

    # Rotation Loop
    while theta + new_theta > 1e-3:
        intersection(initial_x)
        new_theta = new_theta - delta_theta
        if theta + new_theta < 1e-3:
            intersection(initial_x)
            
    # Return
    return x_values,y_values,sides

#----------------------------------------------------------------------------------------------------

x_cor, y_cor, sides = polygon(args.sides) # polygon(Sides)

#----------------------------------------------------------------------------------------------------

# Processing
cleaned_x_cor = []
cleaned_y_cor = []
for i in range(len(x_cor)):
    if x_cor[i] != -1:
        cleaned_x_cor.append(x_cor[i])
    elif i == 0:
        cleaned_x_cor.append(x_cor[i])
for i in range(len(y_cor)):
    if y_cor[i] != 0:
        cleaned_y_cor.append(y_cor[i])
    else:
        if i != len(y_cor)-1 and i != len(y_cor)-2:
            if y_cor[i] == 0 and y_cor[i+1] == 0 and y_cor[i+2] == 0:
                cleaned_y_cor.append(y_cor[i])
            elif i == 0:
                cleaned_y_cor.append(y_cor[i])
final_segment_x = -1
final_segment_y = 0
cleaned_x_cor.append(final_segment_x)
cleaned_y_cor.append(final_segment_y)

# Polygon
plt.figure(figsize=[18,8])

plt.subplot(1,2,1)

plt.axhline(0, color = '#00b894', linewidth = 1)
plt.axvline(0, color = '#00b894', linewidth = 1)
plt.xlim(-1.1,1.1)
plt.ylim([-1.1,1.1])
plt.plot(np.cos(alpha), np.sin(alpha), color = '#6c5ce7', linewidth = 1)
plt.plot(cleaned_x_cor,cleaned_y_cor, linewidth = 0.8, color='#636e72')
plt.grid(False)

if sides > 16:
    plt.subplot(1,2,2)

    plt.axhline(0, color = '#00b894', linewidth = 1)
    plt.axvline(0, color = '#00b894', linewidth = 1)
    if 17 <= sides <= 33:
        plt.xlim(-1.013,-(0.987)**sides)
        plt.ylim([-0.03,(0.95)**sides])
    else:
        plt.xlim(-1.007,-(0.9937)**sides)
        plt.ylim([-0.03,(0.98)**sides])
    plt.plot(np.cos(alpha), np.sin(alpha), color = '#6c5ce7', linewidth = 1.7)
    plt.plot(cleaned_x_cor,cleaned_y_cor, linewidth = 1.7, color='#636e72')
    plt.grid(False)

plt.show()
