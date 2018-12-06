from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

url = 'https://action.hsi.org/page/24986/petition/1?en_chan=tw'
for i in range(1000000000):
    driver = webdriver.Chrome('C:\\Users\\1\\Desktop\\IT\\Programs\\unlimitedemails\\chromedriver')
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_id('en__field_supporter_firstName').send_keys('Alicia')
    driver.find_element_by_id('en__field_supporter_lastName').send_keys('Keys')
    driver.find_element_by_id('en__field_supporter_emailAddress').send_keys('r4p70r1@abv.bg')
    obj = Select(driver.find_element_by_name("supporter.country"))
    obj.select_by_index(1)
    driver.find_element_by_xpath("//button[@class='btn btn-next']").click()
    time.sleep(2)
    driver.quit()


