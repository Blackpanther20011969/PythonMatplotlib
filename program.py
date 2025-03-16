import matplotlib.pyplot as plt

# Umsatzdaten für 2020 und 2021
revenue_2020 = [6436, 2355, 5533, 6334, 5332, 5466, 7576, 4356, 3256, 2356, 2545, 5255]
revenue_2021 = [3542, 5243, 5121, 7321, 9511, 5541, 8851, 3574, 4215, 5678, 8422, 7512]

# Monate des Jahres
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Stil für das Diagramm festlegen
plt.style.use('ggplot')

# Diagramm erstellen
fig, ax = plt.subplots()

# Monate als x-Achse festlegen
ax.set_xticks(month)
ax.plot(month, revenue_2020, label="2020")
ax.plot(month, revenue_2021, label="2021")

# Legende hinzufügen
plt.legend()

# Titel und Achsenbeschriftungen hinzufügen
ax.set_title("Revenue by month")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue in €")

# Diagramm anzeigen
plt.show()