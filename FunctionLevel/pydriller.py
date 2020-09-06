from pydriller import RepositoryMining
import sys
from datetime import datetime
class pydrill:
    def __init__(self):

        str_modified = ""
        str_diff_parsed = ""
        repository_loc = sys.argv[1]
        from_tag = sys.argv[2]
        to_tag = sys.argv[3]
        pydrill.main(self, str_modified, str_diff_parsed,repository_loc,from_tag,to_tag)

    def main(self,str_modified, str_diff_parsed,repository_loc,from_tag,to_tag):

        self.str_modified = str_modified
        self.str_diff_parsed = str_diff_parsed
        self.repository_loc = repository_loc
        self.from_tag = from_tag
        self.to_tag = to_tag

        print("Process is started!")
        for commit in RepositoryMining(str(repository_loc),from_tag=str(from_tag),to_tag=str(to_tag)).traverse_commits():
            str_modified = str_modified + "\n"
            for m in commit.modifications:
                str_modified = str_modified +str(m.methods)+ ","
                str_diff_parsed = str_diff_parsed+ str(m.diff_parsed)+','+str(m.filename)+'\n'

            print("processing...")
        print("Pydrill process is done!")

        with open('func_modified.txt', 'w') as classhandle:
            classhandle.write(str_modified)

p = pydrill()