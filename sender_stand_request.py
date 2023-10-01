import configuration
import data
import requests


# Создание заказа
def post_new_order(create_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                    json = create_order,
                    headers = data.headers)
response = post_new_order(data.create_order)

# Сохранение номера трека заказа
order_track = response.json()["track"]


# Получение заказа по треку заказа
def get_order_by_track(order_track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                        params={"t": order_track})