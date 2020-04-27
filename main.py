import PySimpleGUI as sg
from cpf import isCpfValid

class Tela:

    def __init__(self):
        sg.change_look_and_feel('Black')
        #   (left, right),(top, bottom)
        l = [(130,1),(1,1)]
        v = [(100,1),(1,1)]

        # layout
        lay = [
            [sg.Text('Ex: "123.456.789-00"', justification='right', pad=(l))],
            [sg.Text('CPF:'), sg.InputText(key='cpf')],
            [sg.Button('Check', key='checker'), sg.Text(' '*20, key='validador', pad=(v))],
        ]

        self.jan = sg.Window('CPF Checker').layout(lay)

    def iniciar(self):
        while 1:
            self.btn, self.values = self.jan.Read()

            CPF = self.values['cpf']

            if self.btn == 'checker':
                print('\n** CLICK')
                print(f'\n** CPF:\n** {CPF}')

                if isCpfValid(CPF):
                    self.jan['validador'].update('CPF válido!', text_color='green')
                else:
                    self.jan['validador'].update('CPF inválido!', text_color='red')

            if self.btn is None:
                break

##    def verdade(self):
##        btn = sg('CPF válido!', text_color='green')
##        return btn
##
##    def falso(self):
##        btn = sg('CPF inválido!', text_color='red')
##        return btn


def main():
    app = Tela()
    app.iniciar()


# programa principal
if __name__ == '__main__':
    main()
