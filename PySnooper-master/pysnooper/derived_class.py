
from scripts.baseclass1 import BaseClass1
from scripts.baseclass2 import BaseClass2



class DerivedClass(BaseClass1,BaseClass2):
        
    def __init__(self, name):
        self.name = name
        
    def dummy(self):
        pass
        
    