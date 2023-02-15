import asyncio

from aiogram import Dispatcher, Router
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
from aiogram.filters import Command, Text

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboard_utils import *

router: Router = Router()

@router.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                        reply_markup=start_inline_kb)

            
@router.callback_query(Text(text='start'))
async def start_love_story(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['love_start'])
    await asyncio.sleep(1)
    await callback.message.answer(text=LEXICON_RU['first_q'],
                                reply_markup=first_q_kb)


@router.message(Text(text=['1 июля', '12 июля', '27 июля', '1 город', 'Случайно встретились еще в Москве', 'На кругу', 'Клепу', 'Ивана барабана']))
async def send_error_message(message: Message):
    await message.answer(LEXICON_RU['mistake'])


@router.message(Text(text='19 июля'))
async def send_second_q(message: Message):
    await message.answer_photo(photo=FSInputFile("photo/q1.png"), caption=LEXICON_RU['right_1_q'], 
                                reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer(text=LEXICON_RU['second_q'],
                        reply_markup=second_q_kb)


@router.message(Text(text=['3 города', '4 города']))
async def send_error_geography(message: Message):
    await message.answer(text=LEXICON_RU['many_geography'])


@router.message(Text(text='2 города'))
async def send_third_q(message: Message):
    await message.answer_photo(photo=FSInputFile("photo/q2.png"), caption=LEXICON_RU['right_2_q'],
                            reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer(text=LEXICON_RU['russian_city_intro'])
    await asyncio.sleep(2)
    await message.answer_photo(photo=FSInputFile("photo/q2_piter.png"), caption=LEXICON_RU['q2_piter'])
    await asyncio.sleep(1)
    await message.answer_photo(photo=FSInputFile("photo/q2_nn.png"), caption=LEXICON_RU['q2_nn'])
    await asyncio.sleep(1)
    await message.answer_photo(photo=FSInputFile("photo/q2_kazan.png"), caption=LEXICON_RU['q2_kazan'])
    await asyncio.sleep(1)
    await message.answer_photo(photo=FSInputFile("photo/q2_sochi.png"), caption=LEXICON_RU['q2_sochi'])
    await asyncio.sleep(1.5)
    await message.answer(text=LEXICON_RU['third_q'],
                        reply_markup=third_q_kb)

                    
@router.message(Text(text='Нас познакомил Иван'))
async def send_ivan(message: Message):
    await message.answer(text=LEXICON_RU['no_ivan'])


@router.message(Text(text='На речке (абсолютно не важно как 😂)'))
async def send_four_q(message: Message):
    await message.answer_photo(photo=FSInputFile("photo/q3.png"), caption=LEXICON_RU['right_3_q'],
                            reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer(text=LEXICON_RU['four_q'],
                        reply_markup=four_q_kb)

                    
@router.message(Text(text='Все с тобой понятно, так и знала, что не любишь меня'))
async def send_love_you(message: Message):
    await message.answer(text=LEXICON_RU['love_you'])


@router.message(Text(text='Конечно никого'))
async def send_five_q(message: Message):
    await message.answer_photo(photo=FSInputFile("photo/q4.png"), caption=LEXICON_RU['right_4_q'],
                            reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer_photo(photo=FSInputFile("photo/q4_klepa.png"), caption=LEXICON_RU['q4_klepa'])
    await asyncio.sleep(2)
    await message.answer(text=LEXICON_RU['five_q'],
                        reply_markup=five_q_kb)


@router.message(Text(text=['Вариант 4 кажется правильным', 'Приглядись к варианту 1', 'Безгранично, бесконечно, безумно ...', 'Вариант 3']))
async def send_summary(message: Message):
    await message.answer_photo(photo=FSInputFile("photo/q5.png"), caption=LEXICON_RU['right_5_q'],
                            reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer_photo(photo=FSInputFile("photo/q5_serious.png"), caption='Серьезной')
    await asyncio.sleep(2)
    await message.answer_photo(photo=FSInputFile("photo/q5_funny.png"), caption='Веселой')
    await asyncio.sleep(2)
    await message.answer_photo(photo=FSInputFile("photo/q5_strong.png"), caption='Сильной')
    await asyncio.sleep(2)
    await message.answer_photo(photo=FSInputFile("photo/q5_style.png"), caption='Стильной')
    await asyncio.sleep(2)
    await message.answer_photo(photo=FSInputFile("photo/q5_housy.png"), caption='Хозяйственной')
    await asyncio.sleep(2)
    await message.answer(text=LEXICON_RU['best_girl'])
    await asyncio.sleep(1.5)
    await message.answer_media_group(media=[FSInputFile("photo/q5_other.png"), FSInputFile("photo/q5_other_1.png"),
                                        FSInputFile("photo/q5_other_2.png"), FSInputFile("photo/q5_other_3.png"),
                                        FSInputFile("photo/q5_other_4.png"), FSInputFile("photo/q5_other_5.png"),
                                        FSInputFile("photo/q5_other_6.png"), FSInputFile("photo/q5_other_7.png")])
    await asyncio.sleep(1)
    await message.answer(text=LEXICON_RU['other_but_sim'], reply_markup=final_inline_kb)


@router.message(Text(text='final_task'))
async def send_final_task(message: Message):
    await message.answer_photo(photo=FSInputFile("photo/win_photo.png"))
    await asyncio.sleep(0.5)
    await message.answer(text=LEXICON_RU['final_text'])


