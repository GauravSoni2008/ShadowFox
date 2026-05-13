def format_number(number, specifier):
    result = format(number, specifier)
    return f'result = {result}'

print(format_number(221, 'o')) #'o' in python formatting stand for Octal