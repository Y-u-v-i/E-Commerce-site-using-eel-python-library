import eel
eel.init('Gui')
@eel.expose
def App():
    print('Application running successfully!!')
App()
eel.start('index.html')

