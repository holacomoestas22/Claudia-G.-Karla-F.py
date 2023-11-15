o = input("hay otro vendedor? (respuesta si/no) ")
final = 0 
comision_1 =0 


while o.lower() == "si":
  
  n = str(input("dime tu nombre "))
  s = int(input("dime tu salario "))
  v = int(input("dame tu total de ventas "))
  if v < 3500:
    comision_1 = s * .07 
  elif v <= 3500 and v >= 7000:
    comision_1 = s * .1
  elif v > 7000:
    comision_1 = s * .15
  else:
    print("no tengo esa opcion") 
  final = s + comision_1 
  print("el salario total de", n, "es", final)
  o = input("hay otro vendedor? (respuesta si/no) ")
