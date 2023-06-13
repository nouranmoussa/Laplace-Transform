import sympy
sympy.init_printing()

t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

f =  sympy.exp(a*t)                   #here we write any function

result1 = sympy.laplace_transform(f, t, s)
print(result1)
