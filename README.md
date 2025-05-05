# Структура проекту
<pre lang="text"><code> ``` 
library_project/
│
├── adapters/                 # Зовнішні адаптери (views, forms)
│   └── django_app/
│       ├── templates/
│       │   └── ...          # HTML шаблони
│       ├── views.py         # Контролери
│       ├── forms.py         # Django-форми
│       └── urls.py          # Маршрути
│
├── domain/                  # Домена логіка
│   ├── models.py            # Клас користувача, книги, замовлення
│   └── services.py          # Логіка замовлення книги
│
├── infrastructure/          # Робота з БД
│   └── repositories.py      # Адаптери для збереження/отримання даних
│
├── library_project/         # Конфігурація Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── db.sqlite3
 ``` </code></pre>
