from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start_inline_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
                                                                                text='А я люблю тебя❤',
                                                                                callback_data='start'
                                                                                )]])

#################################################

first_q_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                    resize_keyboard=True,
                                                    keyboard=[[KeyboardButton(text='1 июля')],
                                                            [KeyboardButton(text='12 июля')],
                                                            [KeyboardButton(text='19 июля')],
                                                            [KeyboardButton(text='27 июля')]])

#################################################

second_q_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                    resize_keyboard=True,
                                                    keyboard=[[KeyboardButton(text='1 город')],
                                                            [KeyboardButton(text='2 города')],
                                                            [KeyboardButton(text='3 города')],
                                                            [KeyboardButton(text='4 города')]])

##################################################

third_q_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                    resize_keyboard=True,
                                                    keyboard=[[KeyboardButton(text='На кругу')],
                                                            [KeyboardButton(text='Нас познакомил Иван')],
                                                            [KeyboardButton(text='Случайно встретились еще в Москве')],
                                                            [KeyboardButton(text='На речке (абсолютно не важно как 😂)')]])

##################################################

four_q_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                    resize_keyboard=True,
                                                    keyboard=[[KeyboardButton(text='Конечно никого')],
                                                            [KeyboardButton(text='Клепу')],
                                                            [KeyboardButton(text='Ивана барабана')],
                                                            [KeyboardButton(text='Все с тобой понятно, так и знала, что не любишь меня')]])

##################################################

five_q_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                    resize_keyboard=True,
                                                    keyboard=[[KeyboardButton(text='Вариант 4 кажется правильным')],
                                                            [KeyboardButton(text='Приглядись к варианту 1')],
                                                            [KeyboardButton(text='Безгранично, бесконечно, безумно ...')],
                                                            [KeyboardButton(text='Вариант 3')]])

###################################################

final_inline_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
                                                                                text='Последнее задание (обещаю😅)',
                                                                                callback_data='final_task'
                                                                                )]])