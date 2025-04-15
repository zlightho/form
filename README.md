# Flask Backend for Form Submission

## Описание
Этот проект позволяет сохранять данные, отправленные из HTML-формы, в CSV-файл (`submissions.csv`).

## Быстрый старт

1. **Установите зависимости**:
   ```
   pip install -r requirements.txt
   ```
2. **Запустите сервер**:
   ```
   python backend.py
   ```
3. **Настройте отправку формы в вашем HTML** (см. пример ниже).

## Пример JavaScript для отправки формы

```html
<script>
document.getElementById('your-form-id').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => { data[key] = value; });

    fetch('/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.status === "success") {
            alert("Форма успешно отправлена!");
        } else {
            alert("Ошибка отправки формы.");
        }
    })
    .catch(() => alert("Ошибка соединения с сервером."));
});
</script>
```

Замените `your-form-id` на реальный id вашей формы.

---

## Как это работает
- Backend принимает POST-запросы на `/submit`.
- Все поля формы автоматически сохраняются в `submissions.csv`.

---

**Если нужна помощь с интеграцией или примером формы — дайте знать!**
