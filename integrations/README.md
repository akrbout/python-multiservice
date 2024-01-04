# Инфраструктура для локальной разработки

## Как развернуть?
* Устанавливаем Docker/docker-compose;
* В данном каталоге выполняем в терминале:
```shell
docker-compose up -d
```
* Ждем, пока загрузятся и запустятся образы;
* Готово! 

По порту `8080` на `localhost` можно зайти в Adminer и просмотреть таблицы базы данных.

Если нужно проверить работу контейнеров, то прописываем в терминале:
```shell
docker ps
```
При правильном запуске образов должны увидеть следующее:
```
CONTAINER ID    IMAGE       COMMAND                 CREATED     STATUS      PORTS                    NAMES
c7fde71f1403    postgres    "docker-entrypoint.s…"  8 days ago  Up 8 days   0.0.0.0:5432->5432/tcp   integrations-db-1
fe06f52571ed    adminer     "entrypoint.sh php -…"  8 days ago  Up 8 days   0.0.0.0:8080->8080/tcp   integrations-adminer-1
```

В случае необходимости (если порт `8080` занят и используется другим сервисом), то его можно поменять в файле
`docker-compose.yml`.