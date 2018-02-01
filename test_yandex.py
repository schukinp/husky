from selene.api import *


def test_yandex():
    browser.open_url('http://www.yandex.ru')
    s('input[aria-label="Запрос"]').set('audi купить')
    s('div.search2__button').click()
    pages = s(by.xpath('//div[@aria-label="Страницы"]'))
    ad = ss('li[aria-label="Реклама"] > div > h2')
    if int(pages.get_attribute('childElementCount')) > 1:
        s(by.xpath('//div[@aria-label="Страницы"][1]')).click()
        if len(ad) > 0:
            for el in ad:
                print(el.text)
        else:
            print('Рекламных блоков нет')
    else:
        print('Страниц меньше 2')


test_yandex()
