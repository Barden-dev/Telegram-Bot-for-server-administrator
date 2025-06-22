import subprocess

import config
import kb
import functions
import time
import utils



from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from functools import wraps
from aiogram.enums import ParseMode

router = Router()

last_call = {}

def admin_required(handler):
    @wraps(handler)
    async def wrapper(*args, **kwargs):
        # Получаем сообщение или callback-запрос из аргументов
        for arg in args:
            if isinstance(arg, types.Message):
                user_id = arg.from_user.id
                message = arg
            elif isinstance(arg, types.CallbackQuery):
                user_id = arg.from_user.id
                message = arg.message
        
        # Проверяем, есть ли пользователь в списке админов
        if user_id not in config.ADMINS:
            return  # Прерываем выполнение, если не админ
        
        # Если админ, продолжаем выполнение хэндлера
        return await handler(*args, **kwargs)
    return wrapper

# МЕНЮ СТАРТ
@router.message(Command("start"))
@admin_required
async def cmd_start(message: types.Message, state: FSMContext):
    message_text = functions.get_server_stats()
    await message.answer(f"Здарова!\n\n{message_text}", reply_markup=kb.get_main_keyboard())
# МЕНЮ СТАРТ

@router.callback_query(F.data == "server_reboot")
@admin_required
async def server_reboot_off(callback: types.CallbackQuery):
    await callback.message.answer("Перезагружаю...")
    utils.reboot_server()

@router.callback_query(F.data == "server_poweroff")
@admin_required
async def server_power_off(callback: types.CallbackQuery):
    await callback.message.answer("Звершение работы...")
    utils.shutdown_server()

@router.callback_query(F.data == "server_local_ip")
@admin_required
async def local_ip(callback: types.CallbackQuery):
    ip = utils.get_local_ip()
    await callback.message.answer(f"Локальный ip адрес: {ip}")
    await callback.answer()

@router.callback_query(F.data == "server_global_ip")
@admin_required
async def global_ip(callback: types.CallbackQuery):
    ip = utils.get_global_ip()
    await callback.message.answer(f"Глобальный ip адрес: {ip}")
    await callback.answer()

@router.callback_query(F.data == "server_status")
@admin_required
async def server_status(callback: types.CallbackQuery):
    message_text = functions.get_server_stats()
    await callback.message.edit_text(message_text, reply_markup=kb.get_main_keyboard())
    await callback.answer()

@router.callback_query(F.data == "bot_restart")
@admin_required
async def bot_restart(callback: types.CallbackQuery):
    await callback.answer("Бот перезапускается...")
    utils.restart_bot()

@router.callback_query(F.data == "get_site")
@admin_required
async def bot_restart(callback: types.CallbackQuery):
    link = utils.get_global_ip() + ":8080"
    await callback.message.answer(f"<a href='{link}'>Ссылка</a>", parse_mode=ParseMode.HTML)


@router.callback_query(F.data == "site_restart")
@admin_required
async def bot_restart(callback: types.CallbackQuery):
    await callback.answer("Запуск/Перезапуск сайта...")
    utils.restart_site()

@router.callback_query(F.data == "wakeup_device")
@admin_required
async def wakeonlan(callback: types.CallbackQuery):
    utils.wakeonlan()
    await callback.message.answer("Включаю...")
    




# УДАЛАИТЬ / ЗАКРЫТЬ МЕНЮ
@router.callback_query(F.data == "close_menu")
@admin_required
async def remove_reminder(callback: types.CallbackQuery):
    await callback.message.delete()
# УДАЛАИТЬ / ЗАКРЫТЬ МЕНЮ
