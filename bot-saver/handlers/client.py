from func.client_func import *
from database.sqlite_db import *


# ------------------------------------------------------FSMContext------------------------------------------------------
@dp.message_handler(state="*", commands="cancel")
async def command_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Вам неоткуда выходить.", reply_markup=kb_start)
        return
    else:
        await state.finish()
        await message.answer("Завершено.", reply_markup=kb_start)


# ------------------------------------------------------FSMContext------------------------------------------------------

# handler for command "/start"
@dp.message_handler(commands="start", state="*")
async def command_start(message: types.Message):
    await States.CHOICE_AWAIT.set()
    await message.answer("Привет! Ты хочешь задать учётные данные или получить их?", reply_markup=kb_all)


# handler for button to SET or GET or FINISH state
@dp.message_handler(content_types=['text'], state=States.CHOICE_AWAIT)
async def command_start(message: types.Message, state: FSMContext):
    if message.text == "Задать!":
        await States.CHOICE_SET.set()
        await message.answer("Нужно проверить, есть ли у вас сохранённые данные!", reply_markup=kb_check)
    elif message.text == "Получить!":
        await States.CHOICE_GET.set()
        await message.answer("Нужно проверить, есть ли у вас сохранённые данные!", reply_markup=kb_check)
    elif message.text == "Я передумал(":
        await state.finish()
        await message.answer("Вы отменили выбор! Нажмите /start")
    else:
        await state.finish()
        await message.answer("Вы повели себя неправильно!\n\nПовторите команду /start")


# ______________________________________________________________________________________________________________________
# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_AWAIT)
async def not_a_text_v1(message: types.Message):
    await message.answer("Воспользуйтесь клавиатурой или нажмите /cancel")


# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_SET)
async def not_a_text_v1(message: types.Message):
    await message.answer("Воспользуйтесь клавиатурой или нажмите /cancel")


# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_SET_LOGIN)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")


# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_SET_PASSWORD)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")


# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_SET_QUESTION)
async def not_a_text_v1(message: types.Message):
    await message.answer("Воспользуйтесь клавиатурой или введите /cancel")


# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_SET_ANSWER)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")


# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_SET_FINISH)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")

# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_GET)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")

# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_GET_CHECK)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")

# No text
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_GET_SUCCESS)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")

# ______________________________________________________________________________________________________________________

# Text to CHOICE_GET handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_GET)
async def choice_get(message: types.Message, state=FSMContext):

    async with state.proxy() as data:
        data['userid'] = message.from_user.id

    out = await check_user(message.from_user.id)

    if out:
        await message.answer("У вас уже есть запись!", reply_markup=kb_view)
        await States.CHOICE_GET_CHECK.set()
    elif not out:
        await message.answer("Вы новый пользователь!", reply_markup=kb_register)
        await States.CHOICE_SET_LOGIN.set()
    else:
        await message.answer("Некорректный результат, повторите ввод!", reply_markup=kb_check)


# Text to CHOICE_GET_CHECK handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_GET_CHECK)
async def choice_get_question(message: types.Message, state=FSMContext):

    async with state.proxy() as data:
        data['userid'] = message.from_user.id

    result = await sql_get_userdata(state)

    await message.answer(f"Ваш ключевой вопрос: \n{result[2]}\nОтветьте на него, чтобы получить данные.")
    await States.CHOICE_GET_SUCCESS.set()


# Text to CHOICE_GET_SUCCESS handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_GET_SUCCESS)
async def choice_get_finish(message: types.Message, state=FSMContext):

    async with state.proxy() as data:
        data['userid'] = message.from_user.id

    result = await sql_get_userdata(state)

    if message.text.lower().replace(' ', '') == result[3]:
        await message.answer(f"Ваши данные: \nЛогин: {result[0]}\nПароль: {result[1]}\nДата создания: {result[4]}\nБудьте здоровы!")
        await state.finish()
        await States.CHOICE_AWAIT.set()
        await message.answer("Что вы хотите сделать дальше?", reply_markup=kb_all)
    else:
        await state.finish()
        await message.answer("Вы ответили неверно! Сессия завершена.")
        await States.CHOICE_AWAIT.set()
        await message.answer("Что вы хотите сделать дальше?", reply_markup=kb_all)


# Text to CHOICE_SET handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_SET)
async def choice_check(message: types.Message, state=FSMContext):

    out = await check_user(message.from_user.id)

    async with state.proxy() as data:
        data['userid'] = message.from_user.id

    if message.text == "Проверить!":
        if out:
            await message.answer("У вас уже есть запись!", reply_markup=kb_change)
        else:
            await message.answer("Вы новый пользователь!", reply_markup=kb_register)
        await States.CHOICE_SET_LOGIN.set()
    else:
        await message.answer("Некорректный результат, повторите ввод!", reply_markup=kb_check)


# Text to CHOICE_SET_LOGIN handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_SET_LOGIN)
async def choice_create_login(message: types.Message, state=FSMContext):

    if message.text == "Изменить!":
        await message.answer("Введите логин.", reply_markup=kb_out)
        await States.CHOICE_SET_PASSWORD.set()

    elif message.text == "Зарегистрироваться!":
        await message.answer("Введите логин.", reply_markup=kb_out)
        await States.CHOICE_SET_PASSWORD.set()

    else:
        out = await check_user(message.from_user.id)
        if out:
            await message.answer("Некорректный результат, повторите ввод!", reply_markup=kb_change)
            await States.CHOICE_SET_LOGIN.set()
        else:
            await message.answer("Некорректный результат, повторите ввод!", reply_markup=kb_register)
            await States.CHOICE_SET_LOGIN.set()


# Text to CHOICE_SET_PASSWORD handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_SET_PASSWORD)
async def choice_create_password(message: types.Message, state=FSMContext):
    await message.answer("Введите пароль.", reply_markup=kb_out)
    async with state.proxy() as data:
        data['login'] = message.text
    await States.CHOICE_SET_QUESTION.set()


# Text to CHOICE_SET_QUESTION handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_SET_QUESTION)
async def choice_create_question(message: types.Message, state=FSMContext):
    await message.answer("Вы должны выбрать ключевой вопрос, ответ на который будет давать доступ к информации при "
                         "попытке её получения. \nНа выбор у вас есть три варианта:\n1) Имя питомца.\n2) Название "
                         "любимой футбольной комманды.\n3) Название первой прочитанной вами книги.\n\n(Справка: "
                         "Ответы должны быть односложными и не содержать никаких символов, кроме букв.)",
                         reply_markup=kb_questions)

    async with state.proxy() as data:
        data['password'] = message.text

    await States.CHOICE_SET_ANSWER.set()


# Text to CHOICE_SET_ANSWER handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_SET_ANSWER)
async def choice_create_answer(message: types.Message, state=FSMContext):
    if message.text in ["Имя питомца.", "Футбольная команда.", "Первая прочитанная книга."]:
        await message.answer("Вы выбрали тип вашего вопроса! Теперь ответьте на него.", reply_markup=kb_out)
        async with state.proxy() as data:
            data['question'] = message.text
        await States.CHOICE_SET_FINISH.set()
    else:
        await message.answer("Некорректный результат, повторите ввод!", reply_markup=kb_questions)
        await States.CHOICE_SET_ANSWER.set()


# Text to CHOICE_SET_FINISH handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_SET_FINISH)
async def choice_set_finish(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['answer'] = message.text.lower().replace(' ', '')
        data['datetime'] = message.date

    if check_user(message.from_user.id):
        await on_delete_func(state)

    await sql_add_userdata(state)

    await state.finish()
    await message.answer("Вы создали запись!")
    await States.CHOICE_AWAIT.set()
    await message.answer("Что вы хотите сделать дальше?", reply_markup=kb_all)


# ----------------------------------------------------------------------------------------------------------------------
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start', state=None)
