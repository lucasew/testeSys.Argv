# -.- coding: utf-8 -.-
import sys
import os
"""
    Script para testar como o sys.argv é representado de acordo com a linha de comando passada
"""
print "Tipo do valor: ", type(sys.argv)
print "Atributos do valor", dir(sys.argv)

for a in sys.argv:
    print "Valor: ", type(a) , ' ' , a
os.system('pause') #Pausa a execução no final
