import understand
import sys
import csv

class Metrics:
    def __int__(self,db):
        self.db = db

    def DBlodb(self,args):
        self.args = args
        db = understand.open(str(args))
        return db

    def metric_val(self,file):
        self.file = file
        file_metric = []
        metrics = self.file.metric(self.file.metrics())

        for k, v in sorted(metrics.items()):
            file_metric.append(v)
        return file_metric

    def printresult(self,name,final_list,iterator,header):
        self.name = name
        self.final_list = final_list
        self.iterator = iterator
        self.header = header


        i = 0


        with open(str(name), 'w') as classhandle:
            i = 0

            #classhandle.write(str(header))
            #classhandle.write('\n')
            for listitem in final_list:
                for j in listitem:
                    classhandle.write('%s,' % j)
                    i = i + 1
                    if i % int(iterator) == 0:            classhandle.write('\n')



