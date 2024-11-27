from datetime import datetime

from aiogram import types, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from api_communucation.auth import register, login
from api_communucation.meetings import get_meetings
from telegram_bot.app.keyboards.user_keyboards import *
from telegram_bot.app.state.register import RegisterState
from telegram_bot.app.utils.text import text_data

router = Router()

login_L = 'not'
password = 'not'
data_registr = []


def profile(login_L: str, password: str):
    data_profile = login(login_L, password)
    result = f"""
🌇 Добрый вечер, {data_profile[0]['user']['lastName']} {data_profile[0]['user']['firstName']}!

<b>👤 Ваш профиль:</b>
<b>id:</b> {data_profile[0]['user']['id']}
<b>Логин:</b> {data_profile[0]['user']['login']}
<b>Почта:</b> {data_profile[0]['user']['email']}
<b>Номер телефона</b> {data_profile[0]['user']['phone']}
<b>Дата рождения</b> {data_profile[0]['user']['birthday']}

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
    global login_L, password
    if login_L == 'not' or password == 'not':
        await message.answer(text_data['authorization'], reply_markup=registration_keyboard())
    else:
        await message.answer(profile(login_L, password), reply_markup=profile_keyboard())


@router.callback_query(F.data == 'exit_profile')
async def exit_profile(callback: types.CallbackQuery) -> None:
    global login_L, password
    login_L, password = 'not', 'not'
    await callback.message.edit_text("Вы успешно вышли из своего профиля", reply_markup=log_out_profile_keyboard())


@router.callback_query(F.data == 'open_profile')
async def send_profile_callback(callback: types.CallbackQuery) -> None:
    global login_L, password
    if login_L == 'not' or password == 'not':
        await callback.message.edit_text(text_data['authorization'], reply_markup=registration_keyboard())
    else:
        await callback.message.edit_text(profile(login_L, password), reply_markup=profile_keyboard())


"""____________________________________________РЕГИСТРАЦИЯ В СИСТЕМЕ______________________________________________"""


@router.callback_query(F.data == 'start_registration')
async def start_registration(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text('<b>1️⃣ Как вас зовут?</b>\nВведите ваше имя и фамилию, чтобы другие участники вкс могли узнать вас')
    await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Привет {message.text}!\n'
                         f'<b>2️⃣ Отправьте ваш логин</b>\nЗапомните его, ведь он вам понадобиться еще при авторизации')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regLogin)


async def register_login(message: Message, state: FSMContext):
    await message.answer(f'Ваш логин: {message.text}\n'
                         f'<b>3️⃣ Отправьте ваш пароль</b>\nЗапомните его, ведь он вам понадобиться еще при авторизации')
    await state.update_data(reglogin=message.text)
    await state.set_state(RegisterState.regPassword)


async def register_password(message: Message, state: FSMContext):
    await message.answer(f'Ваш пароль: {message.text}\n'
                         f'<b>4️⃣ Отправьте вашу почту</b>\nНа нее будут приходить рассылки и напоминания о будущих вкс\nВ любой момент эту функцию можно отключить😉')
    await state.update_data(regpassword=message.text)
    await state.set_state(RegisterState.regEmail)


async def register_email(message: Message, state: FSMContext):
    await message.answer(f'Ваша почта: {message.text}\n'
                         f'<b>5️⃣ Отправьте ваш номер телефона</b>\nВы почти у цели!')
    await state.update_data(regemail=message.text)
    await state.set_state(RegisterState.regPhone)


async def register_phone(message: Message, state: FSMContext):
    global data_registr
    await state.update_data(regphone=message.text)
    msg = f'Ваш номер телефона: {message.text}'
    await message.answer(msg)

    reg_data = await state.get_data()
    reg_name = reg_data.get('regname')
    reg_surname = "Михайлов"
    reg_login = reg_data.get('reglogin')
    reg_password = reg_data.get('regpassword')
    reg_email = reg_data.get('regemail')
    reg_phone = reg_data.get('regphone')
    data_registr = [reg_name, reg_surname, reg_login, reg_password, reg_email, reg_phone]
    await state.clear()
    await message.answer(f"<b>✏️ Проверьте введенные вами данные:</b>\n\n"
                         f"<b>Имя:</b> {reg_name}\n"
                         f"<b>Фамилия:</b> {reg_surname}\n"
                         f"<b>Логин:</b> {reg_login}\n"
                         f"<b>Пароль:</b> <span class='tg-spoiler'>{reg_password}</span>\n"
                         f"<b>Почта:</b> {reg_email}\n"
                         f"<b>Номер телефона:</b> {reg_phone}\n\n"
                         f"Сохранить изменения?",
                         reply_markup=save_changes_keyboard())


@router.callback_query(F.data == 'ok_registration')
async def ok_registration(callback: types.CallbackQuery) -> None:
    reg_name = data_registr[0]
    reg_surname = data_registr[1]
    reg_login = data_registr[2]
    reg_password = data_registr[3]
    reg_email = data_registr[4]
    reg_phone = data_registr[5]

    try:
        result = register(first_name=reg_name, last_name=reg_surname, login=reg_login, password=reg_password,
                          email=reg_email, phone=reg_phone)
        print(result)
        await callback.message.answer("Вы успешно зарегистрировались! Теперь можете войти в свой аккаунт /profile")
    except:
        await callback.message.answer("Упс, произошла поломка😔\n"
                                      "Бригада хомячков уже занимается ее починкой, придется немного подождать")


"""__________________________________________________________________________________________________________________"""


@router.callback_query(F.data == 'no_registration')
async def no_registration(callback: types.CallbackQuery) -> None:
    await callback.message.answer("Регистрация успешно отменена")


@router.callback_query(F.data == 'edit_profile')
async def edit_profile(callback: types.CallbackQuery) -> None:
    ...


@router.callback_query(F.data == 'open_working_with_VKS')
async def open_working_with_VKS(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_data['open_working_with_VKS'], reply_markup=vks_table())


@router.callback_query(F.data == 'open_available_VKS')
async def send_available_VKS(callback: types.CallbackQuery) -> None:
    global login_L, password
    if login_L == 'not' or password == 'not':
        await callback.message.edit_text(text_data['authorization'], reply_markup=registration_keyboard())
    else:
        token = login(login_L, password)[0]['token']
        print(token)
        result = get_meetings(token, datetime(2024, 11, 26), datetime(2024, 11, 27))
        for i in result[0]['data']:
            result = f"""
<b>Ваша встреча id</b> {i['id']} - {i['name']}
<b>Начало:</b> {' '.join(i['startedAt'].split('T'))}
<b>Конец:</b> {' '.join(i['endedAt'].split('T'))}
<b>Продолжительность:</b> {i['duration']} мин.
            
🔗 {i['permalink']}
            """
            await callback.message.answer(result)


@router.callback_query(F.data == 'view_my_VKS')
async def view_my_VKS(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('pass2', reply_markup=setting_vks())


@router.callback_query(F.data == 'open_support')
async def send_support_information(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_data['information'])


@router.message(F.text)
async def click_for_more(message: Message) -> None:
    global login_L, password

    if message.text.lower() == 'информация':
        await message.answer(text_data['information'])
    else:
        try:
            login_L, password = message.text.split()
            await send_profile_command(message)
        except:
            login_L, password = 'not', 'not'
            await message.answer("Я не понимаю вас :(\nОбратитесь за помощью используя /help")


def register_user_handlers(dp: Dispatcher) -> None:
    dp.include_router(router)
