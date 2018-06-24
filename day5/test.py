import csv
import os
class test:
    def read(self,filename):
        list = []
        base_parh = os.path.dirname(__file__)
        print(base_parh)
        path = base_parh.replace('day5', 'data/'+filename)
        print(path)
        file = open(path, 'r')
        with open(path, 'r') as file:
            data_table = csv.reader(file)
            for row in data_table:
                print(row)
                list.append(row)
        return list
if __name__=='__main__':
    list = test().read('test_data.csv')
    #print(list[0][1])
