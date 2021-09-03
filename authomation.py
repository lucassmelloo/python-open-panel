from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class WebController:
    chrome_options = Options()
    chrome_options.add_argument("--kiosk")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://portal.labapoiobrasil.com.br/painel/abrir?id=6&token=Nv2KUvjBg8oaUE0BkCNfzgIKe6arAQsk')
    e = driver.find_element_by_xpath("//*[contains(text(),'Abrir Caixas')]")
    e.click()
