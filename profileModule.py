### import module_name
import profilingTool
print(profilingTool.build_profile('Adam', 'Jensen'))

### from module_name import function_name
from profilingTool import build_profile
print(build_profile('Ken', 'Masters'))

### from module_name import function_name as fn
from profilingTool import build_profile as bp
print(bp('Robert', 'McNamara'))

### import module_name as mn
import profilingTool as pf
print(pf.build_profile('Michael', 'Jackson'))

### from module_name import *
from profilingTool import*
print(build_profile('Jeff', 'Bezos'))
