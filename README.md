# GPU Watchdog
Detect the end of training process or program failure (eg. out of mem) by monitoring GPU memory usage, and send notifications by WeChat official account: 方糖.    

### Requirements
1. Python 3.6+
2. GPUtil 1.4.0

### Usage
1. Register and get SCKEY at [Server酱](sc.ftqq.com)  
2. Run `python gpu_watchdog.py --threshold 1024 --index 0`  

```shell
usage: gpu_watchdog.py [-h] [--threshold THRESHOLD] [--index INDEX]

optional arguments:
  -h, --help            show this help message and exit
  --threshold THRESHOLD
                        GPU memory threshold (MB)
  --index INDEX         Index of the GPU to be monitored
```

Contact me: alphagomk at foxmail dot com