class Main:
    def Structural_data_load(self,args):
        self.args = args

        structural_dependency = open(str(args))
        structural_dependency = structural_dependency.read()
        return structural_dependency

    def Logical_data_load(self,args):
        self.args = args
        logical_dependency = open(str(args))
        logical_dependency = logical_dependency.read()
        return logical_dependency

    def write(self,file_structural,title):
        self.file_structural = file_structural
        self.title = title
        with open(str(title), 'w')as handler:
            for i in (file_structural):
                handler.write(i)
                handler.write(":")
                handler.write(str(file_structural[str(i)]))
                handler.write('\n')
