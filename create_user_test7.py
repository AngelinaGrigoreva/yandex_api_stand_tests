import sender_stand_request
import data
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body
# Функция для негативной проверки
def negative_assert_symbol(first_name):
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body(first_name)
    # В переменную response сохраняется результат запроса
    response = sender_stand_request.post_new_user(user_body)
    # Проверка, что код ответа равен 400
    assert response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "длина должна быть не менее 2 и не более 15 символов"
# Тест 7. Ошибка
# Параметр fisrtName состоит из слов с пробелами
def test_create_user_has_space_in_first_name_get_error_response():
        negative_assert_symbol("Человек и КО")