from os.path import dirname, basename, isfile
import glob

modules = glob.glob(dirname(__file__)+"/*.py")
nameDir = basename(dirname(__file__))
__all__ = []
myVars = vars()

for f in modules:
    if isfile(f) and not f.endswith('__init__.py'):
        tempVar = __import__("API." + nameDir + "." + basename(f)[:-3], fromlist=nameDir)
        myVars[basename(f)[:-3]] = tempVar.myVars[basename(f)[:-3]]
        __all__ += [basename(f)[:-3]]

foo = "bar"
