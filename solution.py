#################################
# input # read from 'input.txt' #
#################################
from contextlib import redirect_stdout
from io import StringIO
from difflib import Differ
from itertools import zip_longest as _zip_longest

with open('input.txt', 'r') as f:
    _input = f.read()

def input_generator(_input):
    for line in _input.splitlines():
        yield line

input_gen=input_generator(_input)
input = input_gen.__next__

captured_stdout = StringIO()
_redirect_stdout = redirect_stdout(captured_stdout)
_redirect_stdout.__enter__()

#################################
# main # only copy this section #
#################################
def solve(a,b):
    print(a+b)
    print(a)

T=int(input())
for _ in range(T):
    a=int(input())
    b=int(input())
    
    solve(a,b)

######################################
# output # compare with 'output.txt' #
######################################
_redirect_stdout.__exit__(None, None, None)

with open('output.txt', 'r') as f:
    out = f.read()

for x,y in _zip_longest(captured_stdout.getvalue().splitlines(),
                out.splitlines()):
    print('\n'.join(Differ().compare([x],[y])))
