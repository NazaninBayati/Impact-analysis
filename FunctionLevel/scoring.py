import FunctionLevel.Main
import sys
import json

class score(FunctionLevel.Main.Main):

    def max_str(self,arr_members):
        self.arr_members = arr_members
        max_str_temp1 = arr_members.split(',')
        max_str_temp2 = max_str_temp1[0]
        max_str_temp3 = max_str_temp1[1]
        max_str_length = min(len(max_str_temp2),len(max_str_temp3))
        i=0
        for i in range(1,max_str_length-1):
            if max_str_temp2[i]>max_str_temp3[i+1]:
                return True

            elif max_str_temp2[i]<max_str_temp3[i+1]:
                return False

            else:
                continue


    def logical_data_cleaning(self,logical_db, file_bascket):
        self.logical_db = logical_db
        self.file_basket = file_bascket
        logic = logical_db.split('RelationRecord(items=frozenset({')
        for i in range(1, logic.__len__() - 1):

            bascket = logic[i].split('}')


            bascket_members = bascket[0]
            if len(bascket_members.split(',')) > 1:


                comparison = score.max_str(self, bascket_members)

                support = bascket[1].split(',')[1].split('=')[1]
                len_value = (len(str(bascket).split('confidence=')))


                if comparison :
                    confidence_second = str(bascket).split('confidence=')[len_value-2].split(',')[0]
                    confidence = str(bascket).split('confidence=')[len_value-1].split(',')[0]
                    lift_second = str(bascket).split('lift=')[len_value-2].split(')')[0]
                    lift = str(bascket).split('lift=')[len_value-1].split(')')[0]



                elif not(comparison):
                    confidence = str(bascket).split('confidence=')[len_value-2].split(',')[0]
                    confidence_second = str(bascket).split('confidence=')[len_value-1].split(',')[0]
                    lift = str(bascket).split('lift=')[len_value-2].split(')')[0]
                    lift_second = str(bascket).split('lift=')[len_value-1].split(')')[0]




                if bascket_members not in file_bascket:
                    file_bascket[bascket_members] = []
                file_bascket[bascket_members].append(support)
                file_bascket[bascket_members].append(confidence)
                file_bascket[bascket_members].append(lift)
                file_bascket[bascket_members].append(confidence_second)
                file_bascket[bascket_members].append(lift_second)


            else: continue
        return file_bascket

    def structural_data_cleaning(self,structural_db, file_structural):
        self.structural_db = structural_db
        self.file_structural = file_structural
        struct = ''
        struct = structural_db.split('\n')
        print(" ")
        for i in range(0, struct.__len__()-1):
            str_spliter = struct[i].split(',')
            if str_spliter.__len__()>1:
                j=0
                str_formatter =[]
                a = str_spliter.__len__()
                while j < str_spliter.__len__()-2:
                    str_formatter .append(str(str_spliter[j]))
                    j = j+1
                str_formatter .append( str(str_spliter[j]))
            if str(str_formatter) not in file_structural:
                file_structural[str(str_formatter)] = []
            #file_structural[struct[i]].append(support)
        return file_structural





    def merge_score(self, file_structural, support_dict,merged_result_dictionary):
        self.file_structural = file_structural
        self.support_dict = support_dict
        self.merged_result_dictionary=merged_result_dictionary

        for i in range(0,file_structural.__len__()-1):
            a = list(file_structural.keys())
            d = str(str(a[i]).split('[')[1].split("]")[0]).split("\\")[0].split("\\")

            if d[0] in support_dict:
                print(d[0])
                file_structural[str(d)]=support_dict[str(d[0])]
                if str(d)  not in merged_result_dictionary:
                    merged_result_dictionary[str(d)]=[]
                merged_result_dictionary[str(d)]=support_dict[str(d[0])]


    def main(self,logical_db,structural_db, file_bascket,file_structural,merged_result_dictionary):
        self.logical_db = logical_db
        self.structural_db = structural_db
        self.file_bascket = file_bascket
        self.file_structural  = file_structural
        self.merged_result_dictionary = merged_result_dictionary

        support_dict = score.logical_data_cleaning(self,logical_db, file_bascket)

        score.structural_data_cleaning(self, structural_db, file_structural)

        score.merge_score(self, file_structural, support_dict,merged_result_dictionary)


        #json.dump(support_dict, open("func_logical.json", "w"))
       # json.dump(file_structural, open("func_structural.json", "w"))
        FunctionLevel.Main.Main.write(self,file_structural,'MergedList_function_structural.txt')
        FunctionLevel.Main.Main.write(self,merged_result_dictionary,'MergedList_func_result.txt')
        #json.dump(file_structural, open("func_structural.json", "w"))

    def __init__(self):
        file_bascket = {}
        file_structural = {}
        merged_result_dictionary = {}
        #args_logical = sys.argv[1]
        args_logical ='func_result.txt'
        #args_structural = sys.argv[2]
        args_structural = "Func_Level_ARM.txt"
        logical_db = FunctionLevel.Main.Main.Logical_data_load(self,str(args_logical))
        structural_db = FunctionLevel.Main.Main.Structural_data_load(self,str(args_structural))
        self.logical_db = logical_db
        self.structural_db = structural_db
        score.main(self,logical_db,structural_db, file_bascket,file_structural,merged_result_dictionary)

P1 = score()






