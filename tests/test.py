from  pages.base_page import  BasePage


def  test(driver):
    page = BasePage(driver, "https://github.com/Mirtalll/Avto-test-on-python")
    page.open()