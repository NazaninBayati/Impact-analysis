import os , subprocess , time

# YOU CAN COMMENT LINE 4 AND 5 AFTER FIRST TIME YOU CREATE THE UND DATABASE
subprocess.run([r'/Impact-analysis/FileLevel/DB.bat'])
time.sleep(10)

# STRUCTURAL DEPENDENCY
os.system('python structural_filelevel.py /path/to/udb')

#LOGICAL DEPENDENCY
os.system('python pydrill_filelevel.py /path/to/project')
os.system('python arm.py')
os.system('python scoring.py')

