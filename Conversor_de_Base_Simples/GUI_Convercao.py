import PySimpleGUI as sg

class TelaPy:
    #escolhendo um tema
    sg.change_look_and_feel('DarkGreen1')
    def __init__(self):
    #Iniciando layout
        layout = [
            [sg.Text('Escreva um valor: ', size=(15, 0)), sg.Input(key='valor', size=(15, 0))],
            [sg.Text('Sua base: ', size=(15,0)), sg.Input(key='base1', size=(15,0))],
            [sg.Text('Nova base: ', size=(15,0)), sg.Input(key='base2', size=(15,0))],
            [sg.Text('Valor da conversao:',size=(15,0)), sg.Output(size=(15, 10))],
            [sg.Button('Enviar')]
        ]
    #Configurando a Janela
        self.janela = sg.Window('Conversor de bases').layout(layout)
#Extraindo as informacoes
    def iniciar_Tela(self, valor, base1, base2):
        # while True:
            self.button, self.values = self.janela.Read()
            valor = self.values['valor']
            base1 = self.values['base1']
            base2 = self.values['base2']
            # print(f'Valor: {valor}'
            #       f'\nBase 1: {base1}\n'
            #       f'Base 2: {base2}')
if __name__ == '__main__':
    tela = TelaPy()
    valor = base1 = base2 = 0
    tela.iniciar_Tela(valor, base1, base2)