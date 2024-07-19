import csv
import random
import math

trabajadores = [
        {"nombre":"Juan Pérez"},
        {"nombre":"María García"},
        {"nombre":"Carlos López"},
        {"nombre":"Ana Martínez"},
        {"nombre":"Pedro Rodríguez"},
        {"nombre":"Laura Hernández"},
        {"nombre":"Miguel Sánchez"},
        {"nombre":"Isabel Gómez"},
        {"nombre":"Francisco Díaz"},
        {"nombre":"Elena Fernández"}
        ]

def asignar_sueldos_aleatorios():
    for trabajador in trabajadores:
        trabajador['sueldo']=random.randint(300000,2500000)

def clasificar_sueldos():
    sueldo=[]
    contador1=0
    contador2=0
    contador3=0
    for i in trabajadores:
        sueldo.append(i['sueldo'])
    for sueldos in trabajadores:
        if sueldos['sueldo']<800000:
            contador1 +=1
    print("Sueldos menores a $800.000 TOTAL: ",contador1)
    for trabajador in trabajadores:
        if trabajador['sueldo']<800000:
            print(f"Nombre empleado: {trabajador['nombre']},Sueldo: ${trabajador['sueldo']}")
    for sueldos in trabajadores:
        if sueldos['sueldo']>=800000 and sueldos["sueldo"]<=2000000:
            contador2 +=1
    print("Sueldos entre $800.000 y $2.000.000 TOTAL: ",contador2)
    for trabajador in trabajadores:
        if trabajador['sueldo']>=800000 and trabajador["sueldo"]<=2000000:
            print(f"Nombre empleado: {trabajador['nombre']},Sueldo: ${trabajador['sueldo']}")
    for sueldos in trabajadores:
        if sueldos["sueldo"]>2000000:
            contador3 +=1
    print("Sueldos superiores a $2.000.000 TOTAL: ",contador3)
    for trabajador in trabajadores:
        if trabajador["sueldo"]>2000000:
            print(f"Nombre empleado: {trabajador['nombre']},Sueldo: ${trabajador['sueldo']}")
    total=sum(sueldo)
    print("TOTAL SUELDOS: $",total)

def ver_estadísticas():
    sueldo=[]
    for i in trabajadores:
        sueldo.append(i['sueldo'])
    sueldo_max=max(sueldo)
    sueldo_min=min(sueldo)
    sueldo_prom=sum(sueldo)/len(sueldo)
    multi=sueldo[0]*sueldo[1]*sueldo[2]*sueldo[3]*sueldo[4]*sueldo[5]*sueldo[6]*sueldo[7]*sueldo[8]*sueldo[9]
    sueldo_geom=pow(multi,1/10)

    print(f"Sueldo más alto: ${sueldo_max}\nSueldo más bajo: ${sueldo_min}\nPromedio de sueldos: ${sueldo_prom}\nMedia geometrica: ${sueldo_geom}")

def reporte_de_sueldos():
    with open('Reporte de sueldos.csv','w',newline='') as archivo:
        writer=csv.writer(archivo)
        writer.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Líquido"])
        for trabajador in trabajadores:
            descuento_salud=trabajador['sueldo']*0.7
            descuento_afp=trabajador['sueldo']*0.12
            sueldo_liquido=trabajador["sueldo"]-descuento_salud-descuento_afp
            writer.writerow([trabajador['nombre'],trabajador["sueldo"],descuento_salud,descuento_afp,sueldo_liquido])
            print(f"Nombre empleado: {trabajador['nombre']}, Sueldo Base: ${trabajador['sueldo']}, Descuento Salud: ${descuento_salud}, Descuento AFP: ${descuento_afp}, Sueldo Líquido: ${sueldo_liquido}")
        
def salir_del_programa():
    print("Finalizando programa…\nDesarrollado por Sebastian Zanabria\nRUT 19174724-0")

while True:
    print("Menu")
    op=int(input("1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas.\n4. Reporte de sueldos\n5. Salir del programa\nElija una opcion: "))
    if op==1:
        asignar_sueldos_aleatorios()
    elif op==2:
        clasificar_sueldos()
    elif op==3:
        ver_estadísticas()
    elif op==4:
        reporte_de_sueldos()
    elif op==5:
        salir_del_programa()
        break
    else:
        print("favor ingrese una opcion valida")