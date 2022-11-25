from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Buttons on start_message
b1_1 = KeyboardButton('Задать!')
b1_2 = KeyboardButton('Получить!')
b1_3 = KeyboardButton('Я передумал(')
kb_all = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_all.add(b1_1, b1_2).add(b1_3)

# ButtonToCheck
b2_1 = KeyboardButton('Проверить!')
kb_check = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_check.add(b2_1)

# ButtonToChange
b3_1 = KeyboardButton('Изменить!')
b3_2 = KeyboardButton('/cancel')
kb_change = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_change.add(b3_1).add(b3_2)

# ButtonToRegister
b4_1 = KeyboardButton('Зарегистрироваться!')
b4_2 = KeyboardButton('/cancel')
kb_register = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_register.add(b4_1).add(b4_2)

# ButtonToOut
b5_1 = KeyboardButton('/cancel')
kb_out = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_out.add(b5_1)

# Buttons To Questions
b6_1 = KeyboardButton('Имя питомца.')
b6_2 = KeyboardButton('Футбольная команда.')
b6_3 = KeyboardButton('Первая прочитанная книга.')
b6_4 = KeyboardButton('/cancel')
kb_questions = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_questions.add(b6_1).add(b6_2).add(b6_3).add(b6_4)

# ButtonToStart
b7_1 = KeyboardButton('/start')
kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start.add(b7_1)

# ButtonToView
b7_1 = KeyboardButton('Посмотреть!')
kb_view = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_view.add(b7_1)