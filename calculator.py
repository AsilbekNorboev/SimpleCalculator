
class Calculator:

    def __init__(self, **kwargs):
        self.first_op = kwargs.get('first')
        self.sign = kwargs.get('sign')
        self.second_op = kwargs.get('second')

    def calculate(self):
        if self.sign == '*':
            return float(self.first_op) * float(self.second_op)
        elif self.sign == '-':
            return float(self.first_op) - float(self.second_op)
        elif self.sign == '/':
            if self.second_op=='0':
                print('None Valid Operation')
            else:
                return float(self.first_op)/float(self.second_op)
        elif self.sign == '+':
            return float(self.first_op) + float(self.second_op)
        elif self.sign =='//':
            if self.second_op=='0':
                print('None Valid Operation')
            else:
                return float(self.first_op)//float(self.second_op)
        elif self.sign =='%':
            if self.second_op=='0':
                print('None Valid Operation')
            else:
                return float(self.first_op) % float(self.second_op)

    def validate(self):
        if self.first_op.isdigit() and self.second_op.isdigit():
            if self.sign in ['-', '*', '+', '/', '//', '%']:
                if self.second_op == '0' and self.sign in ['/','//','%']:
                    print('None valid operation (zero error)')
                    return False
                return True
        return False


def main():
    print('Welcome to this simple Calculator program that has the following standard functions: '
          '\n ( - )  ( + ) ( / ) ( * ) ( % ) ( // ) (quit)')
    while (True):
        calc = input("Input in the following way: first, space, sign, space, second operation.\n"
              " Example: 2 + 2\n>").split()
        if calc[0] =='quit':
            print("Thank you for using this calculator! ")
            break
        cal = Calculator(first = calc[0], sign = calc[1], second = calc[2])
        valid = cal.validate()
        if valid:
            result = cal.calculate()
            print(f'{calc[0]} {calc[1]} {calc[2]} = {result:.2f}')
main()