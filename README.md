# Impact Analysis

In this project we have two basic goals:
   -	Analyzing the source code to extract all dependencies
   
   -	Apply it on different granularities i.e. file-level, class-level, function-level
---------------------------------------------------------------------------------------------------------------------------------------------------- 
# Analyzing the source code

We are looking for a complete group of dependencies. Therefore, we first extract the structural dependencies then we check the logical dependencies.

   -	In structural dependency: 
   -	In logical dependency:
 ----------------------------------------------------------------------------------------------------------------------------------------------------  
# Supporting different granularities: 

The project could be applied for various code granularities including:

   -	File level
   -	Class level
   -	Function level
   
Mostly projects which are written in C/C++ are our target.

-----------------------------------------------------------------------------------------------------------------------------------------------

# Source Code Descriptions

* For both File level and Class level you can run the "File level" folder.

To run the "File level" code you only need to execute the setup.py

------------------------------------------------------------------------------------------------------------------------------------------------
The following lines will create the und database, which is required for our structural analysis:
Creating und is mandatory for all levels.

   + subprocess.run([r'/Impact-analysis/FileLevel/DB.bat'])
   + time.sleep(10)

* hint: you can comment these two lines after you created the und database.
* prerequisite: open the DB.bat file and give the proper path i.e. "/home/nazanin/db"

--------------------------------------------------------------------------------------------------------------------------------------------------
Next step the structural dependency will be extracted

   + os.system('python structural_filelevel.py /path/to/udb')

The path that the udb database is located should be given to the above code.

--------------------------------------------------------------------------------------------------------------------------------------------------
Now, you have the structural dependencies and you can start the logical analysis.
The following command lines are co-related and they are input/output of each other.

   + os.system('python pydrill_filelevel.py /path/to/project')
   
* give the path to the project you made und db for to the above command.

   + os.system('python arm.py')
   + os.system('python scoring.py')

* hint: the FinalList_merged_result.txt is the final output

-----------------------------------------------------------------------------------------------------------------------------------------------
* For the Function level, you can run the "Function level" folder.

To run the "Function level" code you only need to execute the setup.py

------------------------------------------------------------------------------------------------------------------------------------------------

The und DB is similar to the prev stage.

For structural dependencies, you need to give the und path to the command line.

   + os.system('python structural_FunctionMetrics.py  /path/to/udb')

-------------------------------------------------------------------------------------------------------------------------------------------------

To analyze the logical dependency these commands should be run:

For the function level, we need to run pydriller.py for every two versions separately, then as the inputs, you have to give the 
project path and define two versions of the project, respectively.

   + os.system('python pydriller.py /path/to/project v15.2.0 v15.2.1')

you can give the paths to the current version of the program and the previous version of the program in the following command.

   + os.system('python function_scenario.py /path/to/current_version /path/to/previous_version')

   + os.system('python arm.py')
   + os.system('python scoring.py')







