from apyori import apriori
import sys

class arm:
    def __init__(self):
        print("Association Rule Mining is in progress...")
        args = "holder_result.txt"
        db = open(str(args))
        db = db.read()
        arm.associationRM(self, db)

    def write(self, association_rules):
        with open('func_result.txt', 'w')as handler:
            for i in range(len(association_rules)):
                handler.write(str(association_rules[i]))
                handler.write('\n')

    def datacleaning(self,db):
        self.db = db
        temp_arr=[]


        temp = db.split('\n')
        i = 0
        while i < temp.__len__():
            arr = []

            spliter = temp[i].split(',')
            if spliter.__len__()>1:

                for j in spliter:
                    if j != '':
                        arr.append(j)

                temp_arr.append( arr)

            i = i + 1

        return temp_arr
    def associationRM(self,db):
        self.db = db
        dataset = arm.datacleaning(self,db)
        association_rules = apriori(dataset, min_support=0.00000001, min_confidence=0.0000000000002)
        association_rules = list(association_rules)
        arm.write(self,association_rules)
        print("Association Rule Mining is done!")



p1 = arm()