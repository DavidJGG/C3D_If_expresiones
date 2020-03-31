class Nodo():    
    def __init__(self):
        self.etqV=[]
        self.etqF=[]
        self.etqS=[]
        self.tmp=""
        self.cod=""
    
    def setEtqV(self, e):
        self.etqV.append(e)
        
    def setEtqF(self, e):
        self.etqF.append(e)

    def setEtqS(self, e):
        self.etqS.append(e)    

    def setTemporal(self, t):
        self.tmp=t
    
    def setCodigo(self, c):
        self.cod=c

    def getEtqV(self):
        return ",".join(self.etqV)
    def getEtqF(self):
        return ",".join(self.etqF)
    def getEtqS(self):
        return ",".join(self.etqS)
    
    def getCodigo(self):
        return self.cod

    def getTmp(self):
        return self.tmp