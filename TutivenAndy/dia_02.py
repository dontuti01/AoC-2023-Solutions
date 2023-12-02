#Solucion 1
archivo=open("texto.txt","r")
suma=0
listo=0
for linea in archivo:
  game,elementos=linea.strip().split(":")
  generados=elementos.strip().split(";")
  juego,id=game.split(" ")

  for combinacion in generados:
    nuevo=combinacion.strip().split(",")
    for i in nuevo:
      numero, color=i.strip().split(" ")

      if ((color=="blue" and int(numero)>14) or (color=="red" and int(numero)>12) or (color=="green" and int(numero)>13)) and listo==0:
        listo=1
  if listo==0:
    suma+=int(id)
  listo=0
print(suma)

#Splucion2

archivo=open("texto.txt","r")
suma=0
listo=0
for linea in archivo:
  game,elementos=linea.strip().split(":")
  generados=elementos.strip().split(";")
  juego,id=game.split(" ")
  n_guardadoB=0
  n_guardadoG=0
  n_guardadoR=0
  for combinacion in generados:
    nuevo=combinacion.strip().split(",")
    
    for i in nuevo:
      numero, color=i.strip().split(" ")
      if color=="blue" and int(numero)>n_guardadoB:
        n_guardadoB=int(numero)
      if color=="green" and int(numero)>n_guardadoG:
        n_guardadoG=int(numero)
      if color=="red" and int(numero)>n_guardadoR:
        n_guardadoR=int(numero)
  suma+=n_guardadoB*n_guardadoG*n_guardadoR
  listo=0
print(suma)