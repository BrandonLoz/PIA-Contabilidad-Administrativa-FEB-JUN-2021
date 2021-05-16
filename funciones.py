import sys
import os
import datetime
import time
import math
import pandas as pd
import re
#from main import *

def menuPrincipal():
    print("\n        Menú principal - PRESUPUESTO MAESTRO      ")
    print("   [1] Presupuesto de Operación.")
    print("   [2] Presupuesto Financiero.")
    print("   [x] Salir del programa.")
    print("_______________________________")
    print(" ")

def menuPptoFinanciero():
    print("_______________________________")
    print("\n        Menú - Presupuesto Financiero       ")
    print("   [1] Estado de Costo de Producción y Ventas de Operación.")
    print("   [2] Estado de Resultados.")
    print("   [3] Estado de Flujo de Efectivo.")
    print("   [4] Balance General.")
    print("   [5] Regresar.")
    print("_______________________________")
    print(" ")

def imprimeBalanceGeneral():
    print("")