from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_find_button(driver):
    driver.get(link)
    buttons = driver.find_elements(By.CSS_SELECTOR, "[type='submit']")
    assert len(buttons) > 0, "Кнопка 'добавить в корзину' не найдена"
