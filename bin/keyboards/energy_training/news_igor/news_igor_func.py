from misc.util import ReplyKeyboardMarkup, KeyboardButton, types, datetime
from misc.loader import bot, moscow_tz

from data import yml_loader
from data.admin_db import is_admin_in_data, load_admin_data

# Функция для создания клавиатуры с вкладками
def create_month_keyboard_igor():
	months = [
		["button_message_september", "button_message_оctober"],
		["button_message_november", "button_message_december"]
	]

	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	for row in months:
		keyboard.add(*[KeyboardButton(yml_loader.news_igor_path["buttons"][month]) for month in row])
		
	keyboard.add(KeyboardButton(yml_loader.energy_training_data["button_energy_training"]))

	return keyboard

# Функция для проверки администратора и получения доступа без ожидания по времени
async def news_igor_handler(message: types.Message):
	# Получение текущей даты и времени
	current_datetime = datetime.datetime.now(moscow_tz)
	target_datetime = datetime.datetime(current_datetime.year, month=1, day=1, hour=0, minute=0, second=0)
	target_datetime = moscow_tz.localize(target_datetime)
		
	time_diff = target_datetime - current_datetime
		
	# Рассчитываем оставшееся время до целевой даты и времени
	days = time_diff.days
	hours = time_diff.seconds // 3600
	minutes = (time_diff.seconds % 3600) // 60

	if time_diff.total_seconds() > 0:
		await bot.send_message(message.chat.id, f"<b>👩🏻‍🦰💬 Вкладка — <code>{yml_loader.news_igor_path['news_igor']['button_news_igor']}</code> будет доступна через: <code>{days} дней {hours} часов и {minutes} минут.</code></b>")
	else:
		keyboard = create_month_keyboard_igor()
		await bot.send_message(message.chat.id, yml_loader.news_igor_path["news_igor"]["button_news_info"], reply_markup=keyboard)

# Обработчик вкладки "Сообщение за Месяц"
async def message_month_handler_igor(message: types.Message, month, button_name, button_info, buttons):
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

	for row in buttons:
		keyboard.add(*[KeyboardButton(btn) for btn in row])

	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		await bot.send_message(message.chat.id, button_info, reply_markup=keyboard)
	else:
		# Получение текущего времени
		current_time = datetime.datetime.now(moscow_tz)

		target_time = datetime.datetime(year=current_time.year, month=month, day=1, hour=0, minute=0, second=0)
		target_time = moscow_tz.localize(target_time)
		time_diff = target_time - current_time

		if time_diff.total_seconds() > 0:
			await bot.send_message(message.chat.id, f"<b>👩🏻‍🦰💬 Вкладка — <code>{button_name}</code> будет доступна через: <code>{time_diff.days} дней {time_diff.seconds // 3600} часов {(time_diff.seconds % 3600) // 60} минут.</code></b>")
		else:
			await bot.send_message(message.chat.id, button_info, reply_markup=keyboard)

# Использование обработчиков вкладок
async def message_september_handler_igor(message: types.Message):
	buttons = [
		[yml_loader.news_igor_path["buttons_month"]["button_nine"], yml_loader.news_igor_path["buttons_month"]["button_ten"]],
		[yml_loader.news_igor_path["buttons_month"]["button_one_thousand"], yml_loader.news_igor_path["buttons_month"]["button_move"]],
		[yml_loader.news_igor_path["news_igor"]["button_backward_month"]]
	]
	await message_month_handler_igor(message, 9, yml_loader.news_igor_path["buttons"]["button_message_september"], yml_loader.news_igor_path["button_message"]["button_message_september_info"], buttons)

async def message_оctober_handler_igor(message: types.Message):
	buttons = [
		[yml_loader.news_igor_path["buttons_month"]["button_thirteen"], yml_loader.news_igor_path["buttons_month"]["button_fourteen"]],
		[yml_loader.news_igor_path["buttons_month"]["button_fifteen"], yml_loader.news_igor_path["buttons_month"]["button_sixteen"]],
		[yml_loader.news_igor_path["buttons_month"]["button_seventeen"]],
		[yml_loader.news_igor_path["news_igor"]["button_backward_month"]]
	]
	await message_month_handler_igor(message, 10, yml_loader.news_igor_path["buttons"]["button_message_оctober"], yml_loader.news_igor_path["button_message"]["button_message_оctober_info"], buttons)

async def message_november_handler_igor(message: types.Message):
	buttons = [
		[yml_loader.news_igor_path["buttons_month"]["button_eight_twenty"], yml_loader.news_igor_path["buttons_month"]["button_nineteen"]],
		[yml_loader.news_igor_path["buttons_month"]["button_twenty"], yml_loader.news_igor_path["buttons_month"]["button_twenty_one"]],
		[yml_loader.news_igor_path["news_igor"]["button_backward_month"]]
	]
	await message_month_handler_igor(message, 11, yml_loader.news_igor_path["buttons"]["button_message_november"], yml_loader.news_igor_path["button_message"]["button_message_november_info"], buttons)

async def message_december_handler_igor(message: types.Message):
	buttons = [
		[yml_loader.news_igor_path["buttons_month"]["button_twenty_two"], yml_loader.news_igor_path["buttons_month"]["button_twenty_three"]],
		[yml_loader.news_igor_path["buttons_month"]["button_twenty_four"], yml_loader.news_igor_path["buttons_month"]["button_twenty_five"]],
		[yml_loader.news_igor_path["buttons_month"]["button_twenty_six"]],
		[yml_loader.news_igor_path["news_igor"]["button_backward_month"]]
	]
	await message_month_handler_igor(message, 12, yml_loader.news_igor_path["buttons"]["button_message_december"], yml_loader.news_igor_path["button_message"]["button_message_december_info"], buttons)

# Обработчик вкладки "Вернутся к выбору Месяца"
async def backward_month_handler_igor(message: types.Message):
	# Вкладки, которые будут отображаться
	months = [
		[yml_loader.news_igor_path["buttons"]["button_message_september"], yml_loader.news_igor_path["buttons"]["button_message_оctober"]],
		[yml_loader.news_igor_path["buttons"]["button_message_november"], yml_loader.news_igor_path["buttons"]["button_message_december"]],
		[yml_loader.energy_training_data["button_energy_training"]]
	]

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	for row in months:
		keyboard.add(*[KeyboardButton(month) for month in row])

	await bot.send_message(message.chat.id, yml_loader.news_igor_path["news_igor"]["button_news_info"], reply_markup=keyboard)