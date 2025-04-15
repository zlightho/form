# Backend для Render.com

- Залейте содержимое этой папки (`backend.py`, `requirements.txt`) в отдельный репозиторий на GitHub.
- При деплое на Render используйте команду запуска:
  gunicorn backend:app
- Backend будет доступен по HTTPS, например:
  https://your-backend.onrender.com/submit
- Не забудьте добавить flask-cors в requirements.txt и подключить CORS в backend.py.
- submissions.csv будет сохраняться в корне сервиса Render (будьте внимательны: файл не сохраняется между перезапусками на бесплатном тарифе).
