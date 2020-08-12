class Main:
    def Structural_data_load(args):
        #args, 'r'

        structural_dependency = open( 'File_level_ARM.txt')
        structural_dependency = structural_dependency.read()
        return structural_dependency

    def Logical_data_load(args):
        #args
        logical_dependency = open('result.txt')
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
