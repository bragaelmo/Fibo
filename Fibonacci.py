numero = int(input("Digite um número inteiro para a sequencia Fibonacci: "));

def fibonacci(n):
    # Verifica se o número é menor ou igual a 1
    if n <= 1:
        return n
    
    # Caso contrário, calcula a sequência de Fibonacci recursivamente
    return fibonacci(n-1) + fibonacci(n-2)
	
	# Imprime os primeiros 10 termos da sequência de Fibonacci
print("Sequencia")
for i in range(numero):
    print(fibonacci(i))