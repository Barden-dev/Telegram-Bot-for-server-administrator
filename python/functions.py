from datetime import datetime, timedelta
import psutil
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from contextlib import suppress

import config

from collections import deque


days_translation = {
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница",
    "Saturday": "Суббота",
    "Sunday": "Воскресенье"
}

def get_current_date(days_to_add=0, weeks_to_add=0):
    total_days_to_add = days_to_add + weeks_to_add * 7
    target_date = datetime.now() + timedelta(days=total_days_to_add)
    current_date = target_date.date()
    weekday_name = days_translation.get(target_date.strftime("%A"), target_date.strftime("%A"))
    formatted_date = {weekday_name : current_date.strftime('%d.%m.%Y')}
    return formatted_date


def get_server_stats():
    # Загруженность CPU в процентах
    cpu_load = psutil.cpu_percent(interval=1)

    # ОЗУ
    memory = psutil.virtual_memory()
    ram_total = memory.total / (1024 * 1024)  # Всего ОЗУ в МБ
    ram_used = memory.used / (1024 * 1024)    # Занято ОЗУ в МБ
    ram_free = memory.available / (1024 * 1024)  # Свободно ОЗУ в МБ

    # Температура процессора (работает на большинстве Linux-систем)
    try:
        temp = psutil.sensors_temperatures()['coretemp'][0].current
    except:
        temp = "Недоступно (установите lm-sensors и проверьте доступ)"

    # Дисковое пространство
    disk = psutil.disk_usage('/')
    disk_free = disk.free / (1024 * 1024 * 1024)  # Свободно в ГБ

    # Формируем сообщение
    stats = (
        f"📊 Состояние сервера:\n"
        f"CPU: {cpu_load}%\n"
        f"ОЗУ занято: {ram_used:.2f} МБ\n"
        f"ОЗУ свободно: {ram_free:.2f} МБ\n"
        f"Температура CPU: {temp}°C\n"
        f"Свободно на диске: {disk_free:.2f} ГБ"
    )
    return stats