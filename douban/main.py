#文件起动爬虫
from scrapy import cmdline
import sys,os
a=os.path.dirname(os.path.abspath(__file__))
sys.path.append(a)
os.chdir(a)
cmdline.execute(['scrapy','crawl','doubancrawer'])