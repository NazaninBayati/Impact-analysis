import os, subprocess, time

# YOU CAN COMMENT LINE 4 AND 5 AFTER FIRST TIME YOU CREATE THE UND DATABASE
subprocess.run([r'/FileLevel/DB.bat'])
time.sleep(10)

# STRUCTURAL DEPENDENCY
os.system('python /FunctionLevel/structural_FunctionMetrics.py  /path/to/udb')

#LOGICAL DEPENDENCY
os.system('python pydriller.py /path/to/project v15.2.0 v15.2.1')
os.system('python function_scenario.py /path/to/current_version /path/to/previous_version')
os.system('python arm.py')
os.system('python scoring.py')