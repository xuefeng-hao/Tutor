import os
import openpyxl

def class_file_name(file_dir, file_type):
    '''
    get file names with specific type
    :param file_dir: the given directory
    :param file_type: the wanted file type
    :return:list of all files with specific type
    '''
    ls = []
    f = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == file_type:
                ls.append(os.path.join(root, file))
                file=file.rstrip(".mp3")
                f.append(file)
    return f

def output2excel(file_dir):
    '''
    Output the names of the files in the folder to the file directory
    :param file_dir: 
    :return:
    '''
    # Get the names of all the files in the file directory and store them in the data list
    data = class_file_name(file_dir,'.mp3')

    # Export data to that directory and save it in excel format with the directory name
    wb = openpyxl.Workbook()
    sheet = wb.active
    # Set table name to file directory name
    sheet.title = file_dir
    for i in range(1, len(data) + 1):
        sheet['A{}'.format(i)] = data[i - 1]

    if file_dir == '.':
        file_dir_name = 'mp3_list'
    wb.save('./{0}.xlsx'.format(file_dir_name))


file_dir = '.'
output2excel(file_dir)
