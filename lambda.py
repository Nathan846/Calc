from calculator import Calculator
def handler(event,handler):
    x = event['x']
    y = event['y']
    calc = Calculator()
    print('Addition of two numbers is ',calc.add(x,y))
    print('Subraction of two numbers is ',calc.sub(x,y))
    print('Multiplication of two numbers is ',calc.mul(x,y))
    print('Division of two numbers is ',calc.div(x,y))

