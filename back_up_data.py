import os
import os.path, time
from datetime import datetime
from dateutil.relativedelta import relativedelta
in_path_dir = '/home/loint/logs/'
in_path_log = '/home/loint/test_log/'
arr = os.listdir(in_path_dir)
date_after_month = datetime.today()+ relativedelta(months = -1)
#if dir not exit, create dir
if os.path.isdir(in_path_log+ date_after_month.strftime('%Y%m')):
    print("dir is exits!")
else:
    print("dir is not exits! create dir: %s" % in_path_log+ date_after_month.strftime('%Y%m'))
    os.mkdir(in_path_log+ date_after_month.strftime('%Y%m'))
for i in arr:
    #if date yyyyMM modified of file == before month yyyyMM then move file to log folder
    if time.strftime('%Y%m',time.gmtime(os.path.getmtime(in_path_dir + i))) == date_after_month.strftime('%Y%m'):
        os.rename(in_path_dir + i, in_path_log+ date_after_month.strftime('%Y%m') + "/" + i)
        print("move file:" + in_path_dir + i + " to " + in_path_log + date_after_month.strftime('%Y%m') + "/" + i)

#print("last modified: %s" % time.ctime(os.path.getmtime(file)).strftime('%Y%m'))