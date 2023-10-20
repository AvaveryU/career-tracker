# Выборы для учебного статуса студентов
ACADEMIC_STATUS_CHOICES = [
    ("passing", "Проходит обучение"),
    ("academic_leave", "Академический отпуск"),
    ("graduate", "Выпускник"),
    ("expelled", "Отчислен"),
]

# Выборы для статуса трудоустройства студентов
EMPLOYMENT_STATUS_CHOICES = [
    ("job_search", "Ищу работу"),
    ("employed", "Трудоустроен"),
    ("internship_search", "В поиске стажировки"),
    ("other", "Другое"),
]

# Статусы для откликов
APPLICATION_STATUS_CHOICES = [
    ("pending", "В ожидании"),
    ("approved", "Одобрено"),
    ("rejected", "Отклонено"),
]

# Статусы для вакансий
VACANCY_STATUS_CHOICES = [
    ("open", "Открыта"),
    ("closed", "Закрыта"),
]

# Выбор грейда
GRADE_CHOICES = [
    ("junior", "Junior"),
    ("middle", "Middle"),
]
