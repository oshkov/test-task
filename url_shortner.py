'''
Секция 1. Практическое задание Python/Ruby

1.2 Короткие ссылки
'''


from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse


app = FastAPI(title='URL_Shortner')

temp_database = {}  # Временная бд


@app.post('/create-url')
async def create_url(url: str):
    try:
        # Проверка на наличия 'http://' в начале ссылки
        if url[:4] != 'http':
            url = f'http://{url}'

        # Создание уникального индекса для ссылки
        if len(list(temp_database.keys())) == 0:
            new_index = 1
        else:
            new_index = int(list(temp_database.keys())[-1]) + 1

        # Добавление ссылки во временную бд
        temp_database[new_index] = url

        response_data = {
            'status': 'success',
            'data': new_index,
            'detail': 'Url was successfully created'
        }
        return JSONResponse(content=response_data, status_code=200)

    # Ошибка сервера
    except Exception as error:
        response_data = {
            'status': 'error',
            'data': str(error),
            'detail': 'Server error'
        }
        return JSONResponse(content=response_data, status_code=500)


@app.get('/redirect={index}', response_class=RedirectResponse)
async def redirect(index):
    try:
        # Получение ссылки по уникальному индексу
        url = temp_database.get(int(index))

        # Проверка на наличие ссылки
        if url is None:
            raise HTTPException(status_code=404, detail='Url not found')

        return url

    # Обработчик прочих ошибок
    except HTTPException as error:
        response_data = {
            'status': 'error',
            'data': None,
            'detail': error.detail
        }
        return JSONResponse(content=response_data, status_code=error.status_code)

    # Ошибка сервера
    except Exception as error:
        response_data = {
            'status': 'error',
            'data': str(error),
            'detail': 'Server error'
        }
        return JSONResponse(content=response_data, status_code=500)