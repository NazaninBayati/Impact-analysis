from apyori import apriori
import sys

class arm:
    def cleanser(self,logic_db,db_struct):
        self.logic_db = logic_db
        self.db_struct = db_struct
        temp = logic_db.split('\n')
        with open('merged_source.txt','w') as handler:
            for i in temp:
                a = i.split(',')
                print(a)
                if i.split(',').__len__()>2:
                    str_splited = i.split(',')
                    counter = 1
                    j=0
                    while j < str_splited.__len__()-1:
                        b = str_splited[j]
                        l = len(str_splited[j].split('.'))
                        if len(str_splited[j].split('.'))>1:
                            if str_splited[j].split('.')[1]=='cc':

                                k = j+1
                                while k < str_splited.__len__()-1:
                                    if str_splited[k].split('.').__len__()>1:
                                        if str_splited[k].split('.')[1]=='cc':
                                            str_joint = str(str_splited[j])+','+str_splited[k]
                                            handler.write(str_joint)
                                            handler.write('\n')


                                    k=k+1
                                    #counter = counter + 1
                        j = j+1

    def __init__(self):
        #args = "/home/nazanin/modified_DB_Ceph_summary.csv"
        args = "modified.txt"
        db = open(str(args))
        db = db.read()
        db_struct = open('File_level_ARM.txt', 'r').read()
        arm.cleanser(self, db, db_struct)

        db_logic = open('merged_source.txt','r').read()


      #  with open("db.txt",'w')as handler:
      #      handler.write(db_struct)
      #      handler.write('\n')
       #     handler.write(db_logic)
        db = db_struct
        db = db + '\n'
        db = db + db_logic


        arm.associationRM(self, db)

    def write(self, association_rules):
        with open('result.txt', 'w')as handler:
            for i in range(len(association_rules)):
                handler.write(str(association_rules[i]))
                handler.write('\n')

    def datacleaning(self,db):
        self.db = db
        temp = db.split('\n')
        i = 0
        while i < temp.__len__():
            temp[i] = temp[i].split(',')
            i = i + 1
        m=0
        n=0
        for m in range(0,len(temp)-1):
            for n in range(0,len(temp[m])-1):
                a = temp[m]
                b = temp[m][n]
                if str(temp[m][n]) == '':
                    counter = n
                    temp[m] = temp[m][0:n]
                    break
        return temp
    def associationRM(self,db):
        self.db = db
        dataset = arm.datacleaning(self,db)
        association_rules = apriori(dataset, min_support=0.0001, min_confidence=0.002)
        association_rules = list(association_rules)
        arm.write(self,association_rules)



p1 = arm()