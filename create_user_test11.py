import sender_stand_request
import data
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body
# Функция для негативной проверки
# В ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_no_firstname(user_body):
        # В переменную response сохрани результат вызова функции
        response = sender_stand_request.post_new_user(user_body)
        # Проверь, что код ответа — 400
        assert response.status_code == 400
        # Проверь, что в теле ответа атрибут "code" — 400
        assert response.json()["code"] == 400
        # Проверь текст в теле ответа в атрибуте "message"
        assert response.json()["message"] == "Не все необходимые параметры были переданы"
# Тест 11. Ошибка
# Параметр fisrtName состоит из пустой строки
def test_create_user_empty_first_name_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body("")
    # Проверка полученного ответа
    negative_assert_no_firstname(user_body)