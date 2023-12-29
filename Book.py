import requests
from PIL import Image, ImageTk
from io import BytesIO


API_KEY = 'AIzaSyAJ1j8sZsZS0ZE5JmrLIh1naLYgRMv7dgQ'
class Book:
    all_info = None
    def __init__(self,id,mark='-',readCountOfPages='0'):
        self.id = id
        self.mark = mark
        self.readCountOfPages = readCountOfPages
        self.all_info = requests.get(f'https://www.googleapis.com/books/v1/volumes/{self.id}?=key{API_KEY}')

        if self.all_info.status_code == 200:
            self.all_info = self.all_info.json()
        else:
            print(f'Error: {self.all_info.status_code}')
        self.title = self.all_info['volumeInfo'].get("title",'Нет информации')
        self.authors = ' '.join(self.all_info['volumeInfo'].get('authors','Нет информации'))
        self.categories = (''.join(self.all_info['volumeInfo'].get("categories",'Нет информации'))
                           .replace(" / General",''))
        self.pageCount = self.all_info['volumeInfo'].get("pageCount",'Нет информации')
        self.publishedDate = self.all_info['volumeInfo'].get("publishedDate",'Нет информации')
        self.description = self.all_info['volumeInfo'].get("description",'Нет информации')

        response = requests.get(self.all_info['volumeInfo']['imageLinks'].get("thumbnail",None))
        if response != None:
            image_data = BytesIO(response.content)
            image = Image.open(image_data).resize((184,274))
            self.icon = ImageTk.PhotoImage(image)