# Техническое задание по проекту «Создание системы индивидуальной библиотеки с помощником на основе нейронных сетей» команда TeamOfDay

**Представление о продукте:**

Приложение электронная библиотека с голосовым помощником, в котором пользователь может создать свою собственную библиотеку книг, вести заметки, оценки, текущее состояние прочтения книги, отзывы и выбирать книги для прочтения, исходя из системы рекомендаций на основе нейросетей.

# Функционал:

Пользователю должны быть предоставлены такие функции как:

**Карточка книги**

•	Добавление книги вручную, либо по штрих(QR)-коду.

•	Автоматическое создание карточки книги с информацией о ней. Возможность пользователю самостоятельно изменять параметры, обложку книги (Если представленное не устраивает).

•	Введение заметок в карточке книги.

•	Отметка о состоянии книги: Читаю (с номером страницы), Прочитано, Собираюсь прочитать, Бросил.

•	Добавление карточки книги в соответствующую папку (описаны пунктом выше).

•	Добавление книги в виде текстового файла (txt, pdf).

•	5-звёздночная оценка книги.

**Читалка**

•	Режим чтения файла с возможностью кастомизации фона и шрифта. 

•	Запоминание страницы, где остановился пользователь.

# Рекомендации

•	Создание отдельного блока с рекомендациями книги.

•	Возможность выставить предпочтения по жанре, дате, периоду.

•	На основе прочитанных книг и предпочтений предлагать книги из открытой базы книг с автоматически созданной карточкой.

•	На карточке рекомендованной книги должна быть основная информация об книге и краткое вступление.

•	Возможность добавить рекомендованную книгу в свою библиотеку.

•	Возможность отклонить рекомендацию и предоставление следующей.
# Голосовой помощник

•	Возможность при помощи голоса добавить новую книгу, изменить параметр или состояние существующей.

•	Добавление заметок без или с привязкой к книге.

•	Ориентация по базе параметров имеющихся книг. (Например, в какой году был написан роман «Война и мир»?).

•	Переадресация на рекомендации при соответствующем запросе.

# Достижения
•	Система поощрения, основанная на статистике пользователя. Кол-во прочитанных книг, страниц, жанров, писателей. Возможность посмотреть статистику.


# Основные фишки:
	1. Голосовой ассистент, который может стать полноценной заменой в введении личной библиотеки.
	2. Собственная система рекомендаций, созданная при помощи развития навыка у нейронной сети.
	3. Интеграция с бесплатными электронными библиотеками (Даёт возможность добавление обложки, сведений о книге, краткое вступление).
	4. Интуитивно-понятный интерфейс папок, карточек книг и рекомендаций.

# Ориентировочный стек:

•	Сама библиотека: Python, Flask или Django


•	База данных: MongoDB или PostgreSQL либо хранение в видео объекта.


•	Голосовой помощник: библиотека SpeechRecognition, либо Sphinx.


•	Система рекомендаций: Языковая модель GPT либо TensorFlow или PyTorch.





