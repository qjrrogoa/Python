from controller import Controller
from view import View

controller = Controller()
while True:
    menu=View.showMenu()
    if menu ==9:
        break;
    controller.handleRequest(menu)
controller.close()