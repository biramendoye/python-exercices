import math

print('-------------------------------------')
print('Quadratic equation : aX² + bX + c = 0')
print('-------------------------------------')

a = int(input('enter the first coefficient : '))
b = int(input('enter the second coefficient : '))
c = int(input('enter the third coefficient : '))

if a == 0:
    if b == 0:
        if c == 0:
            print(
                f'The equation {a}X² + {b}X + {c} = 0 admits an infinity of solutions')
        else:
            print(
                f'The equation {a}X² + {b}X + {c} = 0 does not admit a solution')
    else:
        x = - (c / b)
        print(
            f'The equation {a}X² + {b}X + {c} = 0 has for solution : {x}')
else:
    delta = b**2 - (4 * a * c)
    if delta == 0:
        x_0 = -b / (2*a)
        print(f'The equation {a}X² + {b}X + {c} = 0 has for solution : {x_0}')
    if delta > 0:
        x_1 = (-b - math.sqrt(delta)) / (2*a)
        x_2 = (-b + math.sqrt(delta)) / (2*a)
        print(
            f'The equation {a}X² + {b}X + {c} = 0 has two solutions : {x_1} & {x_2}')
    if delta < 0:
        print(
            f'The equation {a}X² + {b}X + {c} = 0 admits two complex solutions')
