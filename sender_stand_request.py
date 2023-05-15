import configuration
import requests
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

#здесь передается url и json для создания заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,\
                         json=body, headers=data.headers)
#здесь передается url и ручка на поиск заказа
def get_order_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + data.track)

