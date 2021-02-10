from calculator import Calculator
def handler(event,handler):
    x = event['x']
    y = event['y']
    print('Addition of two numbers is ',Calculator.add(x,y))

