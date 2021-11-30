import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_on_page(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button_add_to_basket = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    except:
        assert button_add_to_basket.is_displayed() == True, "Кнопка отсутствует"