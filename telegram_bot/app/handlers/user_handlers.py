from aiogram import types, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.user_keyboards import *
from utils.text import text_data

router = Router()


@router.message(Command('start'))
async def command_start(message: types.Message) -> None:
    await message.answer(text_data['start'], reply_markup=main_keyboards())


@router.message(Command('catalog'))
async def commands_handler(message: types.Message) -> None:
    await message.answer(text_data['catalog'], reply_markup=selection_subjects_keyboard())


@router.callback_query(F.data.startswith("choosing_class_"))
async def main_callback_handler(callback: types.CallbackQuery) -> None:
    subject = callback.data.split('_')[2]
    await callback.message.edit_text(text_data['choosing_class'],
                                     reply_markup=training_class_keyboard(subject))


@router.callback_query(F.data.startswith("training_class_"))
async def training_class_callback_handler(callback: types.CallbackQuery) -> None:
    elements = callback.data.split('_')
    training_class, part, subject = elements[2], elements[3], elements[4]
    await callback.message.edit_text(text_data['output_elements'],
                                     reply_markup=make_keyboard_topic(training_class, part, subject))


@router.callback_query(F.data.startswith("back_"))
async def back_callback_handler(callback: types.CallbackQuery) -> None:
    callback_data = [i for i in callback.data.split('_')]
    reverse = '_'.join(callback_data[1:-1])
    subject = callback_data[-1]

    if reverse == 'choosing_class':
        await callback.message.edit_text(text_data['catalog'], reply_markup=selection_subjects_keyboard())
    elif reverse == 'training_class':
        await callback.message.edit_text(text_data['choosing_class'],
                                         reply_markup=training_class_keyboard(subject))


@router.callback_query(F.data.startswith("send_data_"))
async def send_data_handler(callback: types.CallbackQuery) -> None:
    elements = callback.data.split('_')
    training_class, part, subject = elements[2], elements[3], elements[4]
    data_answer = find_data_materials(training_class, subject)
    text = data_answer[int(elements[5])][0]
    if '—' in text:
        text = text.split('—')[1]
    elif 'до ' in text:
        text = text[13:]
    await callback.message.answer(f'{text}\n'
                                  f'{data_answer[int(elements[5])][1]}')


@router.message(F.text)
async def click_for_more(message: Message) -> None:
    if message.text.lower() == 'информация':
        await message.answer(text_data['information'])


def register_user_handlers(dp: Dispatcher) -> None:
    dp.include_router(router)
