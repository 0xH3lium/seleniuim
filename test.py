from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(r"C:\Users\Rust\Desktop\chromedriver.exe")
driver.get('http://advari.irantvto.ir/index.php/advari_search/search_herfe/98144/0')
time.sleep(3)
driver.find_element("xpath","/html/body/div[7]/table/tbody/tr[2]/td/tempory/div/form/table/tbody/tr[2]/td[2]/select/option[6]").click()
time.sleep(3)
driver.find_element("xpath","/html/body/div[7]/table/tbody/tr[2]/td/tempory/div/form/table/tbody/tr[3]/td[2]/select/option[4]").click()
time.sleep(3)
driver.find_element("xpath","/html/body/div[7]/table/tbody/tr[2]/td/tempory/div/form/table/tbody/tr[4]/td[2]/select/option[8]").click()
time.sleep(3)
a = driver.find_element("xpath","/html/body/div[7]/table/tbody/tr[2]/td/tempory/div/form/table/tbody/tr[6]/td[2]/select")


f = open(r"C:\Users\Rust\Desktop\a.txt","w",encoding="utf-8")
f2 = open(r"C:\Users\Rust\Desktop\b.txt","w",encoding="utf-8")



def xor():
	select = Select(a)
	for index in select.options[1:]:
		print(index.text)
		f.write(index.text.split(":")[0]+'\n')
		f2.write(index.text.split(":")[1]+'\n')

select = Select(a)
xor()

driver.find_element("xpath","/html/body/div[7]/table/tbody/tr[2]/td/tempory/div/form/table/tbody/tr[5]/td[2]/select/option[2]").click()
time.sleep(1)
a = driver.find_element("xpath","/html/body/div[7]/table/tbody/tr[2]/td/tempory/div/form/table/tbody/tr[6]/td[2]/select")
xor()



f.close()
