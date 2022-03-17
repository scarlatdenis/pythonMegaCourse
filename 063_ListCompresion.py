temps = [223, 226, 233, 265]

new_temps = []

for i in temps:
    new_temps.append(i / 10)

print(new_temps)

# another way

new_temps2 = [i / 10 for i in temps]
print(new_temps2)
