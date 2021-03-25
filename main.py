import PySimpleGUI as sg
import os

sg.theme("DarkAmber")


layout = [[sg.Text('500 $', size=(5, 1)),sg.InputText(key='-ccent-')],
          [sg.Text('200 $', size=(5, 1)), sg.InputText(key='-duec-')],
          [sg.Text('100 $', size=(5, 1)), sg.InputText(key='-cent-')],
          [sg.Text('50 $', size=(5, 1)),sg.InputText(key='-cant-')],
          [sg.Text('20 $', size=(5, 1)), sg.InputText(key='-venti-')],
          [sg.Text('10 $', size=(5, 1)), sg.InputText(key='-dieci-')],
          [sg.Button('Calcola')],
          [sg.Text('TOTALE:'), sg.Text(size=(5,1), key='-tot-'),sg.Text(size=(5,1), key='-outduec-'), sg.Text(size=(5,1), key='-outcent-'), sg.Text(size=(5,1), key='-outcant-'), sg.Text(size=(5,1), key='-outventi-'), sg.Text(size=(5,1), key='-outdieci-')]]
          


window=sg.Window("ATM", layout, grab_anywhere=True)

if os.path.exists("File.csv"):
  pass
else:
  file=open("File.csv","x")
  file.close()

while True:
  event, values=window.read()

  print(event, values)

  if event==sg.WIN_CLOSED:
    break

  elif event=="Calcola":
    
    window["-tot-"].update(values["-ccent-"], text_color="red")
    window["-outduec-"].update(values["-duec-"], text_color="red")
    window["-outcent-"].update(values["-cent-"], text_color="red")
    window["-outcant-"].update(values["-cant-"], text_color="red")
    window["-outventi-"].update(values["-venti-"], text_color="red")
    window["-outdieci-"].update(values["-dieci-"], text_color="red")

    file=open("File.csv","a")
    file.write(f'{values["-ccent-"]};{values["-duec-"]};{values["-cent-"]};{values["-cant-"]};{values["-venti-"]};{values["-dieci-"]}\n')
    file.close()

    sg.popup('Soldi ritirati')
  
window.close()
