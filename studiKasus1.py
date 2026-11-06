import numpy as np

suhuCelsius = np.array([28.5, 29.0, 27.8, 30.1, 29.5, 28.2, 31.0, 30.5, 29.2, 28.8])

suhuFahrenheit = (suhuCelsius * 9/5) + 32

print("Suhu dalam Celcius   : ", suhuCelsius)
print("Suhu dalam Fahrenheit: ", suhuFahrenheit)