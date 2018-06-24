import csv
#把读取文件的代码封装成一个方法
class CsvFileManager2:
    @classmethod
    def read(self):
        path=r'D:\yss\zdjb\data\test_data.csv'
        file=open(path,'r')
        #通过csv代码库读取打开的文件,获取到文件中的所有数据
        data_table=csv.reader(file)
        #data_table中,有几行数据,就会执行几次
        for item in data_table:
            print(item)
#测试一下这个方法:
if __name__ == '__main__':
    # csvr=CsvFileManager2()
    # csvr.read()
#如果在方法上面加上classmethod,表示这个方法可以直接用类调用
#如果在方法上写一个classmethod,就不需要先实例化对象后,才能调用
    CsvFileManager2.read()