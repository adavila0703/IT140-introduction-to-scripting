'''
Input

The program needs to receive the input of the amount of hours worked possibly options 
to decide the rate of pay. This way the pay is not hard coded into your program

Steps

1. program start and asks for four inputs
    -hours worked
    -regular pay 
    -overtime pay
    -OT starting point
        This is the hours that you need to reach overtime pay. The reason you should have this as an
        input is to eliminate magic numbers. No hardcoding

2. calculation

function calculatePay(options)
    IF overtime_start is None:
        return regular hours * regular pay
    ELSE: 
        CALCULATE regular hours
        CALCULATE overtime hours
        CALCULATE regular pay
        CALCULATE overtime pay
        return regular pay and overtime pay



'''


def calculate_pay(options: dict) -> int:
    if options['ot_start'] == 0:
        return options['regular_pay'] * options['hours_worked']
    else:
        return (options['regular_pay'] * options['ot_start']) + (options['ot_pay'] * (options['hours_worked'] - options['ot_start']))


def main():
    options = {
        'hours_worked': int(input('Hours Worked: ')),
        'ot_start': int(input('OT Start: ')),
        'regular_pay': int(input('Regular Pay: ')),
        'ot_pay': int(input('OT Pay: ')),
    }
    pay = calculate_pay(options)

    print(f'Week payment: {pay}')


if __name__ == '__main__':
    main()
