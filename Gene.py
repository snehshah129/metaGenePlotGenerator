# Sneh Shah
# Gene Class
# COM 491 Independent Study

import statistics

class Gene:
    def __init__(self,name,chromosome,Type,start,end,strand):
        self.name = name
        self.chromosome = chromosome
        self.Type = Type
        self.start = start
        self.end = end
        self.strand = strand
        self.array = [0] * (self.end - self.start + 1)
        self.fixedArray = [0] * 100
        self.used = False

    def getName(self):
        return self.name

    def getChromosome(self):
        return self.chromosome

    def getType(self):
        return self.Type

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getStrand(self):
        return self.strand

    def getArray(self):
        return self.array

    def createFixedArray(self):
        if len(self.array) >= 100:
            width = len(self.array)//100
            for binNum in range(99):
                binList = []
                for inputVal in range((0 + width*binNum),(width + width*binNum),1):
                    binList.append(self.array[inputVal])
                self.fixedArray[binNum] = round(statistics.mean(binList))
            lastSection = []
            for i in range(width*99,len(self.array),1):
                lastSection.append(self.array[i])
            self.fixedArray[-1] = round(statistics.mean(lastSection))
    
                    
             
    def getFixedArray(self):
        return self.fixedArray

    def getAverageExpression(self):
        average = round(statistics.mean(self.fixedArray))
        return average

    def incrementArray(self,index):
        self.array[index] = self.array[index] + 1

    def isUsed(self):
        return self.used

    def setUsed(self):
        self.used = True

    def printGene(self):
        print('GeneID: ',self.name)
        print('Chromosome: ',self.chromosome)
        print('Type: ',self.Type)
        print('Start: ',self.start)
        print('End: ',self.end)
        print("Array:",self.array)
        
        
