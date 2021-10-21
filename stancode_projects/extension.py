"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'
        respond = requests.get(url)
        html = respond.text
        soup = BeautifulSoup(html)

        items = soup.find_all('table', {'class': 't-stripe'})
        for item in items:
            table_content = item.tbody.text
            token_lst = table_content.split()
            m_total = 0
            fm_total = 0
            for i in range(200):
                m_num = token_lst[2 + i*5].replace(',', '')
                m_total += int(m_num)
                fm_num = token_lst[4 + i*5].replace(',', '')
                fm_total += int(fm_num)
            print('Male Number:', m_total)
            print('Female Number:', fm_total)

    # replace() refer to 'https://blog.csdn.net/zdz0200/article/details/81453367'


if __name__ == '__main__':
    main()
