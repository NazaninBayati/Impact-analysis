from git import Repo
import os, sys, re
from FunctionLevel.Main import *
from FunctionLevel.holder import *

class functionlevel:

  def initialize(self,path,db_path):
    #self.path = path
    #self.db_path = db_path
    for root, directories, files in os.walk(path, topdown=False):
      for name in files:

        if name.split(".").__len__() > 1 and name.split(".")[1] == 'cc':

          db_path.append(os.path.join(root, name))
          print(os.path.join(root, name))

    return db_path
      # for name in directories:
      # print(os.path.join(root, name))


  def clean_data(self,arr):
    self.arr= arr
    cleaner = str(arr).split('(')[0].replace('[','').replace("]",'').replace('\\','')
    arr = [cleaner]
    return arr

  def find_match_func(self, txt, dictio_func, file_dict,filename):

    self.txt = txt
    self.dictio_func = dictio_func
    self.file_dict = file_dict
    self.filename = filename

    i = dictio_func.__len__()-1
    while i >=0:
        res = functionlevel.match_items(self,dictio_func[str(i)])

        if res:
          if str(filename) not in file_dict:
            file_dict[str(filename)] = []


          arr = functionlevel.clean_data(self,dictio_func[str(i)])

          if arr not in file_dict[str(filename)]:
            file_dict[str(filename)].append(arr)
          i = i - 1
          break
        else:
              i = i - 1


  def match_items(self,item):

    self.item = item
    a = str(item[0])
    if re.findall("=|;",str(item[0])):return False
    x = re.match(
      "([\n\r\s]*)([a-zA-Z0-9|\n\r\s]*)(char|string|int|bool|void|float|char|double)([a-zA-Z0-9|!|@|*|$|^|&|~|<|>|-|_]*)([\n\r\s]*)([a-zA-Z0-9|!|@|*|$|^|&|~|<|>|-|_]*)([:]*)*([a-zA-Z0-9|!|@|*|$|^|&|~|<|>|-|_]*)([\(].*)",
      str(item[0]))
    y = re.match(
      "([\n\r\s]*)([!|@||$|^|&|~|<|>|-|_]*[a-zA-Z][a-zA-Z0-9]*[!|@||$|^|&|~|<|>|-|_]*[a-zA-Z]*)([::]+)([!|@||$|^|&|~|<|>|-|_]*[a-zA-Z][a-zA-Z0-9]*[!|@||$|^|&|~|<|>|-|_]*[a-zA-Z]*)([\n\r\s]*)([!|@||$|^|&|~|<|>|-|_]*[a-zA-Z][a-zA-Z0-9]*[!|@||$|^|&|~|<|>|-|_|:]*[a-zA-Z]*)([!|@||$|^|&|*|<|>]*)([\(].*[\)]*).*\{*",
      str(item[0]))
    # z = re.match("([\n\r\s]*)([!|@||$|^|&|~|<|>|-|_]*[a-zA-Z][a-zA-Z0-9]*[!|@||$|^|&|~|<|>|-|_]*[a-zA-Z]*)([::]*)([!|@||$|^|&|~|<|>|-|_|*]*[a-zA-Z][a-zA-Z0-9]*[!|@||$|^|&|~|<|>|-|_|*]*[a-zA-Z]*)([\n\r\s]*)([!|@||$|^|&|~|<|>|-|_|*]*[a-zA-Z][a-zA-Z0-9]*[!|@||$|^|&|~|<|>|-|_|:]*[a-zA-Z]*)([!|@||$|^|&|*|<|>]*)([\(].*[\)]*).*\{*", str(item))
    # print(x)  # ([\n\r\s]*)([a-zA-Z][a-zA-Z0-9]*)([\n\r\s]*)([a-zA-Z][a-zA-Z0-9]*)([::]*)*([\(.*\)]*).*\{
    r = re.match(
      "([\n\r\s]*)([a-zA-Z0-9|!|@|*|$|^|&|~|<|>|-|_]*)([\n\r\s]*)([a-zA-Z0-9|!|@|*|$|^|&|~|<|>|-|_]*)([:]+)([a-zA-Z0-9|!|@|*|$|^|&|~|<|>|-|_]*)([\(])",
      str(item[0]))
    if x or y or r:

      #print("YES! We have a match!")
      return True

    else:
      #print("No match")
      return False


  def find_stmt(self,lookup,txt,dictio_func, file_dict, filename):

    self.lookup = lookup
    self.txt = txt
    self.dictio_func = dictio_func
    self.file_dict = file_dict
    self.filename = filename
    text = txt.split('\n')
    for num, line in enumerate(text):

      if str(num) not in dictio_func:
        dictio_func[str(num)] = []
      dictio_func[str(num)].append(str(line))
      if lookup in line:
        #print('found at line:', num)
        functionlevel.find_match_func(self, txt, dictio_func, file_dict, filename)
        break


  def gitdiff_parser(self,lookup_dict, precommit_lookup_dict, gitdiff_path):

    ## initialize the gitdif file out pf pydriller for each commit


    self.lookup_dict = lookup_dict
    self.precommit_lookup_dict = precommit_lookup_dict
    self.gitdiff_path = gitdiff_path

    db = open(str(gitdiff_path),'r')
    db = db.read()
    db  = db.split("\n")
    for i in db:
      add_arr=[]
      delete_arr = []
      if i != '':
        string = i.split("deleted")
        if string.__len__()>1:
          add = string[0]
          delete = string[1]
        elif re.findall("deleted",i):
          delete = string
        else: add = string



        if string[0]!='':
          str_temp = string[0].split(',')
          k = 0
          while k <str_temp.__len__():
            a = str_temp[k]
            if re.findall("[a-zA-Z]",str_temp[k]):

              if re.findall("([\r\s]*)(added)",str_temp[k]):
                k = k + 1
                add_arr.append(str_temp[k])

              else: add_arr.append(str_temp[k])
            k = k + 1

        if string[1] != '':

          str_temp = string[1].split(',')
          k = 0
          while k < str_temp.__len__()-1:
            a = str_temp[k]
            if re.findall("[a-zA-Z]", str_temp[k]):

              if re.findall("([\r\s]*)(deleted)", str_temp[k]):
                k = k + 1
                delete_arr.append(str_temp[k])
              else: delete_arr.append(str_temp[k])
            k = k + 1


      if str_temp != []:
        filename =  str_temp[str_temp.__len__()-1]

        if str(filename) not in lookup_dict:
          lookup_dict[str(filename)] = []
        lookup_dict[str(filename)].append(add_arr)

        if str(filename) not in precommit_lookup_dict:
          precommit_lookup_dict[str(filename)] = []
        precommit_lookup_dict[str(filename)].append(delete_arr)


  def main(self,lookup_dict,precommit_lookup_dict, dictio_func, file_dict,db_path, db_old_path):

    self.lookup_dict = lookup_dict
    self.precommit_lookup_dict = precommit_lookup_dict
    self.dictio_func = dictio_func
    self.file_dict = file_dict
    self.db_path = db_path
    self.db_old_path = db_old_path


    for i in db_path:

      filename = i.split("/")
      filename = filename[filename.__len__()-1]
      if filename in lookup_dict:
        look = lookup_dict[str(filename)]
        txt = Main.load_db_functionlevel(self, str(i))
        b=len(look)
        for j in range(len(look)):
          for lookup in look[j]:
            a = lookup
            functionlevel.find_stmt(self, lookup, txt, dictio_func, file_dict, filename)


    for i in db_old_path:

      filename = i.split("/")
      filename = filename[filename.__len__()-1]
      if filename in precommit_lookup_dict:
        look = precommit_lookup_dict[str(filename)]
        txt = Main.load_db_functionlevel(self, str(i))
        b=len(look)
        for j in range(len(look)):
          for lookup in look[j]:
            a = lookup
            functionlevel.find_stmt(self, lookup, txt, dictio_func, file_dict, filename)


    Main.write(self,file_dict,"funtion_basket_result.txt")


  def __init__(self):

    dictio_func={}
    file_dict = {}
    lookup_dict={}
    precommit_lookup_dict = {}

    print("logical dependency is extracting...")

    path = sys.argv[1]
    old_path = sys.argv[2]


    hold_db = open("holder_result.txt", "r").read()
    #old_path = '/home/nazanin/Downloads/ceph_versions/ceph-15.2.1'
    #path = '/home/nazanin/Downloads/ceph_versions/ceph-15.2.2'
    gitdiff_path = 'func_modified.txt'

    db_path = []
    db_old_path =[]
    db_path = functionlevel.initialize(self, path, db_path)
    db_old_path = functionlevel.initialize(self, old_path, db_old_path)
    functionlevel.gitdiff_parser(self,lookup_dict, precommit_lookup_dict, gitdiff_path)
    print("processing...")
    functionlevel.main(self, lookup_dict, precommit_lookup_dict, dictio_func, file_dict, db_path, db_old_path)
    print("processing...")
    holder.hold_write(self,hold_db)
    print("logical dependency is completed!")

p = functionlevel()