import Tarefa2 as t2
import numpy as np
import time
import Parte3 as p3

def CriaW(lista):
	tempo=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
	for ndig in lista:
		for dig in range(10):
			for p in [5,10,15]:
				t=time.time()
				A = np.loadtxt("dados_mnist/train_dig" + str(dig) + ".txt")
				A = A/255
				Wd=t2.fatoracaoWH(A,p)
				np.save("W" + str(dig) + "p" + str(p), Wd)

				print("W" + str(dig) + "p" + str(p)) #controle do console
				print(time.time()-t)


				tempo[[5,10,15].index(p)][dig]=time.time()-t #dados para análise


		np.savetxt("tempoCria.csv",np.array(tempo), delimiter=",") #salva matriz de tempo

def TestaW():
	tempos=[]
	for p in [5,10,15]:       #Análise de acertos
		print("Resultados para p = " + str(p) + " são: ")
		tempo = time.time()
		A = np.loadtxt("dados_mnist/test_images.txt")
		b = np.loadtxt("dados_mnist/test_index.txt")
		Digitos, Frequencia = p3.Calcular_acertos(A, b, p)
		for j in range(10):
			tempos.append(Frequencia[j][3])
			print("A frequencia de acertos para o dígito "+str(j)+" é:",Frequencia[j][3],"%")
		print("Tempo da parte 3: ", time.time() - tempo)
		tempos.append(time.time() - tempo)
		tempos.append(0)
	np.savetxt("tempoTesta".csv",np.array(tempos), delimiter=",") #salva matriz de tempo
