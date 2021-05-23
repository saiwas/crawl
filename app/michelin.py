#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import pandas as pd

def main():
  domain = "https://guide.michelin.com"
  url = domain + "/hk/zh_HK/hong-kong-region/hong-kong/restaurants"
  result = []
  request_url = ""

  for x in range(1,12):
    if x == 1:
      request_url = url
    else:
      request_url = url + "/page/" + str(x)

    print(request_url)
    html_content = requests.get(request_url).text
    soup = BeautifulSoup(html_content, "lxml")
    cards = soup.find_all("div", attrs={"class": "col-md-6 col-lg-6 col-xl-3"})
    # print(cards)
    for card in cards:
      restaurant_link_tag = card.find("h3").find('a')
      restaurant_link = domain + restaurant_link_tag['href']
      restaurant_name = restaurant_link_tag.text.strip()
      restaurant_type = card.find("div", attrs={"class": "card__menu-footer--price pl-text"}).text.strip()

      print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx: " + restaurant_name)

      html_content = requests.get(restaurant_link).text
      soup = BeautifulSoup(html_content, "lxml")
      info = soup.find("div", attrs={"class": "restaurant-details__heading d-none d-lg-block"})
      address = info.find("li").text.strip()
      price = info.find("li", attrs={'class': 'restaurant-details__heading-price'}).text.replace(" ", '').replace("\n", "")
      result.append([restaurant_name, restaurant_link, restaurant_type, address, "page - " + str(x), price])

  print(result)
  df = pd.DataFrame(result)
  df.columns = ['店名','链接','类型','地址', '页码', '人均']
  df.to_csv('restaurants.csv')

if __name__ == '__main__' :
  main()
