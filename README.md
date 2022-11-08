### Описание

У нас есть программируемые датчики, измеряющие температуру. Раз в некоторый интервал времени датчики делают запрос по API и записывают свои показания. В показания датчики передают свой ID и текущую температуру в градусах Цельсия.

Необходимо реализовать REST API для добавления/изменения датчиков, их просмотра и добавления новых измерений температуры.

Требуется задать 2 модели (они уже описаны в models.py):

- датчик:

  - название
  - описание (необязательное, например, "спальня" или "корридор на 2 этаже")

- измерение температуры:

  - ID датчика
  - температура при измерении
  - дата измерения

Для сериализаторов используйте `ModelSerializer`.

---

Запросы, которые должны быть реализованы в системе:

1. Создать датчик. Указываются название и описание датчика.
2. Изменить датчик. Указываются название и/или описание.
3. Добавить измерение. Указываются ID датчика и температура.
4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.

```json
[
  {
    "id": 2,
    "name": "ESP32",
    "description": "Датчик на кухне за холодильником"
  },
  {
    "id": 1,
    "name": "ESP32",
    "description": "Перенес датчик на балкон"
  }
]
```

5. Получить информацию по конкретному датчику. Выдается полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.

```json
{
  "id": 1,
  "name": "ESP32",
  "description": "Перенес датчик на балкон",
  "measurements": [
    {
      "temperature": 22.3,
      "created_at": "2021-10-23T16:44:51.432328Z"
    },
    {
      "temperature": 22.5,
      "created_at": "2021-10-23T16:45:51.091212Z"
    }
  ]
}
```

Примеры запросов можно посмотреть в файле [requests.http](./requests.http)

Установить зависимости:

```bash
pip install -r requirements.txt
```

Вам необходимо будет создать базу в postgres и прогнать миграции:

```base
python manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```
