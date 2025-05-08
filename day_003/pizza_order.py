print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese ? Y or N: ")

bill=0
# Definir o preço com base no tamanho
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

# Adicionar custo do pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Adicionar custo do queijo extra
if extra_cheese == "Y":
    bill += 1

# Exibir o valor final da conta
print(f"Your final bill is: ${bill}.")
