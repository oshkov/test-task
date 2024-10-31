# Тестовое задание на позицию Junior Backend разработчик (Python) в MillionAgents

## Секция 1. Практическое задание Python/Ruby

### 1.1 Экранирование

Необходимо написать 3 класса для экранирования следующих данных на ruby или python без использования сторонних библиотек или сервисов:

1. Электронная почта. 

Экранировать нужно название почтового ящика, не домен.

Возможно указать следующие параметры при инициализации класса:

  а. Символ для экранирования, например "x" (aaa@aaa.com -> xxx@aaa.com)

Обязательно соблюдение количества символов для экранирования, то есть при aaaa@aaa.com должно получиться xxxx@aaa.com, а не xxx@aaa.com

2. Номер телефона. 

Экранировать нужно последние n символов, ОБЯЗАТЕЛЬНО сохранение пробелов в этом случае. Возможно указать следующие параметры при инициализации класса:

  а. Символ для экранирования, например "x" (+7 666 777 888 -> +7 666 777 xxx);

  б. Количество символов для экранирования (по умолчанию - 3)

Пробелы должны быть сохранены в оригинале, но при выводе должны сокращаться до одного. То есть, при запросе на экранирование с номером телефона "+7 666 777       888" и при выборе длины экранирования в 5 символов, должно выводиться "+7 666 7xx xxx"

3. Skype.

Обрабатывать нужно как обычные строки "skype:alex.max", так и ссылки, вроде "<a href=\"skype:alex.max?call\">skype</a>".

Результат в первом случае должен получиться "skype:xxx", а во втором - "<a href=\"skype:xxx?call\">skype</a>".

В данном случае не нужно учитывать длину экранируемой строки.


### 1.2 Короткие ссылки

Создать сервис для укорачивания ссылок и редиректа на оригинальную ссылку с короткой. Предусмотреть хранилище для укороченных ссылок, защиту от перебора, редирект с укороченной ссылки на оригинальную. Стек по желанию: либо python/uvicorn, либо ruby/ror. Без использования сторонних библиотек или сервисов.


## Секция 2. Практическое задание SQL/PostgreSQL

### 2.1. Дана таблица:

```
CREATE TABLE reports

(
    id int PRIMARY KEY,

    user_id int,

    reward int,

    created_at timestamp without time zone
) 
```

Необходимо: выбрать всех пользователей (user_id), которые впервые создали отчет в 2021-м году, и подсчитать сумму вознаграждений (reward) за 2022-й год в одном запросе.


### 2.2. Даны таблицы:
```
CREATE TABLE pos

(
    id int PRIMARY KEY,

    title character varying
)
```

```
CREATE TABLE reports

(
    id int PRIMARY KEY,

    barcode character varying,

    price float,

    pos_id int
)
```

Необходимо: использовав агрегатные функции, выбрать все шк и цены (reports.barcode, reports.price) с одинаковыми названиями точек продаж (pos.title).