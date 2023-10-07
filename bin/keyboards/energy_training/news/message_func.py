from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types, datetime
from misc.loader import bot, moscow_tz

from misc.loader import dp
from data import yml_loader

from data.base_glossary import MESSAGES

# Функция для отправки сообщений с задержкой до указанной даты и времени
async def send_delayed_message(chat_id, day_info, inline_keyboard):
	current_datetime = datetime.datetime.now(moscow_tz)
	target_datetime = datetime.datetime(year=current_datetime.year, month=day_info["month"], day=day_info["day"], hour=0, minute=0, second=0)
	target_datetime = moscow_tz.localize(target_datetime)

	time_diff = target_datetime - current_datetime
	hours = time_diff.seconds // 3600
	minutes = (time_diff.seconds % 3600) // 60

	if time_diff.total_seconds() > 0:
		await bot.send_message(chat_id, f"<b>👩🏻‍🦰💬 Вкладка: {day_info['header']}</b>\n" \
						 				f"<b>   	     ↳ </b><b>будет доступна через: ⌛️<code>{hours} часов {minutes} минут</code></b>")
	else:
		await bot.send_message(chat_id, day_info["message_text"]["news_one"], reply_markup=inline_keyboard)

# Функция для обработки кнопки "Предыдущий часть сообщения" для второй страницы
async def process_callback_forward(callback_query: types.CallbackQuery, month_index, day_index):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_backward"], callback_data=f"backward_{month_index}_{day_index}"))

	await bot.edit_message_text(MESSAGES[month_index][day_index]["message_text"]["news_two"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Функция для обработки кнопки "Предыдущий часть сообщения" для второй страницы, если в сообщение две кнопки
async def process_callback_forward_keyboards(callback_query: types.CallbackQuery, month_index, day_index):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_backward"], callback_data=f"backward_{month_index}_{day_index}"),
		InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data=f"forward_{month_index}_{day_index}_two")
	)

	await bot.edit_message_text(MESSAGES[month_index][day_index]["message_text"]["news_two"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_two(callback_query: types.CallbackQuery, month_index, day_index):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_backward"], callback_data=f"backward_{month_index}_{day_index}_two"))

	await bot.edit_message_text(MESSAGES[month_index][day_index]["message_text"]["news_three"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Функция для обработки кнопки "Следующая часть сообщения" для первой страницы
async def process_callback_backward(callback_query: types.CallbackQuery, month_index, day_index):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data=f"forward_{month_index}_{day_index}"))

	await bot.edit_message_text(MESSAGES[month_index][day_index]["message_text"]["news_one"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Функция для отправки сообщений за конкретный день
async def send_day_message(month_index, day_index, callback_query):
	day_info = MESSAGES[month_index][day_index]
	inline_keyboard = day_info["inline_keyboard"]
	await send_delayed_message(callback_query.from_user.id, day_info, inline_keyboard)

# Обработчик для кнопки "Сообщение за 02.10.2023"
async def month_october_02_handler(callback_query: types.CallbackQuery):
	await send_day_message(3, 0, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_3_0")
async def process_callback_forward_october_02(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 3, 0)

@dp.callback_query_handler(lambda query: query.data == "backward_3_0")
async def process_callback_backward_october_02(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 3, 0)

@dp.callback_query_handler(lambda query: query.data == "forward_3_0_two")
async def process_callback_forward_october_02(callback_query: types.CallbackQuery):
	await process_callback_forward_two(callback_query, 3, 0)

@dp.callback_query_handler(lambda query: query.data == "backward_3_0_two")
async def process_callback_backward_october_02(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 3, 0)

# Обработчик для кнопки "Сообщение за 25.09.2023"
async def month_september_25_handler(callback_query: types.CallbackQuery):
	await send_day_message(2, 3, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_2_3")
async def process_callback_forward_september_25(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 2, 3)

@dp.callback_query_handler(lambda query: query.data == "backward_2_3")
async def process_callback_backward_september_25(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 2, 3)

# Обработчик для кнопки "Сообщение за 18.09.2023"
async def month_september_18_handler(callback_query: types.CallbackQuery):
	await send_day_message(2, 2, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_2_2")
async def process_callback_forward_september_18(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 2, 2)

@dp.callback_query_handler(lambda query: query.data == "backward_2_2")
async def process_callback_backward_september_18(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 2, 2)

# Обработчик для кнопки "Сообщение за 11.09.2023"
async def month_september_11_handler(callback_query: types.CallbackQuery):
	await send_day_message(2, 1, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_2_1")
async def process_callback_forward_september_11(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 2, 1)

@dp.callback_query_handler(lambda query: query.data == "backward_2_1")
async def process_callback_backward_september_11(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 2, 1)

# Обработчик для кнопки "Сообщение за 04.09.2023"
async def month_september_04_handler(callback_query: types.CallbackQuery):
	await send_day_message(2, 0, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_2_0")
async def process_callback_forward_september_04(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 2, 0)

@dp.callback_query_handler(lambda query: query.data == "backward_2_0")
async def process_callback_backward_september_04(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 2, 0)

# Обработчик для кнопки "Сообщение за 28.08.2023"
async def month_аugust_28_handler(callback_query: types.CallbackQuery):
	await send_day_message(1, 3, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_1_3")
async def process_callback_forward_аugust_28(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 1, 3)

@dp.callback_query_handler(lambda query: query.data == "backward_1_3")
async def process_callback_backward_аugust_28(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 1, 3)

# Обработчик для кнопки "Сообщение за 21.08.2023"
async def month_аugust_21_handler(callback_query: types.CallbackQuery):
	await send_day_message(1, 2, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_1_2")
async def process_callback_forward_аugust_21(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 1, 2)

@dp.callback_query_handler(lambda query: query.data == "backward_1_2")
async def process_callback_backward_аugust_21(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 1, 2)

@dp.callback_query_handler(lambda query: query.data == "forward_1_2_two")
async def process_callback_forward_аugust_14(callback_query: types.CallbackQuery):
	await process_callback_forward_two(callback_query, 1, 2)

@dp.callback_query_handler(lambda query: query.data == "backward_1_2_two")
async def process_callback_backward_аugust_14(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 1, 2)

# Обработчик для кнопки "Сообщение за 14.08.2023"
async def month_аugust_14_handler(callback_query: types.CallbackQuery):
	await send_day_message(1, 1, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_1_1")
async def process_callback_forward_аugust_14(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 1, 1)

@dp.callback_query_handler(lambda query: query.data == "backward_1_1")
async def process_callback_backward_аugust_14(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 1, 1)

@dp.callback_query_handler(lambda query: query.data == "forward_1_1_two")
async def process_callback_forward_аugust_14(callback_query: types.CallbackQuery):
	await process_callback_forward_two(callback_query, 1, 1)

@dp.callback_query_handler(lambda query: query.data == "backward_1_1_two")
async def process_callback_backward_аugust_14(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 1, 1)

# Обработчик для кнопки "Сообщение за 07.08.2023"
async def month_аugust_07_handler(callback_query: types.CallbackQuery):
	await send_day_message(1, 0, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_1_0")
async def process_callback_forward_аugust_07(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 1, 0)

@dp.callback_query_handler(lambda query: query.data == "backward_1_0")
async def process_callback_backward_аugust_07(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 1, 0)

# Обработчик для кнопки "Сообщение за 31.07.2023"
async def month_july_31_handler(callback_query: types.CallbackQuery):
	await send_day_message(0, 3, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_0_3")
async def process_callback_forward_july_31(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 0, 3)

@dp.callback_query_handler(lambda query: query.data == "backward_0_3")
async def process_callback_backward_july_31(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 0, 3)

# Обработчик для кнопки "Сообщение за 24.07.2023"
async def month_july_24_handler(callback_query: types.CallbackQuery):
	await send_day_message(0, 2, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_0_2")
async def process_callback_forward_july_24(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 0, 2)

@dp.callback_query_handler(lambda query: query.data == "backward_0_2")
async def process_callback_backward_july_24(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 0, 2)

# Обработчик для кнопки "Сообщение за 17.07.2023"
async def month_july_17_handler(callback_query: types.CallbackQuery):
	await send_day_message(0, 1, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_0_1")
async def process_callback_forward_july_17(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 0, 1)

@dp.callback_query_handler(lambda query: query.data == "backward_0_1")
async def process_callback_backward_july_17(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 0, 1)

# Обработчик для кнопки "Сообщение за 10.07.2023"
async def month_july_10_handler(callback_query: types.CallbackQuery):
	await send_day_message(0, 0, callback_query)

@dp.callback_query_handler(lambda query: query.data == "forward_0_0")
async def process_callback_forward_july_10(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 0, 0)

@dp.callback_query_handler(lambda query: query.data == "backward_0_0")
async def process_callback_backward_july_10(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 0, 0)

@dp.callback_query_handler(lambda query: query.data == "forward_0_0_two")
async def process_callback_forward_july_10(callback_query: types.CallbackQuery):
	await process_callback_forward_two(callback_query, 0, 0)

@dp.callback_query_handler(lambda query: query.data == "backward_0_0_two")
async def process_callback_backward_july_10(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 0, 0)