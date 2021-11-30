import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_on_page(browser):
    browser.get(link)
    time.sleep(5)
    button_add_to_basket = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button_add_to_basket) == 1, "Кнопка отсутствует"