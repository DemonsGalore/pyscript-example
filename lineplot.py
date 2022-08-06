import matplotlib.pyplot as plt

fig, ax = plt.subplots()

year = [2016, 2017, 2018, 2019, 2020, 2021]
population_1 = [4, 8, 15, 16, 23, 42]
population_2 = [6, 3, 10, 22, 31, 49]

plt.plot(year, population_1, marker="o", linestyle="--", color="g", label="Country 1")
plt.plot(year, population_2, marker="d", linestyle="-", color="r", label="Country 2")

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Year vs Population")
plt.legend(loc="lower right")

fig
