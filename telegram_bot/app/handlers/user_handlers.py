from aiogram import types, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from telegram_bot.app.keyboards.user_keyboards import *
from telegram_bot.app.utils.text import text_data
from api_communication import auth_login

router = Router()

login = 'not'
password = 'not'


def profile(login: str, password: str):
    data_profile = auth_login(login, password)
    result = f"""
🌇 Добрый вечер, {data_profile['user']['lastName']} {data_profile['user']['firstName']}!

<b>👤 Ваш профиль:</b>
<b>id:</b> {data_profile['user']['id']}
<b>Логин:</b> {data_profile['user']['login']}
<b>Почта:</b> {data_profile['user']['email']}
<b>Номер телефона</b> {data_profile['user']['phone']}
<b>Дата рождения</b> {data_profile['user']['birthday']}

✏️ Если хотите изменить профиль, нажмите на кнопку под этим сообщением.
"""
    return result


@router.message(Command('start'))
async def command_start(message: types.Message) -> None:
    await message.answer(text_data['start'], reply_markup=main_keyboard())


@router.message(Command('help'))
async def command_start(message: types.Message) -> None:
    await message.answer(text_data['help'], reply_markup=help_keyboard())


@router.message(Command('menu'))
async def open_menu(message: types.Message) -> None:
    await message.answer(text_data['menu'], reply_markup=menu_keyboard())


@router.callback_query(F.data == 'menu')
async def open_menu(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_data['menu'], reply_markup=menu_keyboard())


@router.message(Command('profile'))
async def send_profile_command(message: types.Message) -> None:
    global login, password
    if login == 'not' or password == 'not':
        await message.answer(text_data['authorization'])
    else:
        await message.answer(profile(login, password), reply_markup=profile_keyboard())


@router.callback_query(F.data == 'open_profile')
async def send_profile_callback(callback: types.CallbackQuery) -> None:
    global login, password
    if login == 'not' or password == 'not':
        await callback.message.edit_text(text_data['authorization'])
    else:
        await callback.message.edit_text(profile(login, password), reply_markup=profile_keyboard())


@router.callback_query(F.data == 'edit_profile')
async def edit_profile(callback: types.CallbackQuery) -> None:
    ...


@router.callback_query(F.data == 'open_available_VKS')
async def send_available_VKS(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('pass')


@router.callback_query(F.data == 'open_support')
async def send_support_information(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_data['information'])


@router.message(F.text)
async def click_for_more(message: Message) -> None:
    global login, password

    if message.text.lower() == 'информация':
        await message.answer(text_data['information'])
    else:
        try:
            login, password = message.text.split()
            await send_profile_command(message)
        except:
            login, password = 'not', 'not'
        if login != 'hantaton09' or password != 'JK1zRww2N^3TWV2I':
            await message.answer("Я не понимаю вас :(\nОбратитесь за помощью используя /help")


def register_user_handlers(dp: Dispatcher) -> None:
    dp.include_router(router)
