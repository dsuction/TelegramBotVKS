from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from app.utils.parser_data import find_data_materials


# click for more


def main_keyboards() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='/catalog')
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def selection_subjects_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='Алгебра', callback_data='choosing_class_алгебра')],
        [InlineKeyboardButton(text='Геометрия', callback_data='choosing_class_геометрия')],
        [InlineKeyboardButton(text='Теория вероятности и статистики', callback_data='choosing_class_твист')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def training_class_keyboard(subject) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text='10 класс 1 часть', callback_data=f'training_class_10_1_{subject}'),
            InlineKeyboardButton(text='10 класс 2 часть', callback_data=f'training_class_10_2_{subject}')
        ]
    ]

    if subject != 'твист':
        keyboard.append([
            InlineKeyboardButton(text='11 класс 1 часть', callback_data=f'training_class_11_1_{subject}'),
            InlineKeyboardButton(text='11 класс 2 часть', callback_data=f'training_class_11_2_{subject}')
        ])
    keyboard.append([InlineKeyboardButton(text='Назад', callback_data=f'back_choosing_class_{subject}')])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def make_keyboard_topic(training_class, part, subject) -> InlineKeyboardMarkup:
    keyboard = []
    if subject == 'твист':
        subject = 'Теория вероятности и статистика'
    data = find_data_materials(training_class, subject)
    start = 0 if part == '2' else len(data) // 2
    finish = len(data) // 2 + 1 if part == '2' else len(data)

    for i in range(start, finish):
        text = data[i][0]
        if '—' in text:
            text = text.split('—')[1]
        elif 'до ' in text:
            text = text[13:]

        if text != ' ':
            keyboard.append(
                [InlineKeyboardButton(text=text, callback_data=f'send_data_{training_class}_{part}_{subject}_{i}')])

    keyboard.append([InlineKeyboardButton(text='Назад', callback_data=f'back_training_class_{subject}')])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

