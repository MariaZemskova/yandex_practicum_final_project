import data
import sender_stand_request

# Функция получения номера заказа
def positive_assert(order_track):
    order_response = sender_stand_request.get_order_by_track(order_track)
# Выведем номер заказа
    print(order_track)
# Проверить, что код ответа равен 200
    assert order_response.status_code == 200


# Тест 1.
def test_get_order_by_track():
    positive_assert(sender_stand_request.order_track)