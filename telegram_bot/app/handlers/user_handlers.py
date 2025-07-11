import datetime

from aiogram import types, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from api_communucation.acount import update_user_info
from api_communucation.auth import register, login
from api_communucation.meetings import get_meetings, create_meetings
from telegram_bot.app.keyboards.user_keyboards import *
from telegram_bot.app.state.register import RegisterState
from telegram_bot.app.utils.text import text_data

router = Router()
flag_r = False
is_open_profile = False
flag_setting_calendar = False
flag_create_VKS = False
flag_filter = False
start_data = ''
end_data = ''
saved_login = 'not'
saved_password = 'not'
panel_VKS = []
new_id = ''
new_information = ''
data_profile_registration = []
state = []
filter_VKS = []
old_tab_panel_VKS = ''


def profile(user_login: str, user_password: str):
    data_profile = login(user_login, user_password)
    result = f"""
🌇 Добрый вечер, {data_profile[0]['user']['lastName']} {data_profile[0]['user']['firstName']}!

<b>👤 Ваш профиль:</b>
<b>id:</b> {data_profile[0]['user']['id']}
<b>Логин:</b> {data_profile[0]['user']['login']}
<b>Почта:</b> {data_profile[0]['user']['email']}
<b>Номер телефона</b> {data_profile[0]['user']['phone'] if data_profile[0]['user']['phone'] else 'Н/д'}
<b>Дата рождения</b> {data_profile[0]['user']['birthday'] if data_profile[0]['user']['birthday'] else 'Н/д'}

✏️ Если хотите изменить профиль, нажмите на кнопку под этим сообщением.
"""
    return result


"""___________________________________________________БАЗА___________________________________________________________"""


@router.message(Command('start'))
async def command_start(message: types.Message) -> None:
    await message.answer(text_data['start'], reply_markup=main_keyboard())


@router.message(Command('help'))
async def command_help(message: types.Message) -> None:
    await message.answer(text_data['help'], reply_markup=help_keyboard())


@router.message(Command('menu'))
async def open_menu_command(message: types.Message) -> None:
    await message.answer(text_data['menu'], reply_markup=menu_keyboard())


@router.callback_query(F.data == 'menu')
async def open_menu_callback(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_data['menu'], reply_markup=menu_keyboard())


@router.callback_query(F.data == 'open_support')
async def send_support_information(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text_data['information'])


@router.message(Command('profile'))
async def send_profile_command(message: types.Message) -> None:
    global is_open_profile
    try:
        is_open_profile = False
        if saved_login == 'not' or saved_password == 'not':
            is_open_profile = True
            await message.answer(text_data['authorization'], reply_markup=registration_keyboard())
        else:
            await message.answer(profile(saved_login, saved_password), reply_markup=profile_keyboard())
    except:
        await message.answer("Упс, произошла поломка в {command_profile} 😔\n"
                             "Бригада хомячков уже занимается ее починкой, придется немного подождать")


@router.callback_query(F.data == 'exit_profile')
async def exit_profile(callback: types.CallbackQuery) -> None:
    global saved_login, saved_password
    saved_login, saved_password = 'not', 'not'
    await callback.message.edit_text("Вы успешно вышли из своего профиля", reply_markup=log_out_profile_keyboard())


@router.callback_query(F.data == 'open_profile')
async def send_profile_callback(callback: types.CallbackQuery) -> None:
    """
    Открыть профиль аккаунта если его данные уже введены в бот ранее, иначе он запрашивает их у пользователя
    :param callback:
    :return: None
    """

    global is_open_profile
    try:
        is_open_profile = False
        if saved_login == 'not' or saved_password == 'not':
            is_open_profile = True
            await callback.message.edit_text(text_data['authorization'], reply_markup=registration_keyboard())
        else:
            await callback.message.edit_text(profile(saved_login, saved_password), reply_markup=profile_keyboard())
    except:
        await callback.message.answer("Упс, произошла поломка в {callback_open_profile} 😔\n"
                                      "Бригада хомячков уже занимается ее починкой, придется немного подождать")


"""____________________________________________РЕГИСТРАЦИЯ В СИСТЕМЕ______________________________________________"""


@router.callback_query(F.data == 'start_registration')
async def start_registration(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text(
        '<b>1️⃣ Как вас зовут?</b>\nВведите ваше имя и фамилию, чтобы другие участники вкс могли узнать вас')
    await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Привет {message.text}!\n'
                         '<b>2️⃣ Отправьте ваш логин</b>\nЗапомните его, ведь он вам понадобиться еще при авторизации')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regLogin)


async def register_login(message: Message, state: FSMContext):
    await message.answer(f'Ваш логин: {message.text}\n'
                         '<b>3️⃣ Отправьте ваш пароль</b>\nЗапомните его, ведь он вам понадобиться еще при авторизации')
    await state.update_data(reglogin=message.text)
    await state.set_state(RegisterState.regPassword)


async def register_password(message: Message, state: FSMContext):
    await message.answer(f'Ваш пароль: {message.text}\n'
                         '<b>4️⃣ Отправьте вашу почту</b>\nНа нее будут приходить рассылки и напоминания о ВКС\n'
                         'В любой момент эту функцию можно отключить😉')
    await state.update_data(regpassword=message.text)
    await state.set_state(RegisterState.regEmail)


async def register_email(message: Message, state: FSMContext):
    await message.answer(f'Ваша почта: {message.text}\n'
                         '<b>5️⃣ Отправьте ваш номер телефона</b>\nВы почти у цели!')
    await state.update_data(regemail=message.text)
    await state.set_state(RegisterState.regPhone)


async def register_phone(message: Message, state: FSMContext):
    global data_profile_registration

    await message.answer(f'Ваш номер телефона: {message.text}')
    await state.update_data(regphone=message.text)

    reg_data = await state.get_data()
    reg_name, reg_surname = reg_data.get('regname').split()
    reg_login = reg_data.get('reglogin')
    reg_password = reg_data.get('regpassword')
    reg_email = reg_data.get('regemail')
    reg_phone = reg_data.get('regphone')
    data_profile_registration = [reg_name, reg_surname, reg_login, reg_password, reg_email, reg_phone]
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
    """
    Регистрация пользователя в системе ВКС, используя введенные ранее данные
    :param callback:
    :return: None
    """

    reg_name = data_profile_registration[0]
    reg_surname = data_profile_registration[1]
    reg_login = data_profile_registration[2]
    reg_password = data_profile_registration[3]
    reg_email = data_profile_registration[4]
    reg_phone = data_profile_registration[5]

    try:
        result = register(first_name=reg_name, last_name=reg_surname, login=reg_login, password=reg_password,
                          email=reg_email, phone=reg_phone)
        await callback.message.answer("Вы успешно зарегистрировались! Теперь можете войти в свой аккаунт /profile")
    except:
        await callback.message.answer("Упс, произошла поломка в {callback_ok_registration} 😔\n"
                                      "Бригада хомячков уже занимается ее починкой, придется немного подождать")


@router.callback_query(F.data == 'no_registration')
async def no_registration(callback: types.CallbackQuery) -> None:
    await callback.message.answer("Регистрация успешно отменена")


"""_________________________________________ИЗМЕНЕНИЕ_ДАННЫХ_ПОЛЬЗОВАТЕЛЯ____________________________________________"""


@router.callback_query(F.data == 'edit_profile')
async def edit_profile(callback: types.CallbackQuery) -> None:
    global flag_r
    flag_r = True
    await callback.message.edit_text(f"""
Выберите пункт который хотите изменить:
1. Пароль 
2. Имя
3. Фамилия 
4. Отчество
5. Почта
6. Номер телефона
7. Дата рождения

Отправьте в формате [номер пункта]_[новые данные]
""")


"""__________________________________________________РАБОТА_С_ВКС____________________________________________________"""


@router.callback_query(F.data == 'open_working_with_VKS')
async def open_working_with_VKS(callback: types.CallbackQuery) -> None:
    """
    Открывает мень работы с ВКС
    :param callback:
    :return: None
    """
    await callback.message.edit_text(text_data['open_working_with_VKS'], reply_markup=vks_table())


@router.callback_query(F.data == 'upcoming_events_1')
async def upcoming_events_1(callback: types.CallbackQuery) -> None:
    global old_tab_panel_VKS
    old_tab_panel_VKS = callback.data
    await filter_view_my_VKS(callback)


@router.callback_query(F.data == 'upcoming_events')
async def upcoming_events(callback: types.CallbackQuery) -> None:
    """
    Отображает ближайшие события
    :param callback:
    :return:
    """
    global panel_VKS, is_open_profile, state

    is_open_profile = False
    if saved_login == 'not' or saved_password == 'not':
        is_open_profile = True
        await callback.message.answer(text_data['authorization'], reply_markup=registration_keyboard())

    else:
        print(saved_login, saved_password)

        name = None
        priority = None
        department = None
        organizer = None

        if len(state):
            state = ['booked', 'cancelled', 'started', 'ended']
        for i in filter_VKS:
            if i[0] == 'name':
                name = i[1]
            elif i[0] == 'priority':
                priority = int(i[1])
            elif i[0] == 'department':
                department = int(i[1])
            elif i[0] == 'organizer':
                organizer = i[1]

        result = get_meetings(saved_login, saved_password, datetime.datetime.now(),
                              datetime.datetime.now() + datetime.timedelta(days=3), state=state,
                              priority=priority, name=name, department_id=department)
        if result == 'error':
            await callback.message.answer('Попробуйте ввести еще раз')
        elif not result:
            await callback.message.answer('Нет ближайших событий')
        else:
            current_page = 0
            panel_VKS = result
            await displaying_panel_VKS(callback, current_page)


@router.callback_query(F.data == 'filter_VKS-1')
async def filter_VKS_1(callback: types.CallbackQuery) -> None:
    global data_profile_registration, state
    state.append('booked')


@router.callback_query(F.data == 'filter_VKS-2')
async def filter_VKS_2(callback: types.CallbackQuery) -> None:
    global data_profile_registration, state
    state.append('cancelled')


@router.callback_query(F.data == 'filter_VKS-3')
async def filter_VKS_3(callback: types.CallbackQuery) -> None:
    global data_profile_registration, state
    state.append('started')


@router.callback_query(F.data == 'filter_VKS-4')
async def filter_VKS_4(callback: types.CallbackQuery) -> None:
    global data_profile_registration, state
    state.append('ended')


@router.callback_query(F.data == 'filter_VKS-5')
async def filter_VKS_5(callback: types.CallbackQuery) -> None:
    global flag_filter, data_profile_registration
    flag_filter = True
    filter_VKS.append(['name'])
    await callback.message.answer('Введите название ВКС')


@router.callback_query(F.data == 'filter_VKS-6')
async def filter_VKS_6(callback: types.CallbackQuery) -> None:
    global flag_filter, data_profile_registration
    flag_filter = True
    filter_VKS.append(['priority'])
    await callback.message.answer('Введите приоритет')


@router.callback_query(F.data == 'filter_VKS-7')
async def filter_VKS_7(callback: types.CallbackQuery) -> None:
    global flag_filter, data_profile_registration
    flag_filter = True
    filter_VKS.append(['department'])
    await callback.message.answer('Введите id департамента')


@router.callback_query(F.data == 'filter_VKS-8')
async def filter_VKS_8(callback: types.CallbackQuery) -> None:
    global flag_filter, data_profile_registration
    flag_filter = True
    filter_VKS.append(['organizer'])
    await callback.message.answer('Введите организацию')


@router.callback_query(F.data == 'ok_filter_VKS')
async def ok_filter_VKS(callback: types.CallbackQuery):
    if old_tab_panel_VKS == 'upcoming_events_1':
        await upcoming_events(callback)
    elif old_tab_panel_VKS == 'view_my_VKS_1':
        await view_my_VKS(callback)
    elif old_tab_panel_VKS == 'open_available_VKS_1':
        await open_available_VKS(callback)


async def filter_view_my_VKS(callback: types.CallbackQuery) -> None:
    await callback.message.answer('Выберите фильтры для дальнейшего просмотра', reply_markup=filter_VKS_keyboard())


@router.callback_query(F.data == 'no_filter_VKS')
async def no_filter_VKS(callback: types.CallbackQuery) -> None:
    if old_tab_panel_VKS == 'upcoming_events_1':
        await upcoming_events(callback)
    elif old_tab_panel_VKS == 'view_my_VKS_1':
        await view_my_VKS(callback)
    elif old_tab_panel_VKS == 'open_available_VKS_1':
        await open_available_VKS(callback)


@router.callback_query(F.data == 'view_my_VKS_1')
async def view_my_VKS_1(callback: types.CallbackQuery) -> None:
    global old_tab_panel_VKS
    old_tab_panel_VKS = callback.data
    await filter_view_my_VKS(callback)


@router.callback_query(F.data == 'view_my_VKS')
async def view_my_VKS(callback: types.CallbackQuery) -> None:
    """
    Отображает все ВКС, в которых мы зарегистрированы
    :param callback:
    :return:
    """

    global panel_VKS, is_open_profile, state

    is_open_profile = False
    if saved_login == 'not' or saved_password == 'not':
        is_open_profile = True
        await callback.message.answer(text_data['authorization'], reply_markup=registration_keyboard())

    else:
        name = None
        priority = None
        department = None
        organizer = None
        if len(state):
            state = ['booked', 'cancelled', 'started', 'ended']
        print(filter_VKS)
        for i in filter_VKS:
            if i[0] == 'name':
                name = i[1]
            elif i[0] == 'priority':
                priority = int(i[1])
            elif i[0] == 'department':
                department = int(i[1])
            elif i[0] == 'organizer':
                organizer = i[1]

        result = get_meetings(saved_login, saved_password, datetime.datetime.now() - datetime.timedelta(days=14),
                              datetime.datetime.now() + datetime.timedelta(days=14), user_id=True, state=state,
                              priority=priority, name=name, department_id=department)

        if result == 'error':
            await callback.message.answer('Попробуйте ввести еще раз')
        elif not result:
            await callback.message.answer('Вы не зарегистрированы ни в одной ВКС')
        else:
            current_page = 0
            panel_VKS = result
            await displaying_panel_VKS(callback, current_page)


@router.callback_query(F.data == 'open_available_VKS_1')
async def open_available_VKS_1(callback: types.CallbackQuery) -> None:
    global old_tab_panel_VKS
    old_tab_panel_VKS = callback.data
    await filter_view_my_VKS(callback)

@router.callback_query(F.data == 'open_available_VKS')
async def open_available_VKS(callback: types.CallbackQuery) -> None:
    """
    Запрашивает начальную и конечную дату для просмотра всех доступных ВКС в системе
    :param callback:
    :return: None
    """
    global flag_setting_calendar, is_open_profile

    is_open_profile = False
    if saved_login == 'not' or saved_password == 'not':
        is_open_profile = True
        await callback.message.answer(text_data['authorization'], reply_markup=registration_keyboard())

    else:
        flag_setting_calendar = True
        await callback.message.edit_text("""
        📆 <b>Просмотр всех доступных ВКС за выбранный период</b>
        
        Отправьте начальную и конечную дату в формате: ГГГГ-ММ-ДД ГГГГ-ММ-ДД
        """)


async def setting_calendar(message) -> None:
    """
    После введенных пользователем дат уточняется корректность введенных данных
    :param message: Последнее сообщение пользователя
    :return: None
    """

    global flag_setting_calendar, panel_VKS
    flag_setting_calendar = False
    await message.answer(f'Выбранный период: c {start_data} по {end_data}', reply_markup=confirm_date_selection_VKS())


@router.callback_query(F.data == 'ok_date_selection')
async def ok_date_selection(callback: types.CallbackQuery) -> None:
    """
    Если даты введены верно, то возвращает все доступные ВКС
    :param callback:
    :return:
    """
    global panel_VKS, state

    g1, m1, d1 = map(int, start_data.split('-'))
    g2, m2, d2 = map(int, end_data.split('-'))

    name = None
    priority = None
    department = None
    organizer = None

    if len(state):
        state = ['booked', 'cancelled', 'started', 'ended']
    for i in filter_VKS:
        if i[0] == 'name':
            name = i[1]
        elif i[0] == 'priority':
            priority = int(i[1])
        elif i[0] == 'department':
            department = int(i[1])
        elif i[0] == 'organizer':
            organizer = i[1]

    result = get_meetings(saved_login, saved_password, from_date_time=datetime.datetime(g1, m1, d1),
                          to_date_time=datetime.datetime(g2, m2, d2), state=state,
                          priority=priority, name=name, department_id=department)
    if result == 'error':
        await callback.message.answer('Попробуйте ввести еще раз')
    elif not result:
        await callback.message.answer('Нет событий за выбранный период')
    else:
        current_page = 0
        panel_VKS = result
        await displaying_panel_VKS(callback, current_page)


async def displaying_panel_VKS(callback: types.CallbackQuery, current_page: int) -> None:
    """
    Отображает панель с ВКС
    :param callback:
    :param current_page:
    :return:
    """
    if panel_VKS == 'error':
        await callback.message.edit_text('error')
    elif not panel_VKS:
        await callback.message.edit_text('Нет событий за выбранный период')
    else:
        data = panel_VKS[current_page]
        if current_page == 0:
            result = f"""
{current_page + 1}/{len(panel_VKS)}              

<b>Ваша встреча id</b> {data['id']} - {data['name']}
<b>Начало:</b> {' '.join(data['startedAt'].split('.')[0].split('T'))}
<b>Конец:</b> {' '.join(data['endedAt'].split('.')[0].split('T'))}
<b>Продолжительность:</b> {data['duration']} мин.

🔗 {data['permalink']}
"""
            await callback.message.edit_text(result, reply_markup=start_switching_panel_VKS(current_page))

        elif current_page == len(panel_VKS) - 1:
            result = f"""
{current_page + 1}/{len(panel_VKS)}                

<b>Ваша встреча id</b> {data['id']} - {data['name']}
<b>Начало:</b> {' '.join(data['startedAt'].split('.')[0].split('T'))}
<b>Конец:</b> {' '.join(data['endedAt'].split('.')[0].split('T'))}
<b>Продолжительность:</b> {data['duration']} мин.

🔗 {data['permalink']}
"""
            await callback.message.edit_text(result, reply_markup=end_switching_panel_VKS(current_page))

        else:
            result = f"""
{current_page + 1}/{len(panel_VKS)}                

<b>Ваша встреча id</b> {data['id']} - {data['name']}
<b>Начало:</b> {' '.join(data['startedAt'].split('.')[0].split('T'))}
<b>Конец:</b> {' '.join(data['endedAt'].split('.')[0].split('T'))}
<b>Продолжительность:</b> {data['duration']} мин.

🔗 {data['permalink']}
"""
            await callback.message.edit_text(result, reply_markup=switching_panel_VKS(current_page))


@router.callback_query(F.data.startswith('switching_panel_VKS_right'))
async def switching_panel_VKS_right(callback: types.CallbackQuery) -> None:
    """
    Переключить вкладку вправо
    :param callback:
    :return:
    """
    current_page = int(callback.data.split('-')[1])
    await displaying_panel_VKS(callback, current_page + 1)


@router.callback_query(F.data.startswith('switching_panel_VKS_left'))
async def switching_panel_VKS_left(callback: types.CallbackQuery) -> None:
    """
    Переключить вкладку влево
    :param callback:
    :return:
    """
    current_page = int(callback.data.split('-')[1])
    await displaying_panel_VKS(callback, current_page - 1)


@router.callback_query(F.data == 'create_VKS')
async def create_vks(callback: types.CallbackQuery) -> None:
    """
    Запрашивает с пользователя данные, для создания новой ВКС
    :param callback:
    :return:
    """
    global flag_create_VKS

    flag_create_VKS = True
    await callback.message.answer(f"""
<b>📄 Заполните карточку будущего события</b>

<b>Название:</b>

<b>Настройка управления</b>
<b>Необходим микрофон?</b> (да/нет)
<b>Необходима камера?</b> (да/нет)
<b>Необходимо что это?</b> (да/нет)

<b>Количество участников:</b>
<b>Начало ВКС:</b>
<b>Продолжительность:</b>

<b>Во сколько вам напомнить о встрече?</b>
""")


async def register_VKS(data: list, message) -> None:
    """
    Регистрирует новую ВКС, используя ранее введенные данные
    :param data: Введенные пользователем данные для регистрации нового ВКС
    :param message:
    :return:
    """
    global flag_create_VKS
    print(1)
    (name, isMicrophoneOn, isVideoOn, isWaitingRoomEnabled, participantsCount, startedAt, duration,
     sendNotificationsAt) = list(data)
    print(2)
    print(name, isMicrophoneOn, isVideoOn, isWaitingRoomEnabled, participantsCount, startedAt, duration,
          sendNotificationsAt)
    print(3)
    g1, m1, d1 = map(int, startedAt.split('-'))
    g2, m2, d2 = map(int, sendNotificationsAt.split('-'))
    print(4)
    token = login(login=saved_login, password=saved_password)[0]['token']
    print(5)
    print(create_meetings(name=name, is_microphone_on=bool(isMicrophoneOn), is_video_on=bool(isVideoOn),
                          is_waiting_room_enabled=bool(isWaitingRoomEnabled),
                          participants_count=int(participantsCount), started_at=datetime.datetime(g1, m1, d1),
                          duration=int(duration), send_notifications_at=datetime.datetime(g2, m2, d2),
                          state='booked', token=token))
    print(6)
    flag_create_VKS = False
    print(7)
    await message.answer("ВКС успешно зарегистрирован")


@router.callback_query(F.data == 'yes_edit_profile')
async def yes_edit_profile(callback: types.CallbackQuery) -> None:
    global saved_password, flag_r
    if new_id == '1':
        update_user_info(saved_login, saved_password, password_new=new_information)
        saved_password = new_information
    elif new_id == '2':
        update_user_info(saved_login, saved_password, firs_name_new=new_information)
    elif new_id == '3':
        update_user_info(saved_login, saved_password, last_name_new=new_information)
    elif new_id == '4':
        update_user_info(saved_login, saved_password, middle_name_new=new_information)
    elif new_id == '5':
        update_user_info(saved_login, saved_password, email_new=new_information)
    elif new_id == '6':
        update_user_info(saved_login, saved_password, phone_new=new_information)
    elif new_id == '7':
        update_user_info(saved_login, saved_password, birthday_new=new_information)
    flag_r = False
    await callback.message.edit_text('Изменения успешно сохранены! Продолжите изменять профиль?',
                                     reply_markup=is_revers_edit_profile())


@router.callback_query(F.data == 'no_edit_profile')
async def no_edit_profile(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('Изменение профиля успешно отменено')


@router.message(F.text)
async def click_for_more(message: Message) -> None:
    global saved_login, saved_password, new_id, new_information, start_data, end_data, flag_filter

    if message.text.lower() == 'информация':
        await message.answer(text_data['information'])

    if flag_r:
        new_id, new_information = message.text.split('_')
        await message.answer(f"{text_data['edit'][new_id]}: {new_information}", reply_markup=is_edit_profile())

    else:
        if flag_setting_calendar:
            result = message.text.split()
            if len(result) == 2:
                start_data, end_data = result

                await setting_calendar(message)
            else:
                await message.answer("Отправьте начальную и конечную дату в формате: ГГГГ-ММ-ДД ГГГГ-ММ-ДД")

        elif is_open_profile:
            result = message.text.split()
            if len(result) == 2:
                saved_login, saved_password = result
                await send_profile_command(message)
            else:
                await message.answer("""
Введите логин и пароль в данном формате:

<b>Логин</b>
<b>Пароль</b>

Или пройдите регистрацию
""", reply_markup=registration_keyboard())

        elif flag_create_VKS:
            result = message.text.split()
            if len(result) == 8:
                await register_VKS(result, message)
            else:
                await message.answer("")

        elif flag_filter:
            result = message.text
            filter_VKS[-1].append(message.text)
            flag_filter = False

        else:
            await message.answer("Я не понимаю вас :(\nОбратитесь за помощью используя /help")


def register_user_handlers(dp: Dispatcher) -> None:
    dp.include_router(router)
