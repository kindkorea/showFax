a = my_string = "Hello, what are doing"
b = my_string = f'v{my_string}'
print(f'{a=}')
print(f'{b=}')
c = b.lstrip('v')
print(f'{c=}')



