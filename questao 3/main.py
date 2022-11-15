from stack import minPilha

pilha = minPilha()	# cria um objeto do tipo especial de pilha
pilha.push(2)
pilha.push(4)
print(pilha.top())    		# retorna 4, pois 4 está no topo
print(pilha.getMin()) 		# retorna 2, pois é atualmente o menor valor na pilha
pilha.pop() 
pilha.push(-1)
print(pilha.getMin()) 		# retorna -1, pois é atualmente o menor valor na pilha
print(pilha.data)
