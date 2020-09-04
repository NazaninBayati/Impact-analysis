import understand
import sys
import FileLevel.MainMetrics


class fileMetrics(FileLevel.MainMetrics.Metrics):

    # extract used files by the file
    def included_files(self , db,file_dependency):
        self.db = db
        for file in sorted(db.ents("File")):
            if str(file.name()) not in file_dependency:
                file_dependency[str(file.name())]=[]
            file_dependency[str(file.name())].append(list(file.depends()))

    # extract files that included/used the file
    def used_by_file(self , db, file_dependentby):
        self.db = db
        for file in sorted(self.db.ents("File")):
            if str(file.name()) not in file_dependentby:
                file_dependentby[str(file.name())]=[]
            file_dependentby[str(file.name())].append(list(file.dependsby()))


    def file_dependency_list(self,file,file_dependency):
        if str(file) in file_dependency:
            return file_dependency[str(file)]


    def file_dependent_list(self,file,file_dependentby):
        if str(file) in file_dependentby:
            return file_dependentby[str(file)]


    def Language(self,pfix):
        self.pfix = pfix[0]

        db_analyze_language = ''
        if pfix == 'cpp' or pfix == 'h' or pfix == 'C' or pfix == 'hpp' or pfix == 'hxx' or pfix == 'cxx' or \
                pfix == 'H' or pfix == 'inl' or pfix == 'cc' or pfix == 'hh':
            db_analyze_language = 'C++'
        if pfix == 'c':
            db_analyze_language = 'C'
        if pfix == 'a' or pfix == 'ads' or pfix == 'gpr' or pfix == 'ada' or pfix == 'adb_analyze':
            db_analyze_language = 'Ada'
        if pfix == 'cgi' or pfix == 'pl' or pfix == 'pm':
            db_analyze_language = 'Perl'
        if pfix == 'css':
            db_analyze_language = 'CSS'
        if pfix == 'dpr' or pfix == 'dfm':
            db_analyze_language = 'Delphi'
        if pfix == 'f77' or pfix == 'f' or pfix == 'f90' or pfix == 'for' or pfix == 'f03' or \
                pfix == 'f95' or pfix == 'ftn':
            db_analyze_language = 'Fortran'
        if pfix == 'jov' or pfix == 'cpl':
            db_analyze_language = 'Jovidal'
        if pfix == 'mm':
            db_analyze_language = 'Objective-C++'
        if pfix == 'py':
            db_analyze_language = 'Python'
        if pfix == 'sql':
            db_analyze_language = 'Sql'
        if pfix == 'tsx' or pfix == 'ts':
            db_analyze_language = 'TypeScript'
        if pfix == 'vb':
            db_analyze_language = 'Basic'
        if pfix == 'vhdl' or pfix == 'vhd':
            db_analyze_language = 'VHDL'
        if pfix == 'asm' or pfix == 's':
            db_analyze_language = 'Assembly'
        if pfix == 'cbl' or pfix == 'cob' or pfix == 'cpy':
            db_analyze_language = 'COBOL'
        if pfix == 'htm' or pfix == 'html':
            db_analyze_language = 'Html'
        if pfix == 'js':
            db_analyze_language = 'Javascript'
        if pfix == 'pas' or pfix == 'sp':
            db_analyze_language = 'Pascal'
        if pfix == 'plm':
            db_analyze_language = 'Plm'
        if pfix == 'tcl':
            db_analyze_language = 'Tcl'
        if pfix == 'txt' or pfix == 'TXT':
            db_analyze_language = 'Text'
        if pfix == 'vh' or pfix == 'v':
            db_analyze_language = 'Verilog'
        if pfix == 'xml':
            db_analyze_language = 'Xml'
        if pfix == 'bat':
            db_analyze_language = 'MSDos Batch'
        if pfix == 'cs':
            db_analyze_language = 'C#'
        if pfix == 'java':
            db_analyze_language = 'Java'
        if pfix == 'm':
            db_analyze_language = 'Objective-C'
        if pfix == 'php':
            db_analyze_language = 'Php'
        return db_analyze_language


    def fileList(self,file,File_Metrics):
        self.file = file
        self.File_Metrics = File_Metrics

        location = []
        qualified_temp2 = []
        file_qname = self.file.longname()
        file_name_Qualified = file_qname.split('/')
        location.append(file_qname)
        qualified_temp = file_name_Qualified[file_name_Qualified.__len__() - 1].split('.')
        qualified_temp2.append(file_name_Qualified[0:len(file_name_Qualified) - 1])
        qualified_temp2[0].append(qualified_temp[0])
        qualified_temp2 = qualified_temp2[0]
        qualified_temp = ".".join(qualified_temp[1:qualified_temp2.__len__()])
        qualified_list = []
        qualified_list.append(location[0])
        qualified_list.append(qualified_temp)
        file_name_Qualified = '.'.join(qualified_list[1:qualified_list.__len__() - 1])
        if qualified_list[1] not in File_Metrics:
            File_Metrics[qualified_list[1]]=[]
        File_Metrics[qualified_list[1]].append(str(file.name()))
        File_Metrics[qualified_list[1]].append(location[0])
        return (qualified_list[1], location[0])

    def cls_printCallPairs(self,ent,cls_CallPairs):
        self.ent = ent
        self.cls_CallPairs = cls_CallPairs
        defineAref = self.ent.ref("definein")
        if defineAref is not None:
            if str(defineAref.file().longname()) not in cls_CallPairs:
                cls_CallPairs[str(defineAref.file().longname())] = []
            cls_CallPairs[str(defineAref.file().longname())].append(str(ent.longname()))


    def printCallPairs(self,ent,CallPairs):
        self.ent = ent
        self.CallPairs = CallPairs
        defineAref = self.ent.ref("definein")
        if defineAref is not None:
            if str(defineAref.file().longname()) not in CallPairs:
                CallPairs[str(defineAref.file().longname())] = []
            CallPairs[str(defineAref.file().longname())].append(str(ent.longname()))


    def class_cont(self,file,cls_CallPairs):
        if str(file.longname()) in cls_CallPairs:
            return cls_CallPairs[str(file.longname())]


    def function_cont(self,file,CallPairs):
        if str(file.longname()) in CallPairs:
            return CallPairs[str(file.longname())]


    def main(self,db,file_dependency, file_dependentby,File_Metrics,cls_CallPairs,CallPairs):
        self.db = db
        self.file_dependency=file_dependency
        self.file_dependentby=file_dependentby
        self.File_Metrics = File_Metrics
        self.cls_CallPairs = cls_CallPairs
        self.CallPairs = CallPairs


        fileMetrics.included_files(self,db,file_dependency)
        fileMetrics.used_by_file(self,db,file_dependentby)

        for ent in sorted(db.ents("class,method,struct,procedure, template class"), key=lambda ent: ent.name()):
            fileMetrics.cls_printCallPairs(self,ent,cls_CallPairs)

        for ent in sorted(db.ents("function"), key=lambda ent: ent.name()):
            fileMetrics.printCallPairs(self,ent,CallPairs)


        file_list = []
        final_list = []
        counter = 0
        for file in sorted(db.ents("File")):
            def_str=''
            end_str=''
            if file.library() != "Standard":
                for ref in file.refs("define"):
                    def_str = str(ref.line())
                for ref in file.refs("End"):
                    end_str = str(ref.line())
                file_name = (file.name())
                db_analyze_pfix = file_name.split('.')

                if len(db_analyze_pfix) > 1 :
                    if db_analyze_pfix[1] == 'hpp' or db_analyze_pfix[1] == 'h' or db_analyze_pfix[1] == 'hh': continue
                    file_lang = (fileMetrics.Language(self,db_analyze_pfix[1]))

                    name_qname_loc = fileMetrics.fileList(self,file,File_Metrics)
                    file_metric = fileMetrics.metric_val(self,file)

                    if file_metric.__len__()<20:
                        file_metric=['None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None']



                    contained_classes = fileMetrics.class_cont(self,file,cls_CallPairs)
                    contained_function = fileMetrics.function_cont(self,file,CallPairs)
                    dep = fileMetrics.file_dependency_list(self,file,file_dependency)
                    depBy = fileMetrics.file_dependent_list(self,file, file_dependentby)

                    #file_list.append(str(file.name()))
                    #file_list.append(file_lang)
                    #file_list.append(def_str)
                    #file_list.append(end_str)
                    #file_list.append(name_qname_loc[0])

                    stri = ''
                    stri = str(file.name())
                    jj = 0
                    while jj < len(dep[0]):
                        #file_list2=[]
                        #stri = stri + ',' + str(dep[0][jj])
                        file_list.append(stri)
                        file_list.append(str(dep[0][jj]))
                        #file_list.append(file_list2)

                        jj = jj + 1
                        counter=counter+1



                    #file_list.append(contained_function)
                    #file_list.append(contained_classes)
                    #file_list.append(dep[0])
                    #file_list.append(depBy[0])

        #iterator = jj + 10
        iterator = 2
        #header = 'Filename,ProgrammingLanguage,StartLine,EndLine,FileQualifiedname,Location,AltAvgLineBlank,AltAvgLineCode,AltAvgLineComment,AltCountLineBlank,AltCountLineCode,AltCountLineComment,AvgCyclomatic,AvgCyclomaticModified,AvgCyclomaticStrict,AvgEssential,AvgLine,AvgLineBlank,AvgLineCode,AvgLineComment,CountDeclClass,CountDeclFunction,CountLine,CountLineBlank,CountLineCode,CountLineCodeDecl,CountLineCodeExe,CountLineComment,CountLineInactive,CountLinePreprocessor,CountSemicolon,CountStmt,CountStmtDecl,CountStmtEmpty,CountStmtExe,MaxCyclomatic,MaxCyclomaticModified,MaxCyclomaticStrict,MaxEssential,MaxNesting,RatioCommentToCode,SumCyclomatic,SumCyclomaticModified,SumCyclomaticStrict,SumEssential,ContainedFunctions,ContainedClasses,calledFiles,CalledByFiles'
        header = ''
        print("File level done!")
        final_list.append(file_list)
        FileLevel.MainMetrics.Metrics.printresult(self,'File_level_ARM.txt',final_list,iterator,header)
    def __init__(self):
        args = sys.argv[1]

        file_dependency = {}
        file_dependentby = {}
        File_Metrics = {}
        cls_CallPairs = {}
        CallPairs = {}
        file_list = []
        final_list = []
        db = FileLevel.MainMetrics.Metrics.DBlodb(self,str(args))
        FileLevel.MainMetrics.Metrics.__init__(self)
        self.db = db
        fileMetrics.main(self, db,file_dependency,file_dependentby,File_Metrics,cls_CallPairs,CallPairs)

P1 = fileMetrics()