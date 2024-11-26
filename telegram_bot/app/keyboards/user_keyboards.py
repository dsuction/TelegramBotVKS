from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram_bot.app.utils.parser_data import find_data_materials


def profile_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Редактировать профиль', callback_data="edit_profile")],
        [InlineKeyboardButton(text='Доступные функции', callback_data="menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def help_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='🗨️ Поддержка', callback_data='open_support')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def main_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='👤 Профиль', callback_data="open_profile")],
        [InlineKeyboardButton(text='📅 События', callback_data="open_events")],
        [InlineKeyboardButton(text='➕ Создать новую ВКС', callback_data="create_new_VKS")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Работа с BKC', callback_data="open_working_with_VKS")],
        [InlineKeyboardButton(text='Работа с организациями', callback_data="open_working_with_org")],
        [InlineKeyboardButton(text='Подключение к сторонним сервисам', callback_data="connecting_third-partyservices")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
