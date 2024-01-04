# reimport-ecom-backend
Бэкенд учебного проекта reimport-ecom

## ALARM!!!
Перед запуском сервиса необходимо развернуть инфраструктуру
из папки integrations в корне монорепозитория.

## Необходимые ENV для запуска локально
```shell
export DATABASE_ENGINE=postgresql
export DATABASE_USER=postgres
export DATABASE_PASSWORD=testpostgres
export DATABASE_HOST=localhost
export DATABASE_PORT=5432
export DATABASE_NAME=db
export AUTH_SECRET=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
export AUTH_ALGORITHM=HS256
export AUTH_RESET_SECRET=testtest
export AUTH_VERIFICATION_SECRET=testtest
export AVATAR_SERVICE_HOST=localhost
export AVATAR_SERVICE_PORT=3552
export AVATAR_SERVICE_IMAGE_SIZE=500
```
