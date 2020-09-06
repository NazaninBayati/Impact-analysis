import os
# file level structural dependency
os.system('python structural_filelevel.py /home/nazanin/db.udb')

os.system('python pydrill_filelevel.py /home/nazanin/ceph')
os.system('python arm.py')
os.system('python scoring.py')

