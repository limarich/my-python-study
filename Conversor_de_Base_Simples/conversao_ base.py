def converter_decimal(string, base):
    decimal = 0
    c = 0
    string = string.lower()
    for x in range(len(string)-1, -1, -1):
        if string[x].isalpha():
            v = ord(string[x]) - 87
            decimal = decimal + v * pow(base, c)
        else:
            decimal = decimal + int(string[x]) * pow(base, c)
        c += 1
    return decimal
def converter_nova_base(decimal, nova_base):
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                  'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    saida = ''
    while True:
        aux = decimal % nova_base
        saida = saida + caracteres[aux]
        decimal = decimal//nova_base
        if nova_base > decimal:
            aux = decimal % nova_base
            saida = saida + caracteres[aux]
            break
    return saida
if __name__ == '__main__':
    entrada = input("Digite um valor para ser convertido")
    base = int(input("Digite a sua base[2-32]"))
    nova_base = int(input("Digite a nova base[2-32]"))
    decimal = converter_decimal(entrada, base)
    saida = converter_nova_base(decimal, nova_base)
    print(saida[::-1])