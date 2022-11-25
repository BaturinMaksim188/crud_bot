from aiogram.dispatcher.filters.state import State, StatesGroup


# Class of fundamental states
class States(StatesGroup):

    CHOICE_AWAIT = State()

    CHOICE_GET = State()
    CHOICE_GET_CHECK = State()
    CHOICE_GET_SUCCESS = State()

    CHOICE_SET = State()
    CHOICE_SET_LOGIN = State()
    CHOICE_SET_PASSWORD = State()
    CHOICE_SET_QUESTION = State()
    CHOICE_SET_ANSWER = State()
    CHOICE_SET_FINISH = State()
