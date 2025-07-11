from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    regLogin = State()
    regPassword = State()
    regEmail = State()
    regName = State()
    regPhone = State()
