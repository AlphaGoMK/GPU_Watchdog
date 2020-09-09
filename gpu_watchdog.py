import GPUtil
import time
import datetime
import argparse
import sys
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--threshold', type=int, default=1024, help='GPU memory threshold (MB)')
parser.add_argument('--index', type=int, default=0, help='Index of the GPU to be monitored')
opt = parser.parse_args()

sckey = ''  # your sckey
li = []
while True:    
    gpu = GPUtil.getGPUs()[opt.index]
    li.append(gpu.memoryUsed < opt.threshold)
    if sum(li) > 5:
        now = datetime.datetime.now()
        err_info = 'GPU mem drop @ %s'%(now.strftime('%b %d %H:%M'))
        try:
            requests.get('https://sc.ftqq.com/%s.send?text=%s'%(sckey, err_info.replace(' ', '_').replace(':', '_')))
        except:
            print('Send error')
        print('\033[31m%s\033[0m'%err_info)
        sys.exit(0)
    elif len(li) > 5:
        del li[0]

    time.sleep(1)
    