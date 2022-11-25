from aiogram.dispatcher import FSMContext
from Classes.MyClasses import States

from bot_dp import *

from keyboard.client_kb import *


async def cipher_v1(message):
    # !!!КЛЮЧИ!!!
    KEYH = {"М": 0, "У": 0, "Н1": 0, "И1": 0, "Ц": 0, "И2": 0, "П": 0, "А": 0, "Л": 0, "Ь": 0, "Н2": 0, "Ы": 0, "Й": 0}
    KEYV = {"Ц": 0, "Е": 0, "Н": 0, "Т": 0, "Р": 0}
    # !!!КЛЮЧИ ДЛЯ СОЗДАНИЯ МАТРИЦЫ!!!
    VerticalKey = ["Ц", "Е", "Н", "Т", "Р"]
    HorisontalKey = ["М", "У", "Н", "И", "Ц", "И", "П", "А", "Л", "Ь", "Н", "Ы", "Й"]
    # Матричный блок, инструменты
    uncount = False
    oncount = False
    outstr = ""
    MatrixBlock = []
    BlankMass = []
    j = 0
    ja = 0

    for i in message:
        j += 1
        ja += 1
        BlankMass.append(i)

        # Несоответствие количества символов
        # Нехватка
        if ja == len(message):
            if (j != len(HorisontalKey)) or (len(MatrixBlock) < len(VerticalKey)):

                r = (len(VerticalKey) * len(HorisontalKey)) - ((len(MatrixBlock) * len(HorisontalKey)) + len(BlankMass))
                if r != 0:
                    if r % len(HorisontalKey) != 0:
                        for bm in range(r % len(HorisontalKey)):
                            BlankMass.append('.')
                        MatrixBlock.append(BlankMass)
                        BlankMass = []
                    if len(MatrixBlock) < len(VerticalKey):
                        for mb in range(len(VerticalKey) - len(MatrixBlock)):
                            BlankMass = []
                            for bm in range(len(HorisontalKey)):
                                BlankMass.append('.')
                            MatrixBlock.append(BlankMass)
                            BlankMass = []
                uncount = True

        # Перебор
        if (ja < len(message)) and (len(MatrixBlock) == len(VerticalKey)):
            oncount = True

        # Соответствие
        if j == len(HorisontalKey):
            j = 0
            MatrixBlock.append(BlankMass)
            BlankMass = []

        # Условие на сходство длинны сообщения с количеством доступных символов в матричном блоке/недобором/перебором
        if (len(MatrixBlock) == len(VerticalKey) or uncount or oncount):
            uncount = False
            oncount = False

            # Горизонтальная сортировка
            k = 0
            for vk in KEYV:
                KEYV[vk] = MatrixBlock[k]
                k += 1
            SORTKEYV = sorted(KEYV.items())
            MatrixBlock = []

            # Вертикальная сортировка
            k = 0
            elem = []
            for hk in KEYH:
                for strng in SORTKEYV:
                    elem.append(strng[1][k])
                    KEYH[hk] = elem
                k += 1
                elem = []
            SORTKEYH = sorted(KEYH.items())

            # Преобразование в строку
            for strng in SORTKEYH:
                elem.append(strng[1])
            for s in elem:
                for n in s:
                    outstr += n

            # Возврат значения
    return outstr


async def decipher_v1(message):
    # !!!КЛЮЧИ!!!
    KEYH = {"М": 0, "У": 0, "Н1": 0, "И1": 0, "Ц": 0, "И2": 0, "П": 0, "А": 0, "Л": 0, "Ь": 0, "Н2": 0, "Ы": 0, "Й": 0}
    KEYV = {"Ц": 0, "Е": 0, "Н": 0, "Т": 0, "Р": 0}
    # !!!КЛЮЧИ ДЛЯ СОЗДАНИЯ МАТРИЦЫ!!!
    VerticalKey = ["Ц", "Е", "Н", "Т", "Р"]
    HorisontalKey = ["М", "У", "Н", "И", "Ц", "И", "П", "А", "Л", "Ь", "Н", "Ы", "Й"]
    # Матричный блок, инструменты
    DESORTV = {"Ц": 0, "Е": 0, "Н": 0, "Т": 0, "Р": 0}
    DESORTH = {"М": 0, "У": 0, "Н1": 0, "И1": 0, "Ц": 0, "И2": 0, "П": 0, "А": 0, "Л": 0, "Ь": 0, "Н2": 0, "Ы": 0,
               "Й": 0}
    oncount = False
    outstr = ""
    MatrixBlock = []
    BlankMass = []
    j = 0
    ja = 0

    for i in message:
        j += 1
        ja += 1
        BlankMass.append(i)

        # Перебор
        if (ja < len(message)) and (len(MatrixBlock) == len(HorisontalKey)):
            oncount = True


        # Соответствие
        if j == len(VerticalKey):
            j = 0
            MatrixBlock.append(BlankMass)
            BlankMass = []

        if (len(MatrixBlock) == len(HorisontalKey)) or oncount:
            oncount = False

            # Вертикальная десортировка
            k = 0
            elem = []
            for got in sorted(KEYH):
                DESORTH[got] = MatrixBlock[k]
                k += 1
            MatrixBlock = []

            # Горизонтальная десортировка
            elements = list(DESORTH.items())

            k = 0
            elem = []
            elemout = []
            for elm in range(len(DESORTV)):
                for el in elements:
                    if k < 5:
                        elem.append(el[1][k])
                    if len(elem) == len(DESORTH):
                        elemout.append(elem)
                        elem = []
                        k += 1

            k = 0
            for got in sorted(KEYV):
                DESORTV[got] = elemout[k]
                k += 1

            # Преобразование в строку
            elements = list(DESORTV.items())
            for el in elements:
                for elms in el[1]:
                    outstr += elms
    outstr = outstr.replace('.', '')
    return outstr


async def cipher_v2(message):
    return message
