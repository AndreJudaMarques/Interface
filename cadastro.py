from PySimpleGUI import PySimpleGUI as sg

# ler layout
sg.theme('Reddit')
layout = [
      [sg.Text('Usuário'), sg.Input(key='usuario')],
      [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
      [sg.Checkbox('Salvar o login?')],
      [sg.Button('Entrar')]
]

#janela
janela = sg.Window('Tela de login', layout, size=(300,120))


#ler eventos
while True:
      eventos, valores = janela.read()
      if eventos == sg.WINDOW_CLOSED:
            break
      
      if eventos == 'Entrar':
            if valores['usuario'] == 'andre' and valores['senha'] == 'bolonhesa123':
                  print(f'Bem Vindo André')
            else:
                  print('Não é o André')