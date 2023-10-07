from data import yml_loader
from misc.loader import dp

from keyboards.energy_training.news.news_func import (
    backward_month_handler,
    message_december_handler,
    message_jule_handler,
    message_november_handler,
    message_september_handler,
    message_аugust_handler,
    message_оctober_handler,
)

from keyboards.energy_training.news.message_func import (
    # Сообщения за 10.07.2023
	month_july_10_handler,
    # Сообщение за 17.07.2023
	month_july_17_handler,
    # Сообщения за 24.07.2023
	month_july_24_handler,
    # Сообщения за 31.07.2023
	month_july_31_handler,
    # Сообщения за 07.08.2023
	month_аugust_07_handler,
    # Сообщения за 14.08.2023
	month_аugust_14_handler,
    # Сообщения за 21.08.2023
    month_аugust_21_handler,
    # Сообщения за 28.08.2023
	month_аugust_28_handler,
	# Сообщения за 04.09.2023
	month_september_04_handler,
	# Сообщения за 11.09.2023
	month_september_11_handler,
	# Сообщения за 18.09.2023
	month_september_18_handler,
	# Сообщения за 25.09.2023
	month_september_25_handler,
	# Сообщения за 02.10.2023
	month_october_02_handler
)

# Свяжите функции обработки сообщений с диспетчером
# Сообщение за Июль
dp.register_message_handler(message_jule_handler, lambda message: message.text == yml_loader.news_path["buttons"]["button_message_jule"])

# Сообщения за Август
dp.register_message_handler(message_аugust_handler, lambda message: message.text == yml_loader.news_path["buttons"]["button_message_аugust"])

# Сообщения за Сентябрь
dp.register_message_handler(message_september_handler, lambda message: message.text == yml_loader.news_path["buttons"]["button_message_september"])

# Сообщения за Октябрь
dp.register_message_handler(message_оctober_handler, lambda message: message.text == yml_loader.news_path["buttons"]["button_message_оctober"])

# Сообщения за Ноябрь
dp.register_message_handler(message_november_handler, lambda message: message.text == yml_loader.news_path["buttons"]["button_message_november"])

# Сообщения за Декабрь
dp.register_message_handler(message_december_handler, lambda message: message.text == yml_loader.news_path["buttons"]["button_message_december"])

# Вернутся к выбору Месяца
dp.register_message_handler(backward_month_handler, lambda message: message.text == yml_loader.news_path["news"]["button_backward_month"])

# Вкладки "Сообщения за 10.07.2023"
dp.register_message_handler(month_july_10_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_one"])

# вкладка "Сообщение за 17.07.2023"
dp.register_message_handler(month_july_17_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_two"])

# вкладка "Сообщение за 24.07.2023"
dp.register_message_handler(month_july_24_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_three"])

# вкладка "Сообщение за 31.07.2023"
dp.register_message_handler(month_july_31_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_four"])

# вкладка "Сообщение за 07.08.2023"
dp.register_message_handler(month_аugust_07_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_five"])

# вкладка "Сообщение за 14.08.2023"
dp.register_message_handler(month_аugust_14_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_six"])

# вкладка "Сообщение за 21.08.2023"
dp.register_message_handler(month_аugust_21_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_seven"])

# вкладка "Сообщение за 28.08.2023"
dp.register_message_handler(month_аugust_28_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_eight"])

# вкладка "Сообщение за 04.09.2023"
dp.register_message_handler(month_september_04_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_nine"])

# вкладка "Сообщение за 11.09.2023"
dp.register_message_handler(month_september_11_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_ten"])

# вкладка "Сообщение за 18.09.2023"
dp.register_message_handler(month_september_18_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_one_thousand"])

# вкладка "Сообщение за 25.09.2023"
dp.register_message_handler(month_september_25_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_move"])

# вкладка "Сообщение за 02.10.2023"
dp.register_message_handler(month_october_02_handler, lambda message: message.text == yml_loader.news_path["buttons_month"]["button_thirteen"])