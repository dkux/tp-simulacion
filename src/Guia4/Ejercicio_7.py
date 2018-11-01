import matplotlib.pyplot as plt

a = 0.5
b = -0.5
c = 1
d = 1

x = 1
y = 1

valores_x = []
valores_y = []

for i in range(100):
    x_tem = a*x+b*y
    y_tem = c*x+d*y
    x = x_tem
    y = y_tem
    valores_x.append(x)
    valores_y.append(y)

plt.plot(valores_x, valores_y)
plt.show()
