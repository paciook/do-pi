import random
import math as m
from Dots import Dot
from Hilo import Hilo
import threading
import time


def Start(qant):
	CANT_HILOS = 4
	res = []

	for rep in range(100000):
		branchs = []
		ins = 0
		for x in range(CANT_HILOS):
			branchs.append( Hilo( int(qant / CANT_HILOS) ) )
			branchs[x].start()

		for branch in branchs:
			branch.join()
			ins += branch.get_inside()
		
		res.append(Do_pi(ins, qant))
		print(int(100*rep/100000), "%")

	# print(res)
	print(sum(res) / float(len(res)))

def Do_pi(ins, total):

	return (4*ins/float(total))

def main():

	print("¿Con cuantos puntos querés que calcule?")

	QANT_DOTS = int(input())

	Start(QANT_DOTS)

main()
