class Main():

    def load_db_functionlevel(self,db_path):
        db = open(db_path,'r').read()
        return db

    def write(self,file, title):
        self.file = file
        key = file.keys()

        with open(str(title),'w')as handler:
            for i in key:

                a = file[i]
                for j in a:
                    handler.write(str(j[0]).split("\'")[1]+',')

                handler.write("\n")

p = Main()