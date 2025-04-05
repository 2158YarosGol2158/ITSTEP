# from http.client import responses
#
# # import requests
# # from bs4 import BeautifulSoup as bs
# #
# # class Name:
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
# #         pass
# #     def showInfo(self):
# #         pass
# #
# # url="xxxxxxx"
# # obj=Name(url)
# # obj.auditSite()
# # site=obj.getInfo()
# # if site:
# #     obj.showInfo()
# # else:
# #     print("Жодної інформації не отримано")
#
# import requests
# from bs4 import BeautifulSoup as bs
#
# class Comfy:
#     def __init__(self,url):
#         self.url=url
#         self.header={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#     def auditSite(self):
#         response=requests.get(self.url,headers=self.header)
#         if response.status_code==200:
#             self.soup=bs(response.text,"html.parser")
#         else:
#             print("Не вдалося підєднатися до сайту")
#     def getInfo(self):
#         laptop=[]
#         lap=self.soup.find_all('div',class_='products-catalog-grid products-catalog--grid-mode')
#         if not lap:
#             print('Помилка в пошуку на сторінці')
#             return laptop
#         for i in lap[0:4]:
#             name=i.find('a', class_='prdl-item__name ellipsis-2-lines')
#             nameErorr=name.text if name else 'Відсутня'
#             price=i.find('div',class_='products-list-item-price__actions-price-current')
#             priceErorr = price.text if price else 'Відсутня'
#             laptop.append({
#                 'Назва':name,
#                 'Ціна':price
#             })
#         return laptop
#     def showInfo(self,laptop):
#         print('№\t','Назва','\t'*2,'Ціна','\t'*2)
#         print('-'*50)
#         for i in laptop:
#             print('\t',i['Назва'],'\t',i['Ціна'])
#
# url="https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
# obj=Comfy(url)
# print(obj.auditSite())
# site=obj.getInfo()
# print("\tНайпопулярніші 4 ноутбуки:\n")
# if site:
#     obj.showInfo(site)
# else:
#     print("Жодної інформації не отримано")




import requests # запит
from bs4 import BeautifulSoup as bs

class Coin:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, features="html.parser")
        else:
            print("Не вдалося підключитися до сайту")

    def getInfo(self):
        coins = []
        listCoin = self.soup.find('body')
        if not listCoin:
            print("Помилка в пошуку на сторінці")
            return coins
        info = listCoin.find_all('tr')[0:5]
        for i in info:
            name = i.find('p', class_='coin-item-name')
            name2 = name.text.strip() if name else "Відсутня назва"
            price = i.find('div', class_='sc-142c02c-0 iMvbGF')
            price2 = price.text.strip() if price else 'Відсутня ціна'
            coins.append({
                "Назва": name2,
                "Ціна": price2,
            })
        return coins

    def showInfo(self, coins):
        print('\t', "НАЗВА", '\t', "ЦІНА")
        print('-' * 50)
        num = 1
        for i in coins:
            print(num, '\t', i["Назва"], '\t', i["Ціна"])
            num += 1

url = "https://coinmarketcap.com/"
obj = Coin(url)
obj.auditSite()
site = obj.getInfo()
print('5 найпопулярніші криптомонети')
if site:
    obj.showInfo(site)
else:
    print("Жодної інформації не отримано")