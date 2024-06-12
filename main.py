from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://www.urbanoutfitters.com/womens-clothing")

driver.get("https://www.urbanoutfitters.com/shop/uo-bri-double-bow-satin-mini-dress?category=womens-clothing&color=015&viewcode=b")
driver.implicitly_wait(30)
print(driver.title)

l = driver.find_elements(By.TAG_NAME, "img")
print(l)

for img in l:
    src = img.get_attribute('src')
    alt = img.get_attribute('alt')
    if alt.startswith('UO Bri Double Bow Satin Mini Dress') : 
        print(f'Src: {src}, Alt: {alt}')


# for x in l : 
#     k = x.get_property('href')
#     k = k.split('https')
#     # print(k,type(k))
#     links = []
#     if k[1].startswith('://www.urbanoutfitters.com/shop/') : 
#         # print(lin[1])
#         links.append('https' + k[1])
    
    # print

    # for y in links : 
    #     print(y)
    #     driver.get("y")
    #     print(driver.title)

    # for x in k[1]: 
        # print
        
    # k = k.split('\n')
    # print(k,type(k))
    # for y in k : 
        # if y.startswith('https://www.urbanoutfitters.com/shop') : 
            # print(y)
        # else : 
            # print(y,end='\n\n')

