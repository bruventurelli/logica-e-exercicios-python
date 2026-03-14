distancia = float(input("Digite uma distância em metros: "))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print(f"A distância de {distancia} corresponde a: {km}km {hm}hm {dam}dam {dm}dm {cm}cm {mm}mm")
