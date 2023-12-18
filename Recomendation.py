import requests
import random

class Book:
    all_info = None

    def __init__(self,id):
        self.id = id
        self.all_info = requests.get(f'https://www.googleapis.com/books/v1/volumes/{self.id}?=key{API_KEY}')

        if self.all_info.status_code == 200:
            self.all_info = self.all_info.json()
        else:
            print(f'Error: {self.all_info.status_code}')

    def get_all_info(self):
        return self.all_info
    def get_title(self):
        return self.all_info['volumeInfo'].get("title",'Нет информации')

    def get_authors(self):
        return self.all_info['volumeInfo'].get('authors','Нет информации')

    def get_categories(self):
        return ''.join(self.all_info['volumeInfo'].get("categories",'Нет информации')).replace(" / General",'')

    def get_pageCount(self):
        return self.all_info['volumeInfo'].get("pageCount",'Нет информации')

    def get_publishedDate(self):
        return self.all_info['volumeInfo'].get("publishedDate",'Нет информации')

    def get_description(self):
        return self.all_info['volumeInfo'].get("description",'Нет информации')

    def get_icon(self):
        return self.all_info['volumeInfo']['imageLinks'].get("medium")

def Recomendations(Lib):
    if len(Lib) == 0:
        return None
    category = random.choice(list(set(i.get_categories() for i in Lib)))
    index = random.randint(0,requests.get(f"https://www.googleapis.com/books/v1/volumes?q=subject:{category}"
                                          f"&key={API_KEY}").json()['totalItems'])
    return requests.get(f"https://www.googleapis.com/books/v1/volumes?q=subject:{category}"
                        f"&langRestrict=ru&maxResults=1&startIndex={index}&key={API_KEY}").json()


# Апи ключ
API_KEY = 'AIzaSyAJ1j8sZsZS0ZE5JmrLIh1naLYgRMv7dgQ'

# Все книги пользователя должны быть занесены в этот список в виде Book со своим id в GoogleBook
Library = [Book('0NchAwAAQBAJ'),Book('fIyWTKDlMnAC'),Book('86xhAwAAQBAJ')]

# Получение рекомендации
rec = Book(Recomendations(Library).get('items', [{}])[0].get('id'))

# Пример вывода
print(rec.get_title())
