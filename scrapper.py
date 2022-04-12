# importing libraries
import selenium
from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Opening Chrome browser
wbD = wb.Chrome('./chromedriver')

# Opening webpage
wbD.get(
    'https://www.amazon.in/s?bbn=1389396031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389375031%2Cn%3A1389396031%2Cn%3A15747864031&dc&fst=as%3Aoff&qid=1596287247&rnid=1389396031&ref=lp_1389396031_nr_n_1')

# Running loop to store the product links in a list
listOflinks = []
condition = True
while condition:
    productInfoList = wbD.find_elements_by_class_name('a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4')
    for el in productInfoList:
        if (el.text != "" and el.text != "Sponsored"):
            pp2 = el.find_element_by_tag_name('a')
            listOflinks.append(pp2.get_property('href'))
    try:
        wbD.find_element_by_class_name('a-last').click()
    except:
        continue

    if len(listOflinks) >300:
        condition=False

print(len(listOflinks))
rows = []
for el in listOflinks:

    try:
        wbD.get(el)
        title = wbD.find_element_by_class_name("a-size-large.product-title-word-break").text
        price = wbD.find_element_by_class_name("a-size-medium.a-color-price.priceBlockDealPriceString").text
        size = wbD.find_element_by_xpath('// *[ @ id = "productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span').text
        supported_internet_services = wbD.find_element_by_xpath('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[2]/td[2]/span').text
        connector = wbD.find_element_by_xpath('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[3]/td[2]/span').text
        brand = wbD.find_element_by_xpath('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[4]/td[2]/span').text
        resolution = wbD.find_element_by_xpath('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[5]/td[2]/span').text
        temp = {
            'Title': title,
            'size': size,
            'supported internet service': supported_internet_services,
            'Price': price,
            'Brand': brand,
            'connector': connector,
            'resolution': resolution}
        rows.append(temp)
    except:
        continue

df = pd.DataFrame(rows)
df.to_csv("Amazon_tv.csv",index=False)