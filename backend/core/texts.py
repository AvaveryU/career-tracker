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

# Уровень образования
EDUCATION_LEVELS = [
    ("school", "Среднее образование"),
    ("college", "Средне-специальное образование"),
    ("university", "Высшее образование"),
    ("postgrad", "Ученая степень"),
]

#
POSITION_LIST = [
    ("frontend_dev", "Фронтенд-разработчик"),
    ("fullstack_dev", "Фулстек-разработчик"),
    ("python_dev", "Python-разработчик"),
    ("qa_engineer", "Инженер по тестированию"),
    ("java_dev", "Java-разработчик"),
    ("data_scientist", "Специалист по data-science"),
]
