from aiogram import types

from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Полные сведения о сервере", callback_data="server_status"))
    builder.add(types.InlineKeyboardButton(text="Перезагрузка сервера", callback_data="server_reboot"))
    builder.add(types.InlineKeyboardButton(text="Выключить сервер", callback_data="server_poweroff"))
    builder.add(types.InlineKeyboardButton(text="Перезапустить бота", callback_data="bot_restart"))
    builder.add(types.InlineKeyboardButton(text="Локальный айпи", callback_data="server_local_ip"))
    builder.add(types.InlineKeyboardButton(text="Глобальный айпи", callback_data="server_global_ip"))
    builder.add(types.InlineKeyboardButton(text="Ссылка на сайт", callback_data="get_site"))
    builder.add(types.InlineKeyboardButton(text="Перезапустить/Запустить сайт", callback_data="site_restart"))
    builder.add(types.InlineKeyboardButton(text="WakeOnLan", callback_data="wakeup_device"))
    builder.add(types.InlineKeyboardButton(text="Настройки", callback_data="settings"))
    builder.adjust(1)
    return builder.as_markup()