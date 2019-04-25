
from scripts.baseclass1 import BaseClass1
from scripts.baseclass2 import BaseClass2



class ExistingClass(BaseClass1,BaseClass2):
        
    def __init__(self, name):
        self.name = name
        
    def dummy(self):
        pass
        
    