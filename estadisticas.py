menor = 0
Animal = 0
Entre2y5 =0
Entre5y10 =0
Mayor10 = 0
A =input("Hay un animal en el zoologico? (si/no)").lower()
while A == "si":
  men = int(input("Edad del animal"))
  Animal = Animal+1
  if men<=2:
    menor +=1
  elif men <=5 and men>2:
    Entre2y5=Entre2y5+1
  elif men <=10 and men>5:
    Entre5y10 = Entre5y10+1
  else:
    Mayor10 = Mayor10+1
  A= input("Hay algun otro animal en el zoologico? (si/no) ")
menn = (menor*100)/Animal
menn2y5 = (Entre2y5*100)/Animal
menn5y10 = (Entre5y10*100)/Animal
Mayorr10= (Mayor10*100)/Animal
print("Hay", menor, "Animales con menos de 2 años y representan el", menn, "% del total de animales")
print("Hay", Entre2y5, "Animales entre 2 y 5 años y representan el", menn2y5, "% del total de animales ")
print("Hay", Entre5y10, "Animales entre 5 y 10 años y representan el", menn5y10, "% del total de animales")
print("Hay", Mayor10, "Animales con mas de 10 años y representan el", Mayorr10, "% del total de animales")
  
