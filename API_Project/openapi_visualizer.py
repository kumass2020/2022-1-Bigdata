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

ax.set_ylabel('관광객 수')

ax.plot(x, y)

ax.set(ylim=(0, max(y)), yticks=[max(y)/4, max(y)*2/4, max(y)*3/4, max(y)],
        xlim=(0, "202203"), xticks=["202001", "202101", "202201"])

plt.show()