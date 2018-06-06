# coding: utf-8
# 本项目采用selenium来爬取淘宝数据，默认使用火狐浏览器
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyExcelerator import *

# 打开浏览器

result = []
driver = webdriver.Firefox()
keyword = raw_input('Please enter key words:')
if keyword != '':
    URL = 'https://www.taobao.com'
    # 打开爬取页面
    driver.get(URL)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "J_TSearchForm"))
        )
        # 找到输入框并输入查询内容
        elem = driver.find_element_by_class_name('search-combobox-input')
        elem.send_keys(keyword.decode('GBK'))
        # 点击搜索
        driver.find_element_by_class_name('btn-search').click()
        num = 0
        while True:
            time.sleep(3)
            num += 1
            print(num)
            # # 打开爬取页面
            # driver.get(driver.current_url)
            # 隐形等待，最长等待3秒
            driver.implicitly_wait(3)
            # 拖动到页面最底部，=0为拖动到页面最顶部
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)
            # 下一页按钮
            nextbtn = driver.find_element_by_css_selector('span.J_Submit')
            # driver.page_source可以获取当前源码，用BeautifulSoup解析网页
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            content = soup.select('#mainsrp-itemlist .grid .items .item')
            if len(content):
                for item in content:
                    data = {}
                    if len(item.select('.ctx-box .row-1 .price strong')):
                        data['price'] = item.select('.ctx-box .row-1 .price strong')[0].string
                    if len(item.select('.pic-box .pic-box-inner .pic a img')):
                        data['title'] = item.select('.pic-box .pic-box-inner .pic a img')[0]['alt']
                    if len(item.select('.ctx-box .row-3 .location')):
                        data['location'] = item.select('.ctx-box .row-3 .location')[0].string
                    if len(item.select('.ctx-box .row-2 a')):
                        data['url'] = item.select('.ctx-box .row-2 a')[0]['href']
                    result.append(data)
                print(len(result))
                if num > 1:
                    break
                if nextbtn:
                    nextbtn.click()
                else:
                    break
    finally:
        w = Workbook()  # 创建一个工作簿
        ws = w.add_sheet('1')  # 创建一个工作表
        for j in range(0, 4):  # 控制列
            for i, item in enumerate(result):  # 控制行
                if j == 0:  # 第一列
                    ws.write(i, j, item['price'])
                if j == 1:
                    ws.write(i, j, item['title'])
                if j == 2:
                    ws.write(i, j, item['location'])
                if j == 3:
                    ws.write(i, j, item['url'])
        w.save(keyword + '.xls')
        driver.quit()
