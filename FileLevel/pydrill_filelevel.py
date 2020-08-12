from pydriller import RepositoryMining
from datetime import datetime
str_modified = ""

dt1 = datetime(2016, 10, 8, 17, 0, 0)
dt2 = datetime(2016, 10, 18, 17, 59, 0)
#,since=dt1, to=dt2
for commit in RepositoryMining("/home/nazanin/ceph").traverse_commits():
    str_modified = str_modified + "\n"
    for m in commit.modifications:
        str_modified = str_modified +str(m.filename)+ ","
        print(str_modified)



with open('modified.csv', 'w') as classhandle:
    classhandle.write(str_modified)

with open('modified.txt', 'w') as classhandle:
    classhandle.write(str_modified)



