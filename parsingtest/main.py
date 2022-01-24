from urllib.request import urlopen
from bs4 import BeautifulSoup

def parsing(link):
    cvs_part = ''
    name = []
    country = []
    genre = []
    rating = []
    link = urlopen(link)
    bsObj = BeautifulSoup(link, features="html.parser")
    film_name = bsObj.findAll("p", {"class": "selection-film-item-meta__name"})
    for n in film_name:
        name.append(n.get_text())
    film_country = bsObj.findAll("span", {"class": "selection-film-item-meta__meta-additional-item"})
    temporary = []
    for i in film_country:
        temporary.append(i.get_text())
    for i in range(0, len(temporary)):
        if i % 2 == 0:
            country.append(temporary[i])
        else:
            genre.append(temporary[i])
    film_rating = bsObj.findAll("span", {"class": "rating__value rating__value_positive"})
    for r in film_rating:
        rating.append(r.get_text())
    for i in range(0, len(name)):
        cvs_part += name[i] + '; ' + country[i] + '; ' + genre[i] + '; ' + rating[i] + '\n'
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

