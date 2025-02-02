from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Обчислює кількість днів між сьогоднішньою датою та датою, зазначеною у рядку.

    :param date: Рядок з датою у форматі 'YYYY-MM-DD'
    :return: Кількість днів (ціле число). Якщо дата у майбутньому, повертає від'ємне число.
             У випадку неправильного формату повертає повідомлення про помилку.
    """
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'YYYY-MM-DD'."
    
    today_date = datetime.today().date()
    delta = (today_date - given_date).days
    return delta

# Приклад використання:
# Якщо сьогодні 2 лютого 2025 року, то get_days_from_today("2024-08-29") поверне 157
print(get_days_from_today('2024-08-29'))
