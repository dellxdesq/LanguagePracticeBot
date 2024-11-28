from aiogram.fsm.state import State, StatesGroup

# FSM States
class ChatStates(StatesGroup):
    START = State()
    CHAT = State()
    SPANISH_CHAT = State()
