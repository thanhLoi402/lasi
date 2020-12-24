import os
#in_path_dir = '/home/loint/python/'
#in_path_log = '/home/loint/test_log/'
#old_format = '<date>;<time>;<name>;[<ma>;<value1>;<value2>]'
#new_format = '<name>;<ma>;<date>;<value2>;<time>;<value1>'
def change_format(in_path_dir, in_path_log, old_format, new_format):
    new_arr = new_format.split(';')
    len_for = 0
    if '[' in old_format:
        base_template = old_format[0:old_format.index('[')-1].split(';')
        for_template = old_format[(old_format.index('[')+1): (len(old_format) -1)].split(';')
        len_for = len(for_template)
    print('base_template:' , base_template)
    print('for_template:' , for_template)
    arr = os.listdir(in_path_dir)
    patten = ''
    for i in arr:
        if i == 'getLogCharge.sh':
            f = open(i, 'r')
            f_print = open(in_path_log + i, 'w')
            for x in f:
                if ' ' in x:
                    patten = ' '
                elif ';' in x:
                    patten = ';'
                elif ',' in x:
                    patten = ','
                else:
                    patten = ';'
                x = x.replace(' ',';').replace(',',';')
                arr_x = x.split(';')
                base_data = arr_x[0:len(base_template)]
                for_data = arr_x[len(base_template):len(arr_x)]
                print('base_data:' , base_data)
                print('for_data:' , for_data)
                j = 0
                while j < len(for_data):
                    new_line = '';
                    for idx in new_arr:
                        if idx in base_template:
                            new_line+= base_data[base_template.index(idx)] + patten
                        if idx in for_template:
                            new_line+= for_data[j + for_template.index(idx)] + patten
                    print("new_line:"+ new_line)
                    f_print.write(new_line + '\n')
                    j = j + len_for
            f_print.close()
            os.remove(i)
            print('read and remove done file ' + in_path_dir + i + ' to ' + in_path_log + i)