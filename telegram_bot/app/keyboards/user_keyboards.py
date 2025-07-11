from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def profile_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Редактировать профиль', callback_data="edit_profile")],
        [InlineKeyboardButton(text='Доступные функции', callback_data="menu")],
        [InlineKeyboardButton(text='Выйти из профиля', callback_data="exit_profile")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def is_edit_profile() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='✅ Сохранить изменение', callback_data='yes_edit_profile')],
        [InlineKeyboardButton(text='❌ Отменить изменение', callback_data='no_edit_profile')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def is_revers_edit_profile() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Да', callback_data='edit_profile')],
        [InlineKeyboardButton(text='Нет', callback_data='open_profile')]
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
        [InlineKeyboardButton(text='📅 Ближайшие события', callback_data="upcoming_events")],
        [InlineKeyboardButton(text='➕ Создать новую ВКС', callback_data="create_vks")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def registration_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='🔐 Регистрация', callback_data='start_registration')]
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
        [InlineKeyboardButton(text='Ближайшие события', callback_data='upcoming_events_1'),
         InlineKeyboardButton(text="Доступные ВКС", callback_data='open_available_VKS_1')],
        [InlineKeyboardButton(text="Посмотреть мои ВКС", callback_data='view_my_VKS_1')],
        [InlineKeyboardButton(text="Создать новую ВКС", callback_data='create_VKS')],
        [InlineKeyboardButton(text='🔙 Вернуться назад', callback_data="menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def setting_vks() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Состояние")]
    ]


def start_switching_panel_VKS(current_page: int) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Выбрать событие', callback_data=f'select_event-{current_page}'),
         InlineKeyboardButton(text='➡️', callback_data=f'switching_panel_VKS_right-{current_page}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def switching_panel_VKS(current_page: int) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='⬅️', callback_data=f'switching_panel_VKS_left-{current_page}'),
         InlineKeyboardButton(text='Выбрать событие', callback_data=f'select_event-{current_page}'),
         InlineKeyboardButton(text='➡️', callback_data=f'switching_panel_VKS_right-{current_page}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def end_switching_panel_VKS(current_page: int) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='⬅️', callback_data=f'switching_panel_VKS_left-{current_page}'),
         InlineKeyboardButton(text='Выбрать событие', callback_data=f'select_event-{current_page}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def confirm_date_selection_VKS() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Подтвердить', callback_data='ok_date_selection')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def filter_VKS_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Забронированные', callback_data='filter_VKS-1'),
         InlineKeyboardButton(text='Начатые', callback_data='filter_VKS-2'),
         InlineKeyboardButton(text='Законченные', callback_data='filter_VKS-3'),
         InlineKeyboardButton(text='Отмененные', callback_data='filter_VKS-4')],
        [InlineKeyboardButton(text='Наименование', callback_data='filter_VKS-5')],
        [InlineKeyboardButton(text='Приоритет', callback_data='filter_VKS-6')],
        [InlineKeyboardButton(text='Департамент', callback_data='filter_VKS-7')],
        [InlineKeyboardButton(text='Организатор', callback_data='filter_VKS-8')],
        [InlineKeyboardButton(text='✅ Применить', callback_data='ok_filter_VKS'),
         InlineKeyboardButton(text='Показать без фильтров', callback_data='no_filter_VKS')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
