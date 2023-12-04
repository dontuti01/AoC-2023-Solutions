from collections import defaultdict

#01

archivo=open("texto.txt","r")
suma=0
for linea in archivo:
  cont=-1
  si=False
  carta,numeros=linea.strip().split(":")
  tengo,suerte=numeros.strip().split("|")
  tengo=tengo.strip().split(" ")
  suerte=suerte.strip().split(" ")
  for id,i in enumerate(tengo):
    if i=="":
      del tengo[id]
  for id,i in enumerate(suerte):
    if i=="":
      del suerte[id]
  for i in suerte:   
    for j in tengo:
      if i==j:

        cont+=1
        si=True
  if si:
    suma+=2**cont
  else:
    suma+=0
print(suma)
#02

archivo=open("texto.txt","r")
cartas = defaultdict(int)

archivo=open("texto.txt","r")

for i, linea in enumerate(archivo):
    _, linea = linea.split(": ")
    tengo,suerte = map(str.split, linea.split(" | "))
    contador = sum(suerte.count(w) for w in tengo)
    cartas[i] += 1
    for j in range(i + 1, i + contador + 1):
        cartas[j] += cartas[i]
print(sum(cartas.values()))