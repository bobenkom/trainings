from urllib.request import urlopen
from bs4 import BeautifulSoup

def parsing(link: str) -> str:
    """
    Parses one page where url == link that contains 50 movies
    Returns part of future csv file containing info about 50 movies
    :return str
    """
    cvs_part = ''
    link = urlopen(link)
    bsObj = BeautifulSoup(link, features="html.parser")
    film_name = bsObj.findAll("p", {"class": "selection-film-item-meta__name"})
    film_info = bsObj.findAll("span", {"class": "selection-film-item-meta__meta-additional-item"})
    film_rating = bsObj.findAll("span", {"class": "rating__value rating__value_positive"})
    n = 0
    for i in range(0, len(film_name)):
        cvs_part += film_name[i].get_text + '; ' + film_info[n].text + '; ' + film_info[n + 1].text + '; ' + film_rating[i].text + '\n'
        n += 2  # because film info alternate [country, genre, country, genre...]
    return cvs_part


def main():
    csv = 'name; country; genre; rating\n'
    file = open('name.csv', 'w')
    for pagenumber in range(1,6):
        file.write(csv)
        csv = parsing('https://www.kinopoisk.ru/lists/top250/?page=' + str(pagenumber))
    file.write(csv)
    file.close()


if __name__ == '__main__':
    main()

