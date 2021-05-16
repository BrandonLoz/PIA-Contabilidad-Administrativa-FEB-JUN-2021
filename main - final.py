import sys
import os
import datetime
import time
import math
import pandas as pd
import re
from funciones import *
#from funciones import menuPrincipal, RegEx, validarDatos, validarPregunta, validarDecimales, imprimeBalanceGeneral

def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def validarDatos(_patron,_pregunta="Dame un dato: "):
    global captura
    while True:
        _fxvalor = input(_pregunta)
        coincide = re.search(_patron, _fxvalor)
        if (coincide):
            captura = _fxvalor
            break
        else:
            print("*** El dato no es correcto. Intenta de nuevo. ***")

def validarPregunta(_patron,_pregunta="Dame un dato: "):
    global resultado1
    global resultado2
    while True:
        _fxvalor = input(_pregunta)
        coincide = re.search(_patron, _fxvalor)
        if (coincide):
            resultado1 = int(_fxvalor)
            resultado2 = float(resultado1)
            break
        else:
            print("*** La respuesta no es correcta. Intenta de nuevo. ***")

def validarDecimales(_patron,_pregunta="Dame un dato: "):
    global resultado2
    while True:
        _fxvalor = input(_pregunta)
        coincide = re.search(_patron, _fxvalor)
        if (coincide):
            resultado2 = float(_fxvalor)
            break
        else:
            print("*** La respuesta no es correcta. Intenta de nuevo. ***")

respuesta = 1
exportar = 1
resultado1 = 1
resultado2 = 1.00
fecha_aceptada = False
captura = ""
NOMBREEMPRESA = ""

#Listas elementos
listanombreproduc=list()
listaunidadavender=list()
listaprecioventa=list()
listatotal=list()
listaimportedeventa1=list()
listaimportedeventa2=list()

#Listas inventario
lista_invfinal1=list()
lista_invfinal2=list()
lista_invinicial1=list()
lista_invinicial2=list()
lista_total_unidades1=list()
lista_total_unidades2=list()
lista_unidad_producir=list()
lista_suma_camisas_producir=list()

#Listas materiales
lista_nombre_material=list()
lista_total_materiales=list()
lista_req=list()
lista_total_total_materiales=list()
listamat1=list()
listamat2=list()
compras_totales=list()
lista8_1=list()
lista8_2=list()
listareu=list()
listanom8=list()
lista_importeMOD_1=list()
lista_total_horas_1=list()
lista_importeMOD_2=list()
lista_total_horas_2=list()
lista9_1=list()
lista9_2=list()

#Indices
i = 0
j = 0
k = 0
l = 0
contadorp=1
contadoru=0
contador3=0
contador4=0
contador5=0
contador6=0
contador7=0
contador8=0
contador9=0
contador10=0
contador11=0
contador12=0
contador13=0
contador14=0
contador15=0
contador16=0
contador17=0
contador18=0
contador19=0
contador20=0
contador21=0
contador22=1
contador23=0
contador24=0
contador26=0
contador27=0
contador28=0
indice=0

while (True):
    menuPrincipal()
    opcion = input(f"¿Qué opción deseas?: ")
    respuesta = 1
    if RegEx(opcion,"^[1234xX]{1}$"):
        if opcion=="x" or opcion=="X":
            print("\nGracias por utilizar el programa.\n")
            print("\t\t\t\t*** PIA - PRESUPUESTO MAESTRO ***       ")
            print("\t\t\t\t Contabilidad Equipo 2      \n")
            break
        if opcion=="1":
            while respuesta == 1:
                print("\t\t\t\t [1] Presupuesto de Operación.")
                print(f"\n*** Llena completamente la primera parte, Presupuesto de Operación. ***\n")
                NOMBREEMPRESA = (input("Nombre de la Empresa/Fabrica: ").upper())
                NOMBREEMPRESA.upper()
                validarPregunta(r"^[1-9]{1}[0-9]{0,}$",f"Dime el primer año: ")
                primerAño = resultado1
                validarPregunta(r"^[1-9]{1}[0-9]{0,}$",f"Dime el segundo año: ")
                segundoAño = resultado1

                #Cédula 1
                print("_"*80)
                print(f"\n\t\t\t\t 1.Presupuesto de Ventas.")
                print(f"\nLlena los siguientes datos que se piden.\n")
                validarPregunta(r"^[1-9]{1}[0-9]{0,}$",f"Teclea cuántos productos son: ")
                productocon = resultado1

                print(f"\nIngresa los nombres de los productos.")
                for producto in range(productocon):
                    validarDatos(r"^[A-Z ÁÉÍÓÚÜÑ]{1,40}$", f"Nombre del Producto {contadorp}: ")
                    nombre = captura
                    listanombreproduc.append(nombre)
                    contadorp += 1

                print(f"\nLLena lo siguiente para cada producto.")
                for producto in listanombreproduc:
                    unidadavender=int(input(f"\nUnidades a vender del producto {listanombreproduc[contadoru]} del primer semestre: "))
                    listaunidadavender.append(unidadavender)
                    preciodeventa=float(input(f"Precio de venta del producto {listanombreproduc[contadoru]} del primer semestre: "))
                    listaprecioventa.append(preciodeventa)

                    listaimportedeventa1.append(unidadavender*preciodeventa)
                    unidadavender2=int(input(f"\nUnidades a vender del producto {listanombreproduc[contadoru]} del segundo semestre: "))
                    listaunidadavender.append(unidadavender2)
                    preciodeventa2=float(input(f"Precio de venta del producto {listanombreproduc[contadoru]} del segundo semestre: "))
                    listaprecioventa.append(preciodeventa2)

                    listaimportedeventa2.append(unidadavender2*preciodeventa2)
                    contadoru+=1

                i = 0
                j = 0
                k = 0
                print(f"\nVista resumen del Presupuesto de Ventas")
                print("_"*80)
                print(f"\t\t\t\t1er. Semestre\t\t2do. Semestre")
                print("_"*80)
                for nombre in listanombreproduc:
                    j = i + 1

                    print(f"\nProducto {nombre}")
                    print(f"Unidades a vender:\t\t {listaunidadavender[i]}\t\t\t {listaunidadavender[j]} ")
                    print(f"Precio de venta:\t\t {listaprecioventa[i]}\t\t\t {listaprecioventa[j]} ")
                    print(f"Importe de venta:\t\t {listaimportedeventa1[k]}\t\t {listaimportedeventa2[k]}")
                    i+=2
                    j+=1
                    k+=1
                totalventasS1=(sum(listaimportedeventa1))
                totalventasS2=(sum(listaimportedeventa2))
                VENTASTOTALES=(totalventasS1+totalventasS2)

                print(f"\nTotal de Ventas por Semestre:\t {totalventasS1}\t\t {totalventasS2}")
                print(f"Total de Ventas del {segundoAño}:\t{VENTASTOTALES}")
                #Final Cédula 1

                #Cédula 2
                print("_"*80)
                print(f"\t\t\t\t 2.Determinación del Saldo de Clientes y Flujo de Entradas")
                print(f"\nLlena los siguientes datos que se piden.\n")

                saldoCliente=float(input(f"\nDime el saldo de Clientes del Balance General del año {primerAño}: "))
                totalCliente=(saldoCliente+VENTASTOTALES)

                print("\n*** Ingresa los porcentajes de cobranza. ***")
                validarDecimales(r"^[0-9]+([.][0-9]+)?$",f"Porcentaje de cobranza del {primerAño} (Formato 100.0): ")
                porcentaje_cobranza_1er = resultado2
                validarDecimales(r"^[0-9]+([.][0-9]+)?$",f"Porcentaje de cobranza del {segundoAño} (Formato 100.0): ")
                porcentaje_cobranza_2do = resultado2

                cobranza_año_1er = float(saldoCliente * (porcentaje_cobranza_1er/100))
                cobranza_año_2do = float(VENTASTOTALES * (porcentaje_cobranza_2do/100))
                totalEntradas=(cobranza_año_1er+cobranza_año_2do)

                SALDODECLIENTES=(totalCliente-totalEntradas)

                print(f"\nVista resumen del Presupuesto de Ventas")
                print("_"*80)
                print("\t\t\t\t\tImporte\t\t Total")
                print(f"Saldo de Clientes del 31-Dic-{primerAño}:\t\t\t {saldoCliente}")
                print(f"Ventas del {segundoAño}:\t\t\t\t\t{VENTASTOTALES}")
                print(f"Total de Clientes del {segundoAño}:\t\t\t\t {totalCliente}\n")

                print(f"Entradas de Efectivo:")
                print(f"Por cobranza del {primerAño}:\t\t\t {cobranza_año_1er}")
                print(f"Por cobranza del {segundoAño}:\t\t\t {cobranza_año_2do}")
                print(f"Total de Entradas del {segundoAño}:\t\t\t\t {totalEntradas}\n")

                print(f"Saldo de Clientes del {segundoAño}:\t\t\t\t {SALDODECLIENTES}")
                #Final Cédula 2

                #Cédula 3
                #Presupuesto de Producción
                print("_"*80)
                print(f"\t\t\t\t 3.Presupuesto de Producción")
                print(f"\nLlena los siguientes datos que se piden.")

                for producto in listanombreproduc:
                    print(f"\nPrimer Semestre:")
                    inv_final_1=float(input(f"Dime el inventario final de {producto} del primer semestre: "))
                    lista_invfinal1.append(inv_final_1)

                    total_unidades1 = listaunidadavender[contador6] + lista_invfinal1[contador7]
                    lista_total_unidades1.append(total_unidades1)

                    inv_inicial_1=float(input(f"Dime el inventario inicial de {producto} del primer semestre: "))

                    lista_invinicial1.append(inv_inicial_1)
                    lista_unidad_producir.append(total_unidades1-inv_inicial_1)

                    contador8=contador8+1

                    print(f"\nSegundo Semestre:")
                    inv_final_2=float(input(f"Dime el inventario final de {producto} del segundo semestre: "))
                    lista_invfinal2.append(inv_final_2)

                    contador6=contador6+1

                    total_unidades2 = listaunidadavender[contador6] + lista_invfinal2[contador7]
                    lista_total_unidades2.append(total_unidades2)

                    inv_inicial_2=(lista_invfinal1[indice])
                    indice+=1
                    lista_invinicial2.append(inv_inicial_2)
                    lista_unidad_producir.append(total_unidades2-inv_inicial_2)

                    x=lista_unidad_producir[contador9]
                    contador9=contador9+1
                    y=lista_unidad_producir[contador9]
                    total=(x+y)
                    lista_suma_camisas_producir.append(total)

                    contador5+=1
                    contador6+=1
                    contador7+=1
                    contador8+=1
                    contador9+=1
                    contador10+=1

                i = 0
                k = 0
                l = 0
                print(f"\n\t\t\t\t 1er Semestre\t\t 2do Semestre")
                for elemento in listanombreproduc:
                    j = k + 1

                    print(f"\nProducto {elemento}:")
                    print(f"Unidades a vender:\t\t {listaunidadavender[k]}\t\t\t {listaunidadavender[j]} ")
                    print(f"(+) Inventario final:\t\t {lista_invfinal1[i]}\t\t {lista_invfinal2[i]}")
                    print(f"(=) Total de unidades:\t\t {lista_total_unidades1[i]}\t\t {lista_total_unidades2[i]}")
                    print(f"(-) Inventario inicial:\t\t {lista_invinicial1[i]}\t\t {lista_invinicial2[i]}")
                    print(f"(=) Unidades a Producir:\t {lista_unidad_producir[k]}\t\t {lista_unidad_producir[j]}")

                    i+=1
                    j+=1
                    k+=2

                #Cédula 4
                print("_"*80)
                print(f"\t\t\t\t 4.Presupuesto de Requerimiento de Materiales.")
                print(f"\nLlena los siguientes datos que se piden.")

                x=lista_unidad_producir[contador12]
                contador12+=1
                y=lista_unidad_producir[contador12]
                suma=(x+y)

                i = 1
                cuantos=int(input(f"\n¿Cuántos materiales tienes por producto?: "))
                print(f"\nIngresa los nombres de los materiales.")
                for material in range(cuantos):
                    material=input(f"Dime el nombre del material {i}: ")
                    lista_nombre_material.append(material)
                    i += 1
                i = 0

                #SEMESTRE 1
                for producto in listanombreproduc:
                    print(f"\t\t\t\t\t 1er. Semestre\t\t\t2do Semestre")
                    print(f"{producto}:")

                    print(f"\nUnidades a producir: {lista_unidad_producir[contador21]}")
                    contador13=0
                    contador16=0
                    for material in lista_nombre_material:
                        print(f"Material {material}:")
                        for req in range(1):
                            #print(producto)

                            requerimientoM=float(input(f"Dime el requerimiento de Material {material}: ")) #Quitar {material} y M minuscula
                            lista_req.append(requerimientoM)

                        x=(lista_unidad_producir[contador21]*lista_req[contador15])
                        lista_total_materiales.append(x)
                        print(f"Requerimiento de material: {lista_req[contador14]}")
                        print(f"Total de Material {lista_nombre_material[contador16]}: {lista_total_materiales[contador17]}\n")
                        listamat1.append(x)

                        contador13+=1
                        contador14+=1
                        contador15+=1
                        contador16+=1
                        contador17+=1
                    contador21 =contador21+2

                #SEMESTRE 2
                contador25=1
                contador14=0
                contador15=0
                contador17=0
                lista_total_materiales=[]
                for producto in listanombreproduc:
                    print(f"2do. Semestre")
                    print(f"{producto}:")

                    print(f"\nUnidades a producir:{lista_unidad_producir[contador25]}\n")

                    contador13=0
                    contador16=0
                    for material in lista_nombre_material:
                        print(f"Material {material}:")

                        x=(lista_unidad_producir[contador25]*lista_req[contador15])
                        lista_total_materiales.append(x)
                        print(f"Requerimiento de material:{lista_req[contador14]}\n")
                        print(f"Total de Material {material}: {lista_total_materiales[contador17]}\n")
                        listamat2.append(x)

                        contador13+=1
                        contador14+=1
                        contador15+=1
                        contador16+=1
                        contador17+=1
                    contador25=contador25+2


                listaMateriales=[]
                materialA1=sum(listamat1[0::3])
                listaMateriales.append(materialA1)
                materialB1=sum(listamat1[1::3])
                listaMateriales.append(materialB1)
                materialC1=sum(listamat1[2::3])
                listaMateriales.append(materialC1)
                materialA2=sum(listamat2[0::3])
                listaMateriales.append(materialA2)
                materialB2=sum(listamat2[1::3])
                listaMateriales.append(materialB2)
                materialC2=sum(listamat2[2::3])
                listaMateriales.append(materialC2)

                print(f"Total de Requerimientos: ")
                print(f"\t\t\t1er. Semestre\t\t2do. Semestre\t\t\tTotal {segundoAño}")

                materialAT=(materialA1+materialA2)
                materialBT=(materialB1+materialB2)
                materialCT=(materialC1+materialC2)

                print(f"Material A:\t\t {materialA1}\t\t{materialA2}\t\t\t{materialAT}")
                print(f"Material B:\t\t {materialB1}\t\t{materialB2}\t\t\t{materialBT}")
                print(f"Material C:\t\t {materialC1}\t\t{materialC2}\t\t{materialCT}\n")
                #Final Cédula 4

                #Cédula 5
                #Semestre 1
                print("_"*80)
                print(f"\t\t\t\t 5.Presupuesto de Compras de Materiales")
                print(f"\nLlena los siguientes datos que se piden.")
                for material in lista_nombre_material:
                    print(f"\n1er. Semestre:")

                    print(f"Material {material}: ")                    
                    inventarioFinal=int(input(f"\nDime el Inventario Final {material}: "))
                    listareu.append(inventarioFinal)                    
                    total_materiales=(listaMateriales[contador23]+inventarioFinal)                    
                    inventarioInicial=int(input(f"Dime el Inventario Inicial {material}: "))                    
                    material_comprar=(total_materiales-inventarioInicial)                    
                    precio_compra=float(input(f"Dime el precio de compra {material}: "))
                    total_material=(material_comprar * precio_compra)
                    compras_totales.append(total_material)                    
                                        
                    print(f"\nRequerimiento de Materiales: {listaMateriales[contador23]}")
                    print(f"Inventario Final: {inventarioFinal}")
                    print(f"Total de Materiales: {total_materiales}")
                    print(f"Inventario Inicial: {inventarioInicial}")
                    print(f"Material a Comprar: {material_comprar}")
                    print(f"Precio de Compra: {precio_compra}")
                    print(f"Total de Material {material} en $: {total_material}\n")

                    contador23+=1

                print("_"*60)
                print(f"Compras Totales del 1er. Semestre: {sum(compras_totales)}\n")

                #Semestre 2
                listapreciocompra=[]
                for material in lista_nombre_material:
                    print(f"2do. Semestre")
                    
                    print(f"Material {material}: ")
                    inventarioFinal=int(input(f"\nDime el inventario Final {material}:  "))
                    total_materiales=(listaMateriales[contador23]+inventarioFinal)
                    inventarioInicial=(listareu[contador24])
                    contador24+=1
                    material_comprar=(total_materiales-inventarioInicial)
                    precio_compra=float(input(f"Dime el precio de compra {material}: "))
                    listapreciocompra.append(precio_compra)
                    total_material=(material_comprar*precio_compra)
                    compras_totales.append(total_material)
                    
                    print(f"\nRequerimiento de Materiales: {listaMateriales[contador23]}")                    
                    print(f"Inventario Final: {inventarioFinal}")                
                    print(f"Total de Materiales: {total_materiales}")
                    print(f"Inventario Inicial: {inventarioInicial}")                
                    print(f"Material a Comprar: {material_comprar}")                   
                    print(f"Precio de Compra: {precio_compra}")    
                    print(f"Total de Material {material} en $: {total_material}\n")

                    contador23+=1

                print("_"*60)
                print(f"Compras Totales del 2do Semestre: {sum(compras_totales[3::1])}")
                print(f"Total del {segundoAño}: {sum(compras_totales)}\n")
                #Final Cédula 5

                #Cédula 6
                print("_"*80)
                print(f"\t\t\t\t 6.Determinación del saldo de Proveedores y Flujo de Salidas")
                print(f"\nLlena los siguientes datos que se piden.")

                saldo_proveedores= float(input(f"\nDime el saldo de los proveedores {primerAño}: "))
                
                print("\n*** Ingresa los porcentajes de proveedores. ***")
                validarDecimales(r"^[0-9]+([.][0-9]+)?$",f"Porcentaje de proveedores del {primerAño} (Formato 100.0): ")
                porcentaje_proveedores_1er = resultado2
                validarDecimales(r"^[0-9]+([.][0-9]+)?$",f"Porcentaje de proveedores del {segundoAño} (Formato 100.0): ")
                porcentaje_proveedores_2do = resultado2
                compras_totales_suma=sum(compras_totales)
                total_proveedores= (saldo_proveedores+ (compras_totales_suma))
                por_proveedores1 = (saldo_proveedores*(porcentaje_proveedores_1er/100))
                por_proveedores2 = (compras_totales_suma*(porcentaje_proveedores_2do/100))
                total_salidas= (por_proveedores1 + por_proveedores2)
                saldo_proveedores_totales= (total_proveedores - total_salidas)
                
                print(f"\nSaldo de los proveedores {primerAño}:\t\t\t {saldo_proveedores}")            
                print(f"Compras del {segundoAño}:\t\t\t\t {compras_totales_suma}")                
                print(f"Total de Proveedores del {segundoAño}:\t\t\t\t\t {total_proveedores}")
                
                print(f"\nSalidas de Efectivo:")           
                print(f"Por provedores del {primerAño}:\t\t\t {por_proveedores1}")
                print(f"Por provedores del {segundoAño}:\t\t\t {por_proveedores2}")                
                print(f"Total de Salidas {segundoAño}:\t\t\t\t\t {total_salidas}")                

                print(f"\nSaldo de Proveedores del {segundoAño}:\t\t\t\t\t {saldo_proveedores_totales}\n")
                #Final Cédula 6

                #Cédula 7
                print("_"*80)
                print(f"\t\t\t\t 7.Presupuesto de Mano de Obra Directa")
                print(f"\nLlena los siguientes datos que se piden.\n")

                listaHorasReq=[]
                for valor in (listanombreproduc):
                    print(f"Primer Semestre para {valor}:")
                    
                    h_requeridas= float(input(f"\n¿Cuántas horas son requeridas por unidad?: "))
                    listaHorasReq.append(h_requeridas)                    
                    u_producir=(lista_unidad_producir[contador27])
                    cuota_hora= float(input(f"Cuota por hora: "))
                    total_horas= (u_producir*h_requeridas)
                    lista_total_horas_1.append(total_horas)
                    importe_MOD= (total_horas*cuota_hora)
                    
                    print(f"\nUnidades a producir: {u_producir}\n")
                    print(f"Horas requeridas por Unidad: {h_requeridas}")
                    print(f"Total de horas requeridas por unidad: {total_horas}")
                    print(f"Cuota por hora: {cuota_hora}")
                    print(f"Importe de M.O.D: {importe_MOD}\n")

                    lista_importeMOD_1.append(importe_MOD)
                    T_horas_semestre_1= sum(lista_total_horas_1)
                    Total_MOD1= sum(lista_importeMOD_1)
                    
                    contador27= contador27+2
                print(f"Total de Horas requiridas del 1er. Semestre: {T_horas_semestre_1}")
                print(f"Total M.O.D. del 1er. Semestre: {Total_MOD1}\n")
                print(f"------------------------------------------------")

                contador28=1
                contador29=0
                for valor in (listanombreproduc):

                    print(f"Segundo Semestre para {valor}:")

                    u_producir2=(lista_unidad_producir[contador28])
                    h_requeridas2=(listaHorasReq[contador29])                   
                    cuota_hora2= float(input(f"Cuota por hora: "))
                    total_horas2=(u_producir2*h_requeridas2)
                    lista_total_horas_2.append(total_horas2)
                    importe_MOD2= (total_horas2*cuota_hora2)
                    
                    print(f"Unidades a producir: {u_producir2}")                    
                    print(f"Horas requeridas por Unidad: {h_requeridas2}")
                    print(f"Total de horas requeridas por unidad: {total_horas2}")
                    print(f"Cuota por hora: {cuota_hora2}")
                    print(f"Importe de M.O.D: {importe_MOD2}\n")

                    lista_importeMOD_2.append(importe_MOD2)
                    T_horas_semestre_2= sum(lista_total_horas_2)
                    Total_MOD2= sum(lista_importeMOD_2)

                    contador28=contador28+2
                    contador29+=1

                print(f"Total de Horas requiridas del 2do. Semestre:: {T_horas_semestre_2}")
                print(f"Total M.O.D. del 2do. Semestre: {Total_MOD2}\n")

                T_H_Requeridas= T_horas_semestre_1 + T_horas_semestre_2
                T_MOD_porSemestre= Total_MOD1+Total_MOD2
                
                print(f"------------------------------------------------")
                print(f"Total de Horas requeridas del {segundoAño}: {T_H_Requeridas}")
                print(f"Total de M.O.D. del {segundoAño}: {T_MOD_porSemestre}\n")
                #Final Cedula 7

                #Cédula 8
                print("_"*80)
                print(f"\t\t\t\t 8.Presupuesto de Gastos Indirectos de Fabricación")
                print(f"\nLlena los siguientes datos que se piden.\n")

                print(f"PRIMER SEMESTRE:")
                depreciacion=float(input(f"Dime tu Depreciacion Total: "))
                divdep=(depreciacion/2)
                lista8_1.append(divdep)
                lista8_2.append(divdep)
                
                seguro=float(input(f"Dime tu Seguro Total: "))
                divseg=(seguro/2)
                lista8_1.append(divseg)
                lista8_2.append(divseg)
                
                print(f"Depreciacion: {divdep}")
                print(f"Seguro: {divseg}")

                opcion=input(f"Tu mantenimiento se divide en partes iguales semestrales (1-Si / 0-No): ")
                if opcion=="1":
                    mantenimiento=float(input(f"Dime tu Manteniminieto Total: "))
                    divmant=(mantenimiento/2)
                    lista8_1.append(divmant)
                    lista8_2.append(divmant)
                    print(f"Mantenimiento: {divmant}")
                else:
                    mantenimiento1=float(input(f"Dime tu Mantenimiento Del Primer Semestre: "))
                    lista8_1.append(mantenimiento1)
                    print(f"Mantenimiento: {mantenimiento1}")
                    mantenimiento2=float(input(f"Dime tu Mantenimiento Del Segundo Semestre: "))
                    lista8_2.append(mantenimiento2)

                opcion=input(f"Tu Energetico se divide en partes iguales semestrales (1-Si / 0-No): ")
                if opcion=="1":
                    energetico=float(input(f"Dime tu Energetico Total: "))
                    divener=(energetico/2)
                    lista8_1.append(divener)
                    lista8_2.append(divener)
                    print(f"Energetico: {divener}")
                else:
                    energetico1=float(input(f"Dime tu Energetico Del Primer Semestre: "))
                    lista8_1.append(energetico1)
                    print(f"Energetico: {energetico1}")
                    energetico2=float(input(f"Dime tu Energetico Del Segundo Semestre: "))
                    lista8_2.append(energetico2)

                varios=float(input(f"Dime tu Gastos Varios Total: "))
                divva=(varios/2)
                lista8_1.append(divva)
                lista8_2.append(divva)
                print(f"Varios: {divva}")
                totalGIF=(sum(lista8_1))
                print(f"Total G.I.F. del Primer Semestre: {totalGIF}")

                print(f"Segundo Semestre:")

                listanom8=["Depreciacion: ","Seguro: ","Mantenimiento: ","Energetico: ","Varios: "]
                
                for elemento in listanom8:
                    print(f"{elemento}: {lista8_2[contador26]}")
                    contador26=contador26+1
                totalGIF2=(sum(lista8_2))
                print(f"Total G.I.F. del Segundo Semestre: {totalGIF2}")

                TOTALGIF=(totalGIF+totalGIF2)

                print(f"\nCoeficiente para determinar el costo por hora de Gastos Indirectos de Fabricacion")
                print(f"Total G.I.F. del {segundoAño} $: {TOTALGIF}")
                print(f"(/) Total horas M.O.D. Anual: {T_H_Requeridas}")
                x=(TOTALGIF/T_H_Requeridas)
                z=round(x,2)
                costoH_GIF=(z)
                print(f"(=) Costo por Hora de G.I.F. $: {costoH_GIF}\n")
                #Final Cédula 8

                #Cédula 9
                contador26=0
                print(f"\t\t\t\t 9.Gastos de Administración y Ventas:")
                print(f"\nLlena los siguientes datos que se piden.\n")

                print(f"1er Semestre:\n")
                depreciacion2=float(input(f"Dime tu Depreciación Total: "))
                divdep=(depreciacion2/2)
                lista9_1.append(divdep)
                lista9_2.append(divdep)
                
                sueldo_salarios=float(input(f"Dime tu Sueldo y Salarios Total: "))
                divsue=(sueldo_salarios/2)
                lista9_1.append(divsue)
                lista9_2.append(divsue)
                
                comision=float(input(f"Dime la Comisión de Ventas Proyectadas (Formato 100.0): "))
                resultadoco1=(totalventasS1*(comision/100))
                resultadoco2=(totalventasS2*(comision/100))
                lista9_1.append(resultadoco1)
                lista9_2.append(resultadoco2)
                
                print(f"Depreciacion: {divdep}")
                print(f"Saldos y Salarios: {divsue}")
                print(f"Comisiones: {resultadoco1}")

                opcion=input(f"Tus varios se divide en partes iguales semestrales (1-Si / 0-No): ")
                if opcion=="1":
                    vario=float(input(f"Dime tu Varios Total: "))
                    divva1=(divva1/2)
                    lista9_1.append(divva1)
                    lista9_2.append(divva1)
                    print(f"Varios: {divva1}")
                else:
                    vario1=float(input(f"Dime tu Varios del Primer Semestre: "))
                    lista9_1.append(vario1)
                    print(f"Varios: {vario1}")
                    vario2=float(input(f"Dime tu Varios del Segundo Semestre: "))
                    lista9_2.append(vario2)

                intereses=float(input(f"Dime los intereses por prestamo Total: "))
                divi=(intereses/2)
                lista9_1.append(divi)
                lista9_2.append(divi)
                print(f"Intereses por obligaciones: {divi}")

                totalGIF3=(sum(lista9_1))
                totalGIF4=(sum(lista9_2))
                print(f"Total G.I.F. del 1er. Semestre: {totalGIF3}")

                print(f"\n2do. Semestre:")
                listanom9=["Depreciacion: ","Sueldos y Salarios: ","Comisiones: ","Varios: ","Intereses por prestamo: "]
                for elemento in listanom9:
                    print(f"{elemento}: {lista9_2[contador26]}")
                    contador26=contador26+1
        
                TOTALGIFF=(totalGIF3+totalGIF4)
                print(f"Total G.I.F. 2do. Semestre: {totalGIF4}")
                print(f"Total de Gastos de Operacion: {TOTALGIFF}\n")
                #Final Cédula 9

                #Cédula 10
                lista_costo_unitario=[]
                contador=0
                contador1=0
                contador2=0
                contador3=3

                print("_"*80)
                print(f"\t\t\t\t 10.Determinación del Costo Unitario de Productos Terminados")
                print(f"\nLlena los siguientes datos que se piden.\n")
                
                lista_costo_unitario=[]
                lista_nueva=[]
                listaCUT=[]

                contador=0
                contador1=0
                contador2=0
                contador3=3
                contador4=0

                for valor in (listanombreproduc):
                    contador1=0
                    print(f"Producto {valor}:")

                    lista_nueva=[]

                    mano_obra=float(input(f"\n¿Cuánto es de mano de obra?: "))
                    resultado3= mano_obra*listaHorasReq[contador4]

                    v_GIF= float(input(f"¿Cuánto es de GIF?: "))
                    resultado4= v_GIF*listaHorasReq[contador4]

                    contador4+=1

                    x,y,z=(lista_req[contador2:contador3])
                    lista_nueva.append(x)
                    lista_nueva.append(y)
                    lista_nueva.append(z)
                    for cantidad in (lista_nueva):
                        lista_costo_unitario.append(listapreciocompra[contador1]*cantidad)
                        contador1+=1

                    lista_costo_unitario.append(resultado3)
                    lista_costo_unitario.append(resultado4)

                    COSTOUF=(sum(lista_costo_unitario))
                    listaCUT.append(COSTOUF)
                    print(f"Costo Unitario Final: {COSTOUF}\n")
                    lista_costo_unitario=[]
                    contador2=contador2+3
                    contador3=contador3+3
                    contador+=1
                #Final Cédula 10

                #Cédula 11
                print(f"\t\t\t\t 11.Valuación de Inventarios Finales\n")
                print(f"\nLlena los siguientes datos que se piden.\n")
                
                lista_total_material=[]
                lista_costo_total=[]
                lista_unidades=[]
                lista_c_unitario=[]
                lista_inventario=[]
                contador5=0
                contador6=0

                for material in lista_nombre_material:
                    print(f"Material: {lista_nombre_material[contador5]}")
                    total_material= float(input(f"Dime el total de material {lista_nombre_material[contador5]}: "))
                    lista_total_material.append(total_material)
                    lista_costo_total.append( lista_total_material[contador5]*listapreciocompra[contador5])
                    contador5+=1
                total_CU=sum(lista_costo_total)

                print(f"Inventario Final de Materiales: {total_CU}\n")

                for nombres in (listanombreproduc):
                    print(f"Producto: {listanombreproduc[contador6]}")

                    unidades_producto= float(input(f"Total de unidades de {listanombreproduc[contador6]}: "))
                    lista_unidades.append(unidades_producto)

                    c_unitario_total= float(input(f"Dime el costo unitario total de {listanombreproduc[contador6]}: "))
                    lista_c_unitario.append(c_unitario_total)

                    v_inventario=(lista_unidades[contador6]*lista_c_unitario[contador6])
                    lista_inventario.append(v_inventario)
                    contador6+=1
                inv_final_terminado=sum(lista_inventario)


                print(f"Inventario Final de Producto Terminado: {inv_final_terminado}\n")
                #Final Cédula 11
                break
        elif opcion=="2":
            while True:
                print("\t\t\t\t [2] Presupuesto Financiero.")
                print(f"\n*** Llena completamente la segunda parte, Presupuesto Financiero. ***\n")
                menuPptoFinanciero()
                opcion = input("*** Elige el siguiente Estado Financiero para continuar: ")
                respuesta = 1
                exportar = 1
                if RegEx(opcion,"^[12345]{1}$"):
                    if opcion == "1":
                        #Edo de Costo de Producción y Ventas
                        print(f"\n** Complemente los datos para la elaboración del Edo de Costo de Producción y Ventas. **")

                        saldoI=float(input(f"\nDime el Saldo Inicial de Materiales: "))
                        inventarioI_terminados=float(input(f"Dime tu Inventario Inicial de Productos Terminados: "))

                        print(f"\n\t\t\t\t{NOMBREEMPRESA}")
                        print(f"\t\t\t Estado de Costo de Producción y Ventas")
                        print(f"\t\t Presupuesto del 1 de Enero al 31 de Diciembre del {segundoAño}")

                        compras_materiales=(sum(compras_totales))
                        Material_d=(saldoI+compras_materiales)
                        inventarioF=(total_CU)
                        materialU=(Material_d-inventarioF)
                        manodo=(T_MOD_porSemestre)
                        gfi=(TOTALGIF)
                        COSTOPRO=(materialU+manodo+gfi)
                        TOTAL_PRO_DIS=(COSTOPRO+inventarioI_terminados)
                        inventarioF_terminados=(inv_final_terminado)
                        COSTOVENTAS=(TOTAL_PRO_DIS-inventarioF_terminados)

                        print(f"Saldo Incial de Materiales:\t\t\t\t {saldoI}")
                        print(f"(+) Compras de Materiales:\t\t\t\t {compras_materiales}")
                        print(f"(=) Material Disponible:\t\t\t\t {Material_d}")
                        print(f"(-) Inventario Final de Materiales:\t\t\t {inventarioF}")
                        print(f"(=) Materiales Utilizados:\t\t\t\t {materialU}")
                        print(f"(+) Mano de Obra Directa:\t\t\t\t {manodo}")
                        print(f"(+) Gastos de Fabricación Indirectos:\t\t\t {gfi}")
                        print(f"(=) Costo de Producción:\t\t\t\t {COSTOPRO}")
                        print(f"(+) Inventario Inicial de Productos Terminados:\t\t {inventarioI_terminados}")
                        print(f"(=) Total de Producción Disponible:\t\t\t {TOTAL_PRO_DIS}")
                        print(f"(-) Inventario Final de Productos Terminados:\t\t {inventarioF_terminados}")
                        print(f"(=) Costo de Ventas:\t\t\t\t\t {COSTOVENTAS}\n")
                        print("_"*80)

                    elif opcion == "2":
                        #Edo de Resultados
                        print(f"\n** Complemente los datos para la elaboración del Edo de Resultados. **")

                        print(f"\nIngresa los porcentajes de los impuestos (Formato 100.0).")
                        porcentaje=(float(input(f"Porcentaje de ISR: ")))
                        porcentaje2=float(input(f"Porcentaje de PTU: "))
                        UB=(VENTASTOTALES-COSTOVENTAS)
                        UO=(UB-TOTALGIFF)
                        ISR=(UO*(porcentaje/100))
                        z=round(ISR,2)
                        PTU=(UO*(porcentaje2/100))
                        x=round(PTU,2)
                        UN=(UO-ISR-PTU)
                        a=round(UN,2)

                        print(f"\t\t\t\t{NOMBREEMPRESA}")
                        print(f"\t\t\t Estado de Resultados")
                        print(f"\t\t Presupuesto del 1 de Enero al 31 de Diciembre del {segundoAño}")

                        print(f"\nVentas:\t\t\t\t\t\t\t {VENTASTOTALES}")
                        print(f"(-) Costo de Ventas:\t\t\t\t\t {COSTOVENTAS}")
                        print(f"(=) Utilidad Bruta:\t\t\t\t\t {UB}")
                        print(f"(-) Gasto de Operación:\t\t\t\t\t {TOTALGIFF}")
                        print(f"(=) Utilidad de Operación de Operación:\t\t\t {UO}")
                        print(f"(-) ISR:\t\t\t\t\t\t {z}")
                        print(f"(-) PTU:\t\t\t\t\t\t {x}")
                        print(f"(=) Utilidad Neta:\t\t\t\t\t {a}")
                        print("_"*80)

                    elif opcion == "3":
                        #Edo de Flujo de Efectivo
                        print(f"\n** Complemente los datos para la elaboración del Edo de Flujo de Efectivo. **")

                        saldo_inicial=float(input(f"\nDime el saldo inicial en Efectivo: "))
                        CAFM=float(input(f"Dime tu Compra de Activo Fijo (Maquinaria): "))
                        PISR=float(input(f"Dime el pago de ISR del {primerAño}: "))
                        PPTU=float(input(f"Dime el pago de PTU del {segundoAño}: "))

                        print(f"\t\t\t\t{NOMBREEMPRESA}")
                        print(f"\t\t\t Estado de Flujo de Efectivo")
                        print(f"\t\t Presupuesto del 1 de Enero al 31 de Diciembre del {segundoAño}")

                        print(f"\nSaldo Inicial de Efectivo:\t\t\t\t {saldo_inicial}")
                        print(f"Entradas:")
                        print(f"Cobranza {segundoAño}:\t\t\t\t\t\t {cobranza_año_2do}")
                        print(f"Cobranza {primerAño}:\t\t\t\t\t\t {cobranza_año_1er}")

                        TE=(cobranza_año_1er+cobranza_año_2do)
                        ED=(saldo_inicial+TE)
                        PGIF=(TOTALGIF-depreciacion)
                        PGO=(TOTALGIFF-depreciacion2)
                        TS=(por_proveedores1+por_proveedores2+T_MOD_porSemestre+PGO+CAFM+PISR+PPTU+PGIF)
                        FEA=(ED-TS)

                        print(f"Total de Entradas:\t\t\t\t\t\t {TE}")
                        print(f"Efectivo Disponible:\t\t\t\t\t\t {ED}")
                        print(f"Salidas:")
                        print(f"Provedores del {primerAño}:\t\t\t\t\t {por_proveedores1}")
                        print(f"Provedores del {segundoAño}:\t\t\t\t\t {por_proveedores2}")
                        print(f"Pago Mano de Obra Directa:\t\t\t\t {T_MOD_porSemestre}")
                        print(f"Pago Gastos Indirectos de Fabricación:\t\t\t {PGIF}")
                        print(f"Pago de Gastos de Operación:\t\t\t\t {PGO}")
                        print(f"Compra de Activo Fijo (Maquinaria):\t\t\t {CAFM}")
                        print(f"Pago ISR {primerAño}:\t\t\t\t\t\t {PISR}")
                        print(f"Pago PTU {primerAño}:\t\t\t\t\t\t {PPTU}")
                        print(f"Total Salidas:\t\t\t\t\t\t\t {TS}\n")
                        print(f"Flujo De Efectivo Actual:\t\t\t\t\t {FEA}")
                        print("_"*80)

                    elif opcion == "4":
                        #Balance General
                        print(f"\n** Complemente los datos para la elaboración del Balance General. **")

                        DD=float(input(f"\nDime los Deudores Diversos: "))
                        FYE=float(input(f"Dime los Funcionarios y Empleados: "))
                        TAC=(FEA+SALDODECLIENTES+FYE+DD+total_CU+inv_final_terminado)

                        terreno=float(input(f"Dime el Terreno: "))
                        plantaye=float(input(f"Dime la Planta y Equipo: "))
                        PYE=(plantaye+CAFM)
                        depreciaciona=float(input(f"Dime la Depreciación Acumulada: "))
                        DA=(-(depreciaciona+depreciacion+depreciacion2))
                        TANC=(terreno+PYE+DA)
                        AT=(TAC+TANC)
                        documentospa=float(input(f"Dime los Documentos por Pagar: "))
                        TPCP=(saldo_proveedores_totales+documentospa+z+x)
                        obligacionporpagar=float(input(f"Dime tus Obligaciones por pagar: "))
                        TPLP=(obligacionporpagar)
                        PT=(TPCP+TPLP)
                        capaportado=float(input(f"Dime tu Capital Aportado: "))
                        capganado=float(input(f"Dime tu Capital Ganado: "))
                        TCC=(capaportado+capganado+a)
                        SUMAPYC=(PT+TCC)
                        resultadofinal=(AT-SUMAPYC)

                        print(f"\t\t\t\t{NOMBREEMPRESA}")
                        print(f"\t\t\t\t Balance General")
                        print(f"\t\t\ Presupuesto del 1 de Enero al 31 de Diciembre del {segundoAño}")

                        print(f"\t\t\tACTIVO")
                        print(f"Activo Circulante")
                        print(f"Efectivo:\t\t\t\t\t {FEA}")
                        print(f"Clientes:\t\t\t\t\t {SALDODECLIENTES}")
                        print(f"Deudores Diversos:\t\t\t\t\t {DD}")
                        print(f"Funcionarios y Empleados:\t\t\t {FYE}")
                        print(f"Inventario de Materiales:\t\t\t {total_CU}")
                        print(f"Inventario de Producto terminado:\t\t {inv_final_terminado}")
                        print(f"Total de Activos Circulantes:\t\t\t\t\t {TAC}")

                        print(f"\nActivo No Circulante")
                        print(f"Terreno:\t\t\t\t\t {terreno}")
                        print(f"Planta y Equipo:\t\t\t\t {PYE}")
                        print(f"Depreciacion Acumulada:\t\t\t\t {DA}")
                        print(f"Total Activos No Circulantes:\t\t\t\t\t {TANC}")

                        print(f"\nACTIVO TOTAL:\t\t\t\t\t\t\t {AT}")

                        print(f"\nPASIVO")
                        print(f"Pasivo Corto Plazo")
                        print(f"Proveedores:\t\t\t\t\t {saldo_proveedores_totales}")
                        print(f"Documentos por Pagar:\t\t\t\t {documentospa}")
                        print(f"ISR por Pagar:\t\t\t\t\t {z}")
                        print(f"PTU por Pagar:\t\t\t\t\t {x}")
                        print(f"Total de Pasivo Corto Plazo:\t\t\t\t\t {TPCP}")
                        print(f"\nPasivo Largo Plazo")
                        print(f"Obligaciones por pagar:\t\t\t\t {obligacionporpagar}")
                        print(f"Total de Pasivo Largo Plazo:\t\t\t {obligacionporpagar}")

                        print(f"\nPASIVO TOTAL:\t\t\t\t\t {PT}")

                        print(f"\nCAPITAL CONTABLE")
                        print(f"Capital Aportado:\t\t\t\t {capaportado}")
                        print(f"Capital Ganado:\t\t\t\t\t {capganado}")
                        print(f"Utlidad del Ejercicio:\t\t\t\t {a}")
                        print(f"Total de Capital Contable:\t\t\t\t\t {TCC}")

                        print(f"\nSUMA DE PASIVO Y CAPITAL:\t\t\t\t\t {SUMAPYC}")

                        print("_"*80)
                        print(f"\t\t\t\t COMPROBACIÓN: PASIVO + CAPITAL = ACTIVO")
                        print(f"\t\t\t\t\t {PT}   +  {TCC}  =  {AT}")
                        print(f"\t\t\t\t\t {SUMAPYC} = {AT} ")
                        print(f"COMPROBACIÓN:\t\t\t\t {SUMAPYC-AT}")
                        print("_"*80)

                    elif opcion == "5":
                        #print("Regresando al Menú Principal")
                        break
                    else:
                        print("*** No has pulsado ninguna opción correcta. Intenta de nuevo. ***")
                else:
                    print("\n*** Esa respuesta no es válida. Intenta de nuevo. ***")

        else:
            print ("\n*** No has pulsado ninguna opción correcta. Intenta de nuevo. ***")
    else:
        print("\n*** Esa respuesta no es válida. Intenta de nuevo. ***")