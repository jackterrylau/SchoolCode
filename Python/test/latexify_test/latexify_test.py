# latexify library install :   pip install latexify-py
import latexify
import math

@latexify.with_latex
#@latexify.function
#@latexify.expression
def roots(a,b,c):
    return (-b + math.sqrt(b**2-4*a*c))/(2*a)

print(roots)
#latexify.get_latex(roots)

