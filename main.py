import matplotlib.pyplot as plt

def suite_fibonacci (n):
    F0 , F1 = 0 , 1
    if n <= 1:
        return n
    else:
        return  suite_fibonacci(n-1) + suite_fibonacci(n-2)

nbr_rep = int(input("Entrez le nombre de répétitions : "))
y = []
for i in range(nbr_rep):
    y.append(suite_fibonacci(i))

phi = y[-1]/y[-2]
print(f"Nombre d'or : {phi} \navec les termes {y[-1]} et {y[-2]} sur {nbr_rep} répétitions")

plt.plot(y)
plt.title("Suite de Fibonacci")
plt.xlabel(r'$\mathrm{x}$')
plt.ylabel(r"$F(\mathrm{x})$")
plt.show()