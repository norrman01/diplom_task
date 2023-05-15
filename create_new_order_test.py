import sender_stand_request
import data

#здесь будет выполняться запрос на создание заказа, а также
#перевод track из int  в string, и запись в дата
def get_new_user_token():
    user_track = sender_stand_request.post_new_order(data.new_orders).json()["track"]
    data.track = str(user_track)
    print(data.track)

#здесь будет выполняться запрос на получение заказа по треку
def get_order():
    user_order = sender_stand_request.get_order_track().json()
    data.order = user_order
    print(data.order)

#здесь тест дергает первый метод
def test_get_new_token():
    get_new_user_token()

#здесь тест дергает второй метод
def test_get_order():
    get_order()

#здесь идет проверка на код 200
def test_200():
    response = sender_stand_request.get_order_track()
    assert response.status_code == 200





