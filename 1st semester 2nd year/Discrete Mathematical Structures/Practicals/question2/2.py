class RELATION:        #declaring the class
    def __init__(self,matrix):
        self.matrix=matrix
        self.lenOfMatrix=len(matrix)
    def isReflexive(self):           #function checking reflexivity of the relation
        for i in range(self.lenOfMatrix):
            if self.matrix[i][i]!=1:
                return False
        return True
    def isSymmetric(self):       #function checking symmetric nature of the relation
        for i in range(self.lenOfMatrix):
            for j in range(self.lenOfMatrix):
                if self.matrix[i][j]!=self.matrix[j][i]:
                    return False
        return True
    def isAntiSymmetric(self):             #function checking antisymmetrix nature of the relation
        for i in range(self.lenOfMatrix):
            for j in range(self.lenOfMatrix):
                if self.matrix[i][j]==1 and self.matrix[j][i]==1 and i!=j:
                    return False
        return True
    
    def isTransitive(self):           #function checking transitive nature of the relation
        for i in range(self.lenOfMatrix):
            for j in range(self.lenOfMatrix):
                if self.matrix[i][j]==1:
                    for k in range(self.lenOfMatrix):
                        if self.matrix[j][k]==1 and self.matrix[i][k]!=1:
                            return False
        return True
    def determineRelationType(self): #function checking relation type
        isEquivalence=self.isReflexive() and self.isSymmetric() and self.isTransitive()
        isPartialOrder=self.isReflexive() and self.isAntiSymmetric() and self.isTransitive()

        if isEquivalence:
            return "The given relation is a Equivalence Relation"
        elif isPartialOrder:
            return "The given relation is a partial order Relation"
        else:
            return "None"

matrix1=[[1,0,0],[0,1,0],[0,0,1]]     #relation 1
Relation1=RELATION(matrix1)
print(Relation1.determineRelationType())

matrix2=[[1,0,0],[0,1,1],[0,0,1]]   #relation 2
Relation2=RELATION(matrix2)
print(Relation2.determineRelationType())
