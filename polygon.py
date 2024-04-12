import numpy as np
import matplotlib.pyplot as plt

circle_theta = np.linspace(0,2*3.14,747)

# Main Function

def polygon(sides):

    # Parameters & Variables

    initial_x = -1.0
    x_values = []
    y_values = []
    internal_angle = ((sides-2)*180/sides)
    internal_angle_rd = np.deg2rad(internal_angle)
    theta = internal_angle_rd/2
    delta_theta = internal_angle_rd/(sides - 2)
    new_theta = internal_angle_rd/2

    # Tools

    def intersection(x):
        while x != 1 or x < 1:
            if (x**2 + (np.tan(new_theta)*(x + 1))**2 - 1) < 0:
                x = x + 0.00001
                if x == 1 or x > 1:
                    x_values.append(1)
                    y_values.append(0)
                    break
            elif -0.000025 <= (x**2 + (np.tan(new_theta)*(x + 1))**2 - 1) <= 0.000025:
                x_values.append(x)
                y_values.append(np.tan(new_theta)*(x + 1))
                x = x + 0.00001
            else:
                break
        return None

    # Actual Function

    while theta + new_theta > 0.001:
        intersection(initial_x)
        new_theta = new_theta - delta_theta
        if theta + new_theta < 0.001:
            intersection(initial_x)
    # Return

    return x_values,y_values,sides

# ___________________________________________________________________________________________________
#----------------------------------------------------------------------------------------------------

x_cor, y_cor, sides = polygon(7) # you may add the number of sides over here, polygon(sides)

#____________________________________________________________________________________________________ 
#----------------------------------------------------------------------------------------------------

# Cleaning & Arranging

cleaned_x_cor = []
cleaned_y_cor = []
for i in range(len(x_cor)):
    if x_cor[i] != -1:
        cleaned_x_cor.append(x_cor[i])
    else:
        if i == 0:
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
plt.plot(np.cos(circle_theta), np.sin(circle_theta), color = '#6c5ce7', linewidth = 1)
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
    plt.plot(np.cos(circle_theta), np.sin(circle_theta), color = '#6c5ce7', linewidth = 1.7)
    plt.plot(cleaned_x_cor,cleaned_y_cor, linewidth = 1.7, color='#636e72')
    plt.grid(False)

plt.style.use('fivethirtyeight')
plt.show()

# Optional Section

# You may use the code below, if you want the triangular division of sides
# -- c means the statement was already a comment, not part of the actual code

# Repetition of Elements -- c

# repetition_no = 2
# cleaned_x_center = list(np.repeat(cleaned_x_cor,repetition_no))
# cleaned_y_center = list(np.repeat(cleaned_y_cor,repetition_no))

# Coordinates of Triangles -- c

# for i in range(3*len(cleaned_x_cor)):
#     if i != len(cleaned_x_center)-1:
#         if cleaned_x_center[i] == cleaned_x_center[i+1]:
#             if i >= 2:
#                 if cleaned_x_center[i] != cleaned_x_center[i-2]:
#                     cleaned_x_center.insert(i+1,0)
#                     cleaned_y_center.insert(i+1,0)     
#     else:
#         break

# Polygon with Triangular Division -- c

# plt.figure(figsize=[18,8])

# plt.subplot(1,2,1)

# plt.xlim(-1.1,1.1)
# plt.ylim([-1.1,1.1])
# plt.plot(np.cos(circle_theta), np.sin(circle_theta), color = '#6c5ce7', linewidth = 1)
# plt.plot(cleaned_x_center,cleaned_y_center, linewidth = 0.8, color='#636e72')
# plt.axhline(0, color = '#a29bfe', linewidth = 3)
# plt.axvline(0, color = '#a29bfe', linewidth = 3)
# plt.grid(False)

# if sides > 16:
#     plt.subplot(1,2,2)

#     plt.axhline(0, color = '#81ecec', linewidth = 0.5)
#     plt.axvline(0, color = '#81ecec', linewidth = 0.5)
#     if 17 <= sides <= 33:
#         plt.xlim(-1.013,-(0.987)**sides)
#         plt.ylim([-0.03,(0.95)**sides])
#     else:
#         plt.xlim(-1.007,-(0.9937)**sides)
#         plt.ylim([-0.03,(0.98)**sides])
#     plt.plot(np.cos(circle_theta), np.sin(circle_theta), color = '#6c5ce7', linewidth = 1.7)
#     plt.plot(cleaned_x_center,cleaned_y_center, linewidth = 1.7, color='#636e72')
#     plt.grid(False)

# plt.style.use('fivethirtyeight')
# plt.show()
