from pydriller import RepositoryMining
from datetime import datetime
import sys
class pydrill:
    def __init__(self):
        str_modified = ""
        args = sys.argv[1]
        pydrill.main(self,str_modified,args)

    def main(self,str_modified,args):
        self.str_modified = str_modified
        self.args = args
        print("Process is started!")

        for commit in RepositoryMining(str(args)).traverse_commits():
            str_modified = str_modified + "\n"
            for m in commit.modifications:
                str_modified = str_modified +str(m.filename)+ ","
            print("processing...")
        print("Pydrill process is done!")




        with open('modified.txt', 'w') as classhandle:
            classhandle.write(str_modified)

p = pydrill()

