import csv
#每个测试用例对应不同的csv文件
#每条测试用例都会打开一个csv文件,所以每次也应该关闭该文件
class CsvFileManager3:
    @classmethod
    def read(self):
        path=r'D:\yss\zdjb\data\test_data.csv'
        file=open(path,'r')
        try: #异常处理,try尝试执行一下代码
            data_table=csv.reader(file)
            a=[2,3,4,5,6]
            a[6] #这时可能发送数组下标越界
            #如何保证,不论程序执行过程中是否报错,都能正常关闭该文件
            for item in data_table:

                print(item)
            #方法最后应该添加close方法
            #file.close()
        finally:  #最终无论执行过程是否报错,都会执行以下代码

            file.close()
            print("file.close() method is executed")
#测试一下这个方法:
if __name__ == '__main__':#前后都有双下划线,说明是python内置的变量,一般都是常量
    # csvr=CsvFileManager2()
    # csvr.read()
#如果在方法上面加上classmethod,表示这个方法可以直接用类调用
#如果在方法上写一个classmethod,就不需要先实例化对象后,才能调用
    CsvFileManager3.read()