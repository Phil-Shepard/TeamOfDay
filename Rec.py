import requests
import random

def Recomendations(Lib):
    if len(Lib) == 0:
        return None
    category = random.choice(list(set(i.categories for i in Lib)))
    index = random.randint(0,requests.get(f"https://www.googleapis.com/books/v1/volumes?q=subject:{category}"
                                          f"&key={API_KEY}").json()['totalItems'])
    return requests.get(f"https://www.googleapis.com/books/v1/volumes?q=subject:{category}"
                        f"&langRestrict=ru&maxResults=1&startIndex={index}&key={API_KEY}").json()


# Апи ключ
API_KEY = 'AIzaSyAJ1j8sZsZS0ZE5JmrLIh1naLYgRMv7dgQ'

# Получение рекомендации
# rec = Book.Book(Recomendations(Library).get('items', [{}])[0].get('id'))


