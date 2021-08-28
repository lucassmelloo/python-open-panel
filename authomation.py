from selenium import webdriver


class WebController:
    driver = webdriver.Chrome()
    driver.get('http://portal.labapoiobrasil.com.br/painel/abrir?id=6&token=Nv2KUvjBg8oaUE0BkCNfzgIKe6arAQsk')
    e = driver.find_element_by_xpath("//*[contains(text(),'Abrir Caixas')]")
    e.click()
