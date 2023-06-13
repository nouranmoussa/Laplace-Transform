import sympy
sympy.init_printing()

s, t = sympy.symbols('s t')
a = sympy.symbols('a', real=True, positive=True)

trans_func = 1 / (s-a)               #here we write any function

result = sympy.inverse_laplace_transform(trans_func, s, t)
print (result)
