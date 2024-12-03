from aiogram.fsm.state import State, StatesGroup

class ChatStates(StatesGroup):
    START = State()
    CHAT = State()
    SPANISH_CHAT = State()
    CHINESE_CHAT = State()
