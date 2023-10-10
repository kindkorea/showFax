import os
from datetime import datetime
import time

src_file_name222= 'c:/Users/kindk/.vscode/ocProject/exam/1234.gif '
refilename222 = '웅천목재'

class FaxFile :
    def __init__(self,src_file,is_checked):
        self.__src_file = src_file    
        self.__is_checked = is_checked

    @property
    def checked(self):
        return self.__is_checked
    
    @checked.setter
    def checked(self,is_checked):
        self.__is_checked = is_checked

    def FAX_rename(self,dst_file) :
        try :
            #파일 생성일자를 업체명 뒤에 붙임
            creation_time = time.gmtime(os.path.getctime(self.__src_file))
            file_ctime = time.strftime("%Y_%m_%d", creation_time)

            #소스 파일을 파일, 확장자로 쪼갬
            file_path, file_name_ext = os.path.split(self.__src_file)
            file_name , file_ext = os.path.splitext(file_name_ext)

            #새로 변경할 파일명을 조립함
            try :
                dst_file_name = f'{file_path}/{dst_file}_{file_ctime}{file_ext}'
                os.rename(self.__src_file,dst_file_name)
            except FileExistsError :
                print(f'{dst_file_name} is exited')
        except FileNotFoundError :
            print(f'{self.__src_file} is not found')


classList = []
for i in range(10) :
    # print(i)
    classList.append(FaxFile(src_file_name222,i))
# faxfile = FaxFile(src_file_name222,0)
# faxfile.FAX_rename(refilename222)

for faxClass in  classList :
    print(f'{faxClass.checked}')