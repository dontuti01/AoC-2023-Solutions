#solucion1
archivo=open("texto.txt", "r")
contador=0
numeros=["one"]
for i in archivo:
  numero=""
  numero2=""
  intento=0
  veces=0
  for cosa in i:
    if cosa.isdigit():
      numero2=cosa
      veces+=1
      if intento==0:
        numero=cosa
        intento+=1
  numero=numero+numero2
  contador+=int(numero)
print(contador)
#solucion2
archivo=open("texto.txt", "r")
contador=0
for i in archivo:
  i=i.replace("oneight","oneeight")
  i=i.replace("threeight","threeeight")
  i=i.replace("nineight","nineeight")
  i=i.replace("twone","twoone")
  i=i.replace("eightwo","eighttwo")
  i=i.replace("eighthree","eightthree")
  i=i.replace("sevenine","sevennine")
  i=i.replace("one","1")
  i=i.replace("two","2")
  i=i.replace("three","3")
  i=i.replace("four","4")
  i=i.replace("five","5")
  i=i.replace("six","6")
  i=i.replace("seven","7")
  i=i.replace("eight","8")
  i=i.replace("nine","9")
  numero=""
  numero2=""
  intento=0
  veces=0
  for cosa in i:
    if cosa.isdigit():
      numero2=cosa
      veces+=1
      if intento==0:
        numero=cosa
        intento+=1
  numero=numero+numero2
  contador+=int(numero)
print(contador)
