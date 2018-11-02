import matplotlib.pyplot as plt

a1 = 0.8
a2 = 1.3
x1 = 1
x2 = 1

valores1 = []
valores2 = []

for i in range(100):
    x1 = a1*x1
    x2 = a2*x2
    valores1.append(x1)
    valores2.append(x2)

plt.plot(valores1)
plt.show()

plt.plot(valores2)
plt.show()
