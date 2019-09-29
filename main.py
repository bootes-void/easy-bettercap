"""
Julian Guillermo Zapata Rugeles
colombia 
2019

script sencillo que ejecuta bettercap con menu de opcion semigrafico
dependencias 
python3 
bettercap
ruby 

pendientes
opcion menu:
  Instalar dependencias usando rubyonrails
  opciones con sslstrip2
  opciones para Hombre en medio personalizables
  instalador independiente 

futuro:
  dependencias graficas
  interfaz grafica con pyqt5 o tkinter




"""
import os
staticmenu=[1,2,3]

def cls():
  os.system("clear")
  
def validinput():
  passcondition=False
  try:
    print("Ingrese su eleccion seguido de Enter")
    intOption=int(input(">>>"))
    if intOption in staticmenu:
      passcondition=True
  except Exception as e:
    print("opcion no valida")
  return intOption

def takecomman(value):
  if value==1:
    os.system("sudo bettercap -X")
    backed=input("Enter para continuar")
    iniziale()
  if value==2:
    os.system("sudo bettercap -X --proxy -P POST")
    backed=input("Enter para continuar")
    iniziale()

  if value==3:
    cls()
    exit()

def iniziale():
  cls()
  print("##################################")
  print("     ACCESO RAPIDO A BETTERCAP ")
  print("##################################")
  print("")
  print("1 para recoleccion pasiva. ")
  print("2 para recoleccion agresiva. ")
  print("3 para salir.")
  print("")
  intRetorno=validinput()
  takecomman(intRetorno)

iniziale()
