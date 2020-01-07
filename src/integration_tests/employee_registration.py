import pytest
import datetime


class TestEmployeeRegistration:
    # Тест проверяет регистрацию нового пользователя, когда пользователь с таким логином и паролем уже есть
    def test_reregistration(self):
        users = [{'login': 'sysadmin', 'password': 'sysadmin', 'post': 'sysadmin'},
                 {'login': 'libadmin', 'password': 'libadmin', 'post': 'libadmin'},
                 {'login': 'libworker', 'password': 'libworker', 'post': 'libworker'}]
        new_user = {'login': 'sysadmin', 'password': 'sysadmin', 'post': 'sysadmin'}

        for i in users:
            if new_user['login'] == i['login'] and new_user['password'] == i['password']:
                print(
                    'Такой пользователь уже зарегистрирован. Введите новые данные, если хотите изменить уже существующие')
                new_data = {'login': 'sysadmin2', 'password': 'sysadmin2', 'post': 'sysadmin'}
                if new_data['login'] != i['login']:
                    i.update({'login': new_data['login'], 'password': new_data['password'], 'post': new_data['post']})
                    print(f"Данные успешно обновлены {i}")
                    assert True
                else:
                    print("Такой логин уже занят, пожалуйста, выберете другой")
                    assert False


    def test_registration_new_employee(self):
        # Тест проверяет регистрацию нового пользователя
        users = [{'login': 'sysadmin', 'password': 'sysadmin', 'post': 'sysadmin'},
                {'login': 'libadmin', 'password': 'libadmin', 'post': 'libadmin'},
                {'login': 'libworker', 'password': 'libworker', 'post': 'libworker'}]
        new_user = {'login': 'awdawd', 'password': 'sysadmawdawdin', 'post': 'sysadmin'}
        user_exist = False
        for i in users:
            if i == new_user:
                user_not_exist = True
        if not user_exist:
            users.append(new_user)
        assert len(users) == 4