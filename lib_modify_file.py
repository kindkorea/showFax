from pdf2image import convert_from_path
import os
import glob 

class Modify_file():
    def __init__(self,path):
        self.src_path = path
        self.load_files = glob.glob(self.src_path+'/*.*')
        # self.dest_path_month = ''
        # print(f'created Modify_file class {len(self.load_files)=}')

    def __most_recent_pdf(self):

        pdf_file_list = [file for file in self.load_files if file.endswith('.pdf' and '.PDF')]

        if not pdf_file_list :
            print(f'NO PDF file in {self.src_path}')
        else :
            
            pdf_files_with_time =[]
            for pdf_file in pdf_file_list:
                pdf_files_with_time.append((pdf_file,os.path.getctime(pdf_file)))
            
            return max(pdf_files_with_time,key=lambda x: x[1])[0]
        

    def __cmd_re_name(self,src_file, dest_path, change_filename):
        
        file_name_ext = os.path.basename(src_file)
        file_name, file_ext = os.path.splitext(file_name_ext)
        file_path = f'{dest_path}/{change_filename}'
        rename = f'{file_path}/{change_filename}{file_ext}'
        
        self.__cmd_createDirectory(file_path)
        os.startfile(file_path)
        if os.path.exists(rename):
            print(f"{rename} is exist")
        else :    
            os.rename(src_file , rename)
            return rename

    def __cmd_createDirectory(self,directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Error: Failed to create the directory.")

    def pdf_to_jpg(self, dest_path, change_filename):
        
        try : 
            most_recent_pdf = self.__most_recent_pdf()
     
            pages = convert_from_path(most_recent_pdf, dpi=200)
            output_filelist = []  
            file_path = f'{dest_path}/{change_filename}'

            self.__cmd_createDirectory(file_path)
            os.startfile(file_path)

            for i, page in enumerate(pages):
                o_filename = f"{file_path}/{change_filename}#{str(i)}.jpg" 
                page.save(o_filename, "JPEG")
                output_filelist.append(o_filename)

            return  output_filelist
        except :
            print("No PDF file.")

    def pdf_rename(self, dest_path, change_filename):
        src_file  = self.__most_recent_pdf()
        
        if not src_file :
            print("there is no file")

        else : 
            return self.__cmd_re_name(src_file, dest_path, change_filename)

    def reset(self):
        self.load_files=''
        self.load_files = glob.glob(self.src_path+'/*.*')
        print(f'reset : {len(self.load_files)=}')


   


# data1 = Modify_file('c:/Users/kindk/Downloads/')
# files = data1.pdf_to_jpg('c:/Users/kindk/Downloads/','hello')
# files = data1.reset()
# print(f'{files}')

# print(data1.load_files)


# convert_jpg('c:/Users/kindk/Downloads/','c:/Users/kindk/Downloads/','hello')

