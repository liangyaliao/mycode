#!/usr/bin/env python3

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['silver','gold','platinum','copper']
counts = [100, 90, 20,10]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('precious metal I like ')
ax.set_title('precious metal supply by kind')
ax.legend(title='precious metal kind')

plt.show()

plt.savefig("/home/student/mycode/graphing/precious_metals.png")
    # Save to "~/static"
plt.savefig("/home/student/static/precious_metals.png")
print("Graph created.")
