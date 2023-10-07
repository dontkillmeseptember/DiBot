from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types, datetime
from misc.loader import bot, moscow_tz

from misc.loader import dp
from data import yml_loader

from data.base_glossary import MESSAGES_IGOR

# Функция для отправки сообщений с задержкой до указанной даты и времени
async def send_delayed_message(chat_id, day_info, inline_keyboard):
	current_datetime = datetime.datetime.now(moscow_tz)
	target_datetime = datetime.datetime(year=current_datetime.year, month=day_info["month"], day=day_info["day"], hour=0, minute=0, second=0)
	target_datetime = moscow_tz.localize(target_datetime)

	time_diff = target_datetime - current_datetime
	days = time_diff.days
	hours = time_diff.seconds // 3600
	minutes = (time_diff.seconds % 3600) // 60

	if time_diff.total_seconds() > 0:
		await bot.send_message(chat_id, f"<b>👩🏻‍🦰💬 {day_info['header']} — будет доступна через: <code>{days} дней {hours} часов {minutes} минут.</code></b>")
	else:
		await bot.send_message(chat_id, day_info["message_text"]["news_one"], reply_markup=inline_keyboard)

# Функция для обработки кнопки "Предыдущий часть сообщения" для второй страницы
async def process_callback_forward(callback_query: types.CallbackQuery, month_index, day_index):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_backward"], callback_data=f"igor_backward_{month_index}_{day_index}"))

	await bot.edit_message_text(MESSAGES_IGOR[month_index][day_index]["message_text"]["news_two"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Функция для обработки кнопки "Предыдущий часть сообщения" для второй страницы, если в сообщение две кнопки
async def process_callback_forward_keyboards(callback_query: types.CallbackQuery, month_index, day_index):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_backward"], callback_data=f"igor_backward_{month_index}_{day_index}"),
		InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_forward"], callback_data=f"igor_forward_{month_index}_{day_index}_two")
	)

	await bot.edit_message_text(MESSAGES_IGOR[month_index][day_index]["message_text"]["news_two"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_two(callback_query: types.CallbackQuery, month_index, day_index):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_backward"], callback_data=f"igor_backward_{month_index}_{day_index}_two"))

	await bot.edit_message_text(MESSAGES_IGOR[month_index][day_index]["message_text"]["news_three"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Функция для обработки кнопки "Следующая часть сообщения" для первой страницы
async def process_callback_backward(callback_query: types.CallbackQuery, month_index, day_index):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_forward"], callback_data=f"igor_forward_{month_index}_{day_index}"))

	await bot.edit_message_text(MESSAGES_IGOR[month_index][day_index]["message_text"]["news_one"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Функция для отправки сообщений за конкретный день
async def send_day_message(month_index, day_index, callback_query):
	day_info = MESSAGES_IGOR[month_index][day_index]
	inline_keyboard = day_info["inline_keyboard"]
	await send_delayed_message(callback_query.from_user.id, day_info, inline_keyboard)

# Обработчик для кнопки "Сообщение за 25.09.2023"
async def month_september_25_handler(callback_query: types.CallbackQuery):
	await send_day_message(0, 3, callback_query)

@dp.callback_query_handler(lambda query: query.data == "igor_forward_0_3")
async def process_callback_forward_september_25(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 0, 3)

@dp.callback_query_handler(lambda query: query.data == "igor_backward_031")
async def process_callback_backward_september_25(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 0, 3)

# Обработчик для кнопки "Сообщение за 19.09.2023"
async def month_september_19_handler(callback_query: types.CallbackQuery):
	await send_day_message(0, 2, callback_query)

@dp.callback_query_handler(lambda query: query.data == "igor_forward_0_2")
async def process_callback_forward_september_19(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 0, 2)

@dp.callback_query_handler(lambda query: query.data == "igor_backward_0_2")
async def process_callback_backward_september_19(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 0, 2)

@dp.callback_query_handler(lambda query: query.data == "igor_forward_0_2_two")
async def process_callback_forward_september_19(callback_query: types.CallbackQuery):
	await process_callback_forward_two(callback_query, 0, 2)

@dp.callback_query_handler(lambda query: query.data == "igor_backward_0_2_two")
async def process_callback_forward_september_19(callback_query: types.CallbackQuery):
	await process_callback_forward_keyboards(callback_query, 0, 2)

# Обработчик для кнопки "Сообщение за 12.09.2023"
async def month_september_12_handler(callback_query: types.CallbackQuery):
	await send_day_message(0, 1, callback_query)

@dp.callback_query_handler(lambda query: query.data == "igor_forward_0_1")
async def process_callback_forward_september_12(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 0, 1)

@dp.callback_query_handler(lambda query: query.data == "igor_backward_0_1")
async def process_callback_backward_september_12(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 0, 1)

# Обработчик для кнопки "Сообщение за 05.09.2023"
async def month_september_05_handler(callback_query: types.CallbackQuery):
	await send_day_message(0, 0, callback_query)

@dp.callback_query_handler(lambda query: query.data == "igor_forward_0_0")
async def process_callback_forward_september_05(callback_query: types.CallbackQuery):
	await process_callback_forward(callback_query, 0, 0)

@dp.callback_query_handler(lambda query: query.data == "igor_backward_0_0")
async def process_callback_backward_september_05(callback_query: types.CallbackQuery):
	await process_callback_backward(callback_query, 0, 0)