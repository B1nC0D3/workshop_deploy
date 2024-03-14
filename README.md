# Чеклист и сводка команд для деплоя
 
Чеклист для деплоя собственной апи/чего угодно

## Деплой
0. Подключиться к удаленному серверу
   (Можно посмотреть на платформе)
0. Апдейт удаленной машины
   `sudo apt update && sudo apt upgrade`
1. Склонить проект с гитхаба
   `git clone link_to_git`
2. Установка венва
   `sudo python3 -m venv venv`
3. Активация венва
   `source venv/bin/activate`
4. Установка зависимостей
   `pip install -r requirements.txt`
5. Переместить сервисный файлик в папку с сервисными файликами
   `sudo cp infra/api.service /etc/systemd/system/`
6. Активировать сервисный файлик
   `sudo systemctl daemon-reload`
   `sudo systemctl enable api.service`
7. Запустить сервисный файлик
   `sudo systemctl start api.service`
8. Установить nginx
   `sudo apt install nginx`
9. Проверить что установился
   `systemctl status nginx`
10. Переместить nginx-конфиг в папку с конфигами
    `sudo cp infra/nginx.conf /etc/nginx/sites-enabled`
11. Перезапустить nginx
    `sudo systemctl reload nginx`
12. Радоваться тому, что ничего не сломалось

## Короткая сводка команд

### systemctl
Старт/рестарт/статус конкретного сервиса
```shell
sudo systemctl start name.service
sudo systemctl restart name.service
sudo systemctl status name.service
```

### journalctl
Для просмотра логов конкретного сервиса, начиная с сегодняшнего дня
```shell
sudo journalctl -u name.service --since today
```

### Апдейт проекта
1. Пушим изменения
    Далее все на удаленной машине
2. `git pull`
3. `sudo systemctl restart name.service`
