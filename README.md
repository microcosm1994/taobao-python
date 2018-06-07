##### 安装Selenium、BeautifulSoup、pyExcelerator

```
pip install selenium
pip install BeautifulSoup
pip install pyExcelerator
```

#### 引用
```
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyExcelerator import *

# 打开浏览器
driver = webdriver.Firefox()
# 打开爬取页面
driver.get("http://www.python.org")
# 找到输入框并输入查询内容
elem = driver.find_element_by_class_name('search-combobox-input')
elem.send_keys(keyword.decode('GBK'))
# 清楚内容
elem.clear()
# 关闭浏览器
driver.quit()
driver.close()
```

另附Selenium官方文档地址与翻译地址 
<a href='http://selenium-python-zh.readthedocs.io/en/latest/getting-started.html'>Selenium翻译地址</a>
<a href='http://selenium-python.readthedocs.io/installation.html'>Selenium官方文档</a>