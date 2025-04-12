# # from http.client import responses
# #
# # # import requests
# # # from bs4 import BeautifulSoup as bs
# # #
# # # class Name:
# # #     def __init__(self,url):
# # #         self.url=url
# # #         self.header={
# # #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# # #         }
# # #         self.soup=None
# # #     def auditSite(self):
# # #         response=requests.get(self.url,headers=self.header)
# # #         if response.status_code==200:
# # #             self.soup=bs(response.text,"html.parser")
# # #         else:
# # #             print("Не вдалося підєднатися до сайту")
# # #     def getInfo(self):
# # #         pass
# # #     def showInfo(self):
# # #         pass
# # #
# # # url="xxxxxxx"
# # # obj=Name(url)
# # # obj.auditSite()
# # # site=obj.getInfo()
# # # if site:
# # #     obj.showInfo()
# # # else:
# # #     print("Жодної інформації не отримано")
# #
# # import requests
# # from bs4 import BeautifulSoup as bs
# #
# # class Comfy:
# #     def __init__(self,url):
# #         self.url=url
# #         self.header={
# #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# #         }
# #         self.soup=None
# #     def auditSite(self):
# #         response=requests.get(self.url,headers=self.header)
# #         if response.status_code==200:
# #             self.soup=bs(response.text,"html.parser")
# #         else:
# #             print("Не вдалося підєднатися до сайту")
# #     def getInfo(self):
# #         laptop=[]
# #         lap=self.soup.find_all('div',class_='products-catalog-grid products-catalog--grid-mode')
# #         if not lap:
# #             print('Помилка в пошуку на сторінці')
# #             return laptop
# #         for i in lap[0:4]:
# #             name=i.find('a', class_='prdl-item__name ellipsis-2-lines')
# #             nameErorr=name.text if name else 'Відсутня'
# #             price=i.find('div',class_='products-list-item-price__actions-price-current')
# #             priceErorr = price.text if price else 'Відсутня'
# #             laptop.append({
# #                 'Назва':name,
# #                 'Ціна':price
# #             })
# #         return laptop
# #     def showInfo(self,laptop):
# #         print('№\t','Назва','\t'*2,'Ціна','\t'*2)
# #         print('-'*50)
# #         for i in laptop:
# #             print('\t',i['Назва'],'\t',i['Ціна'])
# #
# # url="https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
# # obj=Comfy(url)
# # print(obj.auditSite())
# # site=obj.getInfo()
# # print("\tНайпопулярніші 4 ноутбуки:\n")
# # if site:
# #     obj.showInfo(site)
# # else:
# #     print("Жодної інформації не отримано")
#
#
#
#
# import requests # запит
# from bs4 import BeautifulSoup as bs
#
# class Coin:
#     def __init__(self, url):
#         self.url = url
#         self.header = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup = None
#
#     def auditSite(self):
#         response = requests.get(self.url, headers=self.header)
#         if response.status_code == 200:
#             self.soup = bs(response.text, features="html.parser")
#         else:
#             print("Не вдалося підключитися до сайту")
#
#     def getInfo(self):
#         coins = []
#         listCoin = self.soup.find('body')
#         if not listCoin:
#             print("Помилка в пошуку на сторінці")
#             return coins
#         info = listCoin.find_all('tr')[0:5]
#         for i in info:
#             name = i.find('p', class_='coin-item-name')
#             name2 = name.text.strip() if name else "Відсутня назва"
#             price = i.find('div', class_='sc-142c02c-0 iMvbGF')
#             price2 = price.text.strip() if price else 'Відсутня ціна'
#             coins.append({
#                 "Назва": name2,
#                 "Ціна": price2,
#             })
#         return coins
#
#     def showInfo(self, coins):
#         print('\t', "НАЗВА", '\t', "ЦІНА")
#         print('-' * 50)
#         num = 1
#         for i in coins:
#             print(num, '\t', i["Назва"], '\t', i["Ціна"])
#             num += 1
#
# url = "https://coinmarketcap.com/"
# obj = Coin(url)
# obj.auditSite()
# site = obj.getInfo()
# print('5 найпопулярніші криптомонети')
# if site:
#     obj.showInfo(site)
# else:
#     print("Жодної інформації не отримано")

"""
from http.client import responses

import requests
from bs4 import BeautifulSoup as bs

class Books:
    def __init__(self,url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response=requests.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text,"html.parser")
        else:
            print("Не вдалося підєднатися до сайту")

    def getInfo(self):
            books=[]
            boo = self.soup.find_all('article', class_='product_pod')
            if not boo:
                print('Помилка в пошуку на сторінці')
                return books
            for i in boo[:8]:
                name = i.h3.a['title']
                price = i.find('p', class_='price_color').text
                rating_class = i.find('p', class_='star-rating')
                rating = rating_class['class'][1] if rating_class else "Відсутній"
                books.append({
                    'Назва':name,
                    'Ціна':price,
                    'Рейтинг':rating
                })
            return books

    def showInfo(self, books):

        print('\t', "НАЗВА", '\t', "ЦІНА")
        print('-' * 50)
        num = 1
        for i in books:
            print(num, '\t', i["Назва"], '\t', i["Ціна"], '\t', i["Рейтинг"])
            num += 1



url="http://books.toscrape.com"
obj=Books(url)
obj.auditSite()
site=obj.getInfo()
if site:
    obj.showInfo(site)
else:
    print("Жодної інформації не отримано")
"""

"""
from http.client import responses

import requests
from bs4 import BeautifulSoup as bs

class New:
    def __init__(self,url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response=requests.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text,"html.parser")
        else:
            print("Не вдалося підєднатися до сайту")

    def getInfo(self):
            rates = []
            rate = self.soup.find_all('div', class_='flex items-center gap-4 text-left font-semibold')
            if not rate:
                print('Помилка в пошуку на сторінці')
                return rates
            for i in rate[:4]:
                name = i.find_previous('div', class_='sc-9070a1f-0 TSFnI ellipser').text.strip()
                rate_value = i.text.strip()
                rates.append({
                    'Назва':name,
                    'Курс':rate_value,
                })
            return rates

    def showInfo(self, rates):
        print('Валюта\tКурс')
        print('-' * 30)
        for rate in rates:
            print(f"{rate['Валюта']}\t{rate['Курс']}")


url="https://www.xe.com/currencyconverter/"
obj=New(url)
obj.auditSite()
site=obj.getInfo()
if site:
    obj.showInfo(site)
else:
    print("Жодної інформації не отримано")
"""
import requests
from bs4 import BeautifulSoup as bs


class Eva:
    def __init__(self,url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response=requests.get(self.url,headers=self.header)
        if response.status_code==200:
            response.encoding = 'utf-8'
            self.soup=bs(response.text,"html.parser")
        else:
            print("Не вдалося підєднатися до сайту")

    def getInfo(self):
            cosmetic = []
            cosm = self.soup.find_all('div', class_='product')
            if not cosm:
                print('Помилка в пошуку на сторінці')
                return cosmetic
            for i in cosm[:10]:
                name = i.find('p', class_='product__title').text.strip()
                price = i.find('span', class_='product__regular-price').text.strip()
                cosmetic.append({
                    'Назва':name,
                    'Ціна':price
                })
            return cosmetic

    def showInfo(self, cosmetic):
        print('Топ-10 товарів:')
        n = 1
        for cosmetic_c in cosmetic:
            print(f"{n}. {cosmetic_c['Назва']} - {cosmetic_c['Ціна']}")
            n += 1
        return cosmetic

    def cofigurator(self,cosmetic):
        cart = []
        while True:
            curent_tovar=input("Який товар ви хочете придбати? (введіть номер): ")
            scilcu=input("Скільки одиниць ви хочете купити? ")
            he=input("Хочете ще щось? (так/ні): ")

            cart.append({
                "Товар":curent_tovar,
                "Кількість":scilcu
            })
            if he == "ні":
                return cart,cosmetic

    def calculator(self,cart,cosmetic):
        print("Ваше замовлення:")
        n = 0
        price = 0
        for i in cart:
            print(f" - {cosmetic[int(cart[n]['Товар'])]['Назва']} x{cart[n]['Кількість']} = {int(''.join(ch for ch in cosmetic[int(cart[n]['Товар'])]['Ціна'] if ch.isdigit())) * int(cart[n]['Кількість'])} грн")
            price+=int(''.join(ch for ch in cosmetic[int(cart[n]['Товар'])]['Ціна'] if ch.isdigit())) * int(cart[n]['Кількість'])
            n+=1
        print("Загальна сума до сплати:", str(price), "грн")



url="https://eva.ua/ua/13557/eva-premium/"
obj=Eva(url)
obj.auditSite()
site=obj.getInfo()
if site:
    s = obj.showInfo(site)
    f = obj.cofigurator(s)
    obj.calculator(f[0],f[1])
else:
    print("Жодної інформації не отримано")