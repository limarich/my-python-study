import GUI_Convercao as gc
class Conversor:
    def __init__(self, entrada, base, nova_base):
        self.string = entrada
        self.base = base
        self.nova_base = nova_base
    def converter_decimal(self):
        decimal = 0
        c = 0
        self.string = self.string.lower()
        for x in range(len(self.string)-1, -1, -1):
            if self.string[x].isalpha():
                v = ord(self.string[x]) - 87
                decimal = decimal + v * pow(self.base, c)
            else:
                decimal = decimal + int(self.string[x]) * pow(self.base, c)
            c += 1
        self.decimal = decimal
    def converter_nova_base(self):
        caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                      'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y', 'Z']
        saida = ''
        while True:
            aux = self.decimal % self.nova_base
            saida = saida + caracteres[aux]
            self.decimal = self.decimal//self.nova_base
            if self.nova_base > self.decimal:
                aux = self.decimal % self.nova_base
                saida = saida + caracteres[aux]
                break
        self.saida = saida
if __name__ == '__main__':
    Janela = gc.TelaPy()
    valor = base1 = base2 = 0
    while True:
        Janela.iniciar_Tela(valor, base1, base2)
        valor = str(valor)
        conversor = Conversor(Janela.values['valor'], int(Janela.values['base1']), int(Janela.values['base2']))
        conversor.converter_decimal()
        conversor.converter_nova_base()
        print(conversor.saida[::-1])