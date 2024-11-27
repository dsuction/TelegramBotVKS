from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def profile_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Редактировать профиль', callback_data="edit_profile")],
        [InlineKeyboardButton(text='Доступные функции', callback_data="menu")],
        [InlineKeyboardButton(text='Выйти из профиля', callback_data="exit_profile")]
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


def registration_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Регистрация', callback_data='start_registration')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def log_out_profile_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Авторизация', callback_data='open_profile')],
        [InlineKeyboardButton(text='Регистрация', callback_data='start_registration')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def save_changes_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='✅ Подтвердить', callback_data=f'ok_registration')],
        [InlineKeyboardButton(text='❌ Отмена', callback_data='no_registration')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Работа с BKC', callback_data="open_working_with_VKS")],
        [InlineKeyboardButton(text='Работа с организациями', callback_data="open_working_with_org")],
        [InlineKeyboardButton(text='Подключение к сторонним сервисам', callback_data="connecting_third-partyservices")],
        [InlineKeyboardButton(text='🔙 Вернуться назад', callback_data="open_profile")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def vks_table() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Доступные ВКС", callback_data='open_available_VKS')],
        [InlineKeyboardButton(text="Посмотреть мои ВКС", callback_data='view_my_VKS')],
        [InlineKeyboardButton(text="Создать новую ВКС", callback_data='create_vks')],
        [InlineKeyboardButton(text='🔙 Вернуться назад', callback_data="menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def setting_vks() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Состояние")]
    ]
