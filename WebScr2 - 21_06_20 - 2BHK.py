import xlsxwriter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request  
from numpy import savetxt
import pandas as pd
import numpy as np
import time

element_list = []
link_list = []
prlst1 = []
prlst2 = []
prlst3 = []
prlst4 = []

page_url = "https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(page_url)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2.0)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2.0)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2.0)

#ProductLink = driver.find_elements_by_xpath("""/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/ul/li[1]/a""")
#for i in  ProductLink:
#    pdtlink = i.get_attribute("target")
#ProductLink = driver.find_elements_by_partial_link_text("_blank")


Price = driver.find_elements_by_class_name("price")
area = driver.find_elements_by_class_name("col-4")
facing = driver.find_elements_by_class_name("col-3")
status = driver.find_elements_by_class_name("col-5")
owner_name = driver.find_elements_by_class_name("owner-name")
owner_posted = driver.find_elements_by_class_name("owner-post")
address = driver.find_elements_by_class_name("filter-pro-heading")
pro_list = driver.find_elements_by_class_name("pro-list")




for i in range(0, len(Price)):
        pro_list1 = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div/div[' +str(i+2)+ ']/div[2]/div[2]/ul/li[1]')
        pro_list2 = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div/div[' +str(i+2)+ ']/div[2]/div[2]/ul/li[2]')
        pro_list3 = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div/div[' +str(i+2)+ ']/div[2]/div[2]/ul/li[3]')
        pro_list4 = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div/div[' +str(i+2)+ ']/div[2]/div[2]/ul/li[4]')
        
        prlst1.append(pro_list1)
        prlst2.append(pro_list2)
        prlst3.append(pro_list3)
        prlst4.append(pro_list4)

print("Name",len(address))

for i in range(0, len(Price)):
        element_list.append([address[i].text, Price[i].text, area[i].text, status[i].text, prlst1[i].text, prlst2[i].text, prlst3[i].text, prlst4[i].text, owner_name[i].text, owner_posted[i].text])


print(len(prlst1)); print(len(prlst2)); print(len(prlst3)); print(len(prlst4))
#for p in range(1, 51):
#    img1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/ul/li["+str(p)+"]/a/div[1]/div/div/div/picture/img")
#    #for i in img1:
#    img_src = img1.get_attribute("src")
#   img_link_list.append(img_src)


with xlsxwriter.Workbook('C:/BHK2.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)


print(element_list)
driver.close()
