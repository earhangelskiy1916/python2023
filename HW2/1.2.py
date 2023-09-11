bush_quantity = int(input('enter quantity of bushes: '))
berrys = list()
for i in range(bush_quantity):
    berry_quantity =int(input('enter quantity of berrys: '))
    berrys.append(berry_quantity)

max_quantity = list()
for j in range(len(berrys)):
       max_quantity.append(berrys[j-2] + berrys[j-1] + berrys[j])
print(max(max_quantity))