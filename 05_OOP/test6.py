class Car:
    engine_displacement: float = 1.6
    color: str = 'black'


arr = []
Cars = ["Renault Logan 1.6 black",
"Kia Rio 1.6 white",
"Chevrolet Cobalt 2.0 black",
"Skoda Octavia 1.8 black",
"Honda Civic 1.6 black",
"Toyota Camry 2.0 red",
"Peugeo 307 1.6 purple",
"Ford Focus 1.6 white",
"Mazda 3 1.8 black",
"0"]
i = len(Cars) - 1
while i != -1:
    print(Cars[i])
    if str(Car.engine_displacement) in Cars[i] and Car.color in Cars[i]:
        arr.append(Cars[i])
    i -= 1

print('aaa')
for i in arr:
    print(i)