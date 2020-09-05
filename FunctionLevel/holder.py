
class holder:


    def hold_write(self,hold_db):
        self.hold_db = hold_db
        data = open('funtion_basket_result.txt','r').read()
        hold_db = hold_db + data
        print(hold_db)
        with open("holder_result.txt","w") as handler:
            handler.write(hold_db)
