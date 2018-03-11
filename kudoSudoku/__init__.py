from copy import deepcopy
from time import clock

class sudoku:
    def __init__(self,vals):
        self.__n = len(vals)
        self.__rows = []
        self.__cols = []
        self.__eles = []
        self.blocks = []
        self.isChanged = False
        self.solved = 0
        self.expired = False
        self.Iterations = 0
        self.guesses = 0

        for i in range(self.__n):
            x = subTable(self.__n,self)
            y = subTable(self.__n,self)
            z = subTable(self.__n,self)
            self.__rows.append(x)
            self.__cols.append(y)
            self.blocks.append(z)

        for i in range(self.__n):
            for j in range(self.__n):
                k = int((self.__n)**(1/2.0))
                b = k*(i//k) + (j//k)
                e = element(self,self.__rows[i],self.__cols[j],self.blocks[b])
                if(vals[i][j] != 0):
                    e.setVal(vals[i][j])
                self.__rows[i].setVal(j,e)
                self.__cols[j].setVal(i,e)
                self.blocks[b].setVal( k*(i%k) + j%k,e)
                self.__eles.append(e)
                
        for i in self.__eles:
            for n in range(self.__n):
                if(i.getVal() == 0):
                    if not (i.myRow().contains(n+1) or i.myCol().contains(n+1) or i.myBlock().contains(n+1)):
                        i.markPoss(n+1)

    def __markOut(self):
        for i in self.__rows:
            i.reposs()
        
        for i in self.__cols:
            i.reposs()
        
        for i in self.blocks:
            i.reposs()

    def solve(self):
        clock()
        self.Iterations += 1
        self.isChanged = False
        self.__markOut()
        if(self.isChanged):
            return self.solve()
        else:
            if self.expired: #wrong puzzle
                return {
                    'done' : False,
                    'iterations' : self.Iterations,
                    'guesses' : self.guesses,
                    'timeTaken' : clock(),
                    'solution' : None}
            elif(self.solved == self.__n**2): #solved
                return {
                    'done' : True ,
                    'iterations' : self.Iterations,
                    'guesses' : self.guesses,
                    'timeTaken' : clock(),
                    'solution' : self.__myTable() }
            else: #unsolved
                return self.__guessOne()

    def __myTable(self):
        table = []
        for i in self.__rows:
            row = []
            for ele in i.myeles():
                if(ele.getVal() == 0):
                    row.append(" ")
                else:
                    row.append(ele.getVal())
            table.append(row)
        return table

    def __guessOne(self):
        self.guesses += 1
        selected = 0
        itrs = []
        for i in range(len(self.__eles)):
            posses = self.__eles[i].getPoss()
            if(len(posses) != 0):
                selected = i
                itrs = posses
                break
        
        for i in itrs:
            newTab = deepcopy(self)
            newTab.__eles[selected].setVal(i)
            ss = newTab.solve()
            if(ss['done']):
                return ss


class subTable:
    
    def __init__(self,n,table):
        self.__n = n
        self.__eles = [None for i in range(n)]
        self.__vals = []
        self.__table = table

    def setVal(self,i,val):
        self.__eles[i] = val
        if(val.getVal() != 0):
            self.__vals.append(val.getVal())

    def myeles(self):
        return self.__eles

    def contains(self,val):
        return val in self.__vals

    def addVal(self,val):
        if not val in self.__vals:
            self.__vals.append(val)

        for e in self.__eles:
            if(e != None):
                e.removePoss(val)

    def reposs(self):
        poss = []
        for i in self.__eles:
            if(i.getVal() == 0):
                poss.append(i.getPoss())
            else:
                poss.append([i.getVal()])
        vals = self.solveCons(poss)['val']
        for i in range(len(vals)):
            poss = vals[i]
            if(len(poss) == 1):
                if(poss[0] != self.__eles[i].getVal() and self.__eles[i].getVal() != 0):
                    print(self.__eles[i].getVal(),"Errorrr",poss[0])
                    self.__table.isChanged = True
                elif(poss[0] != self.__eles[i].getVal() and self.__eles[i].getVal() == 0):
                    self.__eles[i].setVal(poss[0])
                    self.__table.isChanged = True
            else:
                posses = self.__eles[i].getPoss()
                for poss in posses:
                    if not poss in vals[i]:
                        self.__eles[i].removePoss(poss)
                        self.__table.isChanged = True

    def solveCons(self,row):
        if(len(row) == 1):
            return { "exists" : True , "val" : row}
        else:
            head = row[0]
            tail = row[1:]
            headfinal = []
            tailfinal = [[] for k in range(len(tail))]
            for ele in head:
                reformed_tail = list(map(lambda x : [e for e in x if e != ele],tail))
                tail_val = self.solveCons(reformed_tail)
                if(tail_val['exists'] and (not ([] in tail_val['val']))):
                    headfinal.append(ele)
                    tailfinal = concatAll(tailfinal,tail_val['val'])
            if(len(head) ==0):
                return {'exists' : False , 'val' : None}
            else:
                return {'exists' : True , 'val' : [headfinal] + tailfinal}   


class element:
    def __init__(self,table,row,col,block):
        self.__val = 0
        self.__poss = []
        self.__row = row
        self.__col = col
        self.__block = block
        self.__table = table

    def setVal(self,val):
        if(self.__row.contains(val) or self.__col.contains(val) or self.__block.contains(val)):
            self.__table.expired = True
        self.__val = val
        self.__table.solved += 1
        self.clearPoss()
        self.__block.addVal(val)
        self.__col.addVal(val)
        self.__row.addVal(val)
        
    def myRow(self):
        return self.__row

    def myCol(self):
        return self.__col
    
    def myBlock(self):
        return self.__block

    def markPoss(self,val):
        if not val in self.__poss:
            self.__poss.append(val)

    def clearPoss(self):
        self.__poss = []

    def getVal(self):
        return self.__val

    def getPoss(self):
        return self.__poss

    def removePoss(self,val):
        if val in self.__poss:
            self.__poss.remove(val)
            if(len(self.__poss) == 1 and self.__val == 0):
                self.setVal(self.__poss[0])



def concatAll(lists1,lists2):
    lists0 = []
    for i in range(len(lists1)):
        resulting_list = list(lists1[i])
        resulting_list.extend([x for x in lists2[i] if x not in lists1[i]])
        lists0.append(resulting_list)
    return lists0
