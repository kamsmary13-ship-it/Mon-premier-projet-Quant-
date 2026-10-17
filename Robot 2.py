# ROBOT 2 - MARY V2
from sklearn.linear_model import LinearRegression

prix = [1800, 1820, 1810, 1850, 1840, 1860, 1890, 1900, 1920, 1950]
X = [[p] for p in prix[:-1]]
y = prix[1:]

model = LinearRegression()
model.fit(X, y)

prix_auj = prix[-1]
prix_demain = int(model.predict([[prix_auj]])[0])

temp = prix_auj
for k in range(7):
    temp = model.predict([[temp]])[0]
prix_semaine = int(temp)

print(f"Demain: {prix_demain} F")
print(f"Semaine: {prix_semaine} F")
