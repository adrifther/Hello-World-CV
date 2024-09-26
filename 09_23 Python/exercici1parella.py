# exercici1 compte enrere (while) i (for)

entrada = "0, 1, 2, 3, 4, 5"
inverted_entrada = ""
for number in entrada:
    inverted_entrada = number + inverted_entrada
print(inverted_entrada)


number = 10

while number > 0:
    number = number - 1
    print(number)