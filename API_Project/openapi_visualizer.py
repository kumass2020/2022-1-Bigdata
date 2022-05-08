import matplotlib.pyplot as plt
import numpy as np
import json

plt.style.use('_mpl-gallery')

with open("API_Project/China_2020_202203.json", "r") as json_file:
    data = json.load(json_file)

x = []
y = []

for object in data:
    x.append(object['yyyymm'])
    y.append(object['visit_cnt'])

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(ylim=(0, max(y)), yticks=[0, max(y)*2/4, max(y)*3/4, max(y)],
        xlim=(0, "202203"), xticks=["202001", "202101", "202201"])

plt.show()