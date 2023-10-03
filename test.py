import os
import subprocess
import glob

src_path = './img'
# print(f'{src_path=}')
load_files = glob.glob(src_path+'/*.*')
jpg_file_list = [file for file in load_files if file.endswith('.jpg')]

# for file in jpg_file_list : 

noChk_file_list = [file for file in jpg_file_list if os.path.basename(file)[0] != 'v']
print(f'{noChk_file_list=}')



for file in noChk_file_list:
    print(f'{file=}')
    subprocess.run(f'C:/Users/kindk/AppData/Local/Imagine/Imagine64.exe {file}')