import matplotlib.pyplot as plt

def dda_line_drawing(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1
    points = []
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points

def plot_line(points):
    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o', color='blue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('DDA Line Drawing Algorithm')
    plt.grid()
    plt.show()

x1, y1 = map(int, input("Enter the starting point (x1, y1): ").split())
x2, y2 = map(int, input("Enter the ending point (x2, y2): ").split())

points = dda_line_drawing(x1, y1, x2, y2)

plot_line(points)
