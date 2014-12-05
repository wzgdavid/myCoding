# encoding: utf-8
import matplotlib.pyplot as plt
import random


def price_list(length):
    plist = []
    price = 20.0
    for n in range(length):
        price += random.randint(-10, 10)

        plist.append(price)
    return plist

plt.plot(price_list(1000))
plt.ylabel('some numbers')
plt.show()
