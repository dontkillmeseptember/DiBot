from misc.util import InlineKeyboardMarkup, InlineKeyboardButton
from data import yml_loader

# Список названий месяцев на русском языке
MONTH_NAMES_RU = [
    yml_loader.calendar_path["months"]["january"], yml_loader.calendar_path["months"]["february"], 
    yml_loader.calendar_path["months"]["мarch"], yml_loader.calendar_path["months"]["april"],
    yml_loader.calendar_path["months"]["may"], yml_loader.calendar_path["months"]["june"], 
    yml_loader.calendar_path["months"]["july"], yml_loader.calendar_path["months"]["аugust"],
    yml_loader.calendar_path["months"]["september"], yml_loader.calendar_path["months"]["october"], 
    yml_loader.calendar_path["months"]["november"], yml_loader.calendar_path["months"]["december"]
]

# Словарь с датами и их обозначениями
SPECIAL_DATES = {
    # 2023
	# Январь
	"2023-01-07": {"emoji": "☦", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["jesus"]},
    "2023-01-13": {"emoji": "🧨", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["old_new_happy"]},
    "2023-01-14": {"emoji": "🧨", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["old_new_happy_two"]},
    "2023-01-25": {"emoji": "🎓", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["student"]},
    "2023-01-27": {"emoji": "🕯️", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["blokada"]},
	# Февраль
	"2023-02-01": {"emoji": "🥀", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["sasha"]},
    "2023-02-09": {"emoji": "🏆", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["herois"]},
	"2023-02-12": {"emoji": "💓", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["mom_igor"]},
	"2023-02-14": {"emoji": "💝", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["valentines_day"]},
    "2023-02-15": {"emoji": "🧪", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["half_life"]},
	"2023-02-23": {"emoji": "🎖", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["deffenses"]},
	"2023-02-24": {"emoji": "🍏", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["stev_jobs"]},
	"2023-02-27": {"emoji": "🍺", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["bavaria"]},
	# Март
	"2023-03-08": {"emoji": "💐", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["women_day"]},
    "2023-03-09": {"emoji": "🧑🏻", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["igor"]},
	"2023-03-14": {"emoji": "🧠", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["einstein"]},
	"2023-03-16": {"emoji": "🧪2️⃣", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["half_life_two"]},
	"2023-03-21": {"emoji": "🌱", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["equinox"]},
	"2023-03-23": {"emoji": "🌴", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["far_cry_one"]},
	"2023-03-27": {"emoji": "⛪️", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["far_cry_five"]},
	# Апрель
	"2023-04-01": {"emoji": "🎭", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["laughter"]},
    "2023-04-12": {"emoji": "🚀", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["astronaut_ru"]},
	"2023-04-14": {"emoji": "🚢", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["titanic"]},
	"2023-04-19": {"emoji": "🛰️", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["satellite"]},
	"2023-04-20": {"emoji": "🔥", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["hitler"]},
    "2023-04-21": {"emoji": "👰🏻‍♀️", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["wedding_slava"]},
	"2023-04-22": {"emoji": "👩🏻‍🦰", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["dinara"]},
	"2023-04-26": {"emoji": "☢️", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["aes"]},
	"2023-04-30": {"emoji": "☠️", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["dead_hitler"]},
	# Май
	"2023-05-01": {"emoji": "⚒", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["work"]},
    "2023-05-05": {"emoji": "🇫🇷", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["napoleon"]},
	"2023-05-09": {"emoji": "🕊️", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["victory"]},
    "2023-05-17": {"emoji": "🐺2️⃣", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["witcher_two"]},
    "2023-05-19": {"emoji": "🐺3️⃣", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["witcher_three"]},
    "2023-05-23": {"emoji": "⚽", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["lch"]},
	"2023-05-25": {"emoji": "🔔", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["sister"]},
	"2023-05-26": {"emoji": "❤️", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["mom_slava"]},
	# Июнь
	"2023-06-01": {"emoji": "👧🏻", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["children"]},
    "2023-06-12": {"emoji": "🇷🇺", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["russia"]},
	"2023-06-20": {"emoji": "👩🏻", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["shaman"]},
	"2023-06-26": {"emoji": "🧔🏻", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["nikita"]},
	"2023-06-22": {"emoji": "😢", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["war"]},
	"2023-06-28": {"emoji": "👑", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["аustralia"]},
	# Июль
    "2023-07-08": {"emoji": "👨‍👩‍👧", "text": yml_loader.calendar_path["calendar_info"]["calendar_jule"]["famaly"]},
    "2023-07-15": {"emoji": "👩🏼‍🌾", "text": yml_loader.calendar_path["calendar_info"]["calendar_jule"]["natasha"]},
    "2023-07-17": {"emoji": "👩🏻‍🎨", "text": yml_loader.calendar_path["calendar_info"]["calendar_jule"]["polina"]},
	"2023-07-27": {"emoji": "👨‍🚒", "text": yml_loader.calendar_path["calendar_info"]["calendar_jule"]["mchs"]},
	# Август
    "2023-08-05": {"emoji": "🪖", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["maksim"]},
    "2023-08-06": {"emoji": "👵🏼", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["babyshka"]},
    "2023-08-09": {"emoji": "☢️", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["atomic"]},
	"2023-08-12": {"emoji": "🏳️‍🌈", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["world_of_tank"]},
	"2023-08-14": {"emoji": "👵🏼", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["babyshka_two"]},
    "2023-08-27": {"emoji": "👰🏻‍♀️", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["wedding"]},
    # Сентябрь
	"2023-09-01": {"emoji": "📚", "text": yml_loader.calendar_path["calendar_info"]["calender_september"]["brain"]},
    "2023-09-05": {"emoji": "🐓", "text": yml_loader.calendar_path["calendar_info"]["calender_september"]["tottenham"]},
	"2023-09-14": {"emoji": "👴🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_september"]["dedushka"]},
    "2023-09-17": {"emoji": "🤵🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_september"]["slava"]},
    # Октябрь
	"2023-10-04": {"emoji": "✊🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["brat"]},
    "2023-10-05": {"emoji": "🤡", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["clowns"]},
    "2023-10-07": {"emoji": "🕴️", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["far_cry_six"]},
	"2023-10-14": {"emoji": "👸🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["quen"]},
	"2023-10-21": {"emoji": "🦓", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["far_cry_two"]},
	"2023-10-26": {"emoji": "🐺1️⃣", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["witcher_one"]},
    # Ноябрь
	"2023-11-05": {"emoji": "⚰️", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["kill_slava"]},
	"2023-11-09": {"emoji": "🧱", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["berlinskia"]},
	"2023-11-16": {"emoji": "👧🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["step_sister"]},
    "2023-11-17": {"emoji": "⛏", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["father"]},
    "2023-11-18": {"emoji": "🐘", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["far_cry_four"]},
	"2023-11-29": {"emoji": "🏝️", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["far_cry_three"]},
	# Декабрь
	"2023-12-03": {"emoji": "👩🏻‍💻", "text": yml_loader.calendar_path["calendar_info"]["calender_december"]["daria"]},
    "2023-12-10": {"emoji": "🕶️", "text": yml_loader.calendar_path["calendar_info"]["calender_december"]["cyberpank"]},
	"2023-12-31": {"emoji": "🇬🇪🇺🇦 — 🎄", "text": yml_loader.calendar_path["calendar_info"]["calender_december"]["alliance"]},
	# 2024
	# Январь
	"2024-01-07": {"emoji": "☦", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["jesus"]},
    "2024-01-13": {"emoji": "🧨", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["old_new_happy"]},
    "2024-01-14": {"emoji": "🧨", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["old_new_happy_two"]},
    "2024-01-25": {"emoji": "🎓", "text": yml_loader.calendar_path["calendar_info"]["calendar_january"]["student"]},
    # Февраль
	"2024-02-01": {"emoji": "🥀", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["sasha"]},
    "2024-02-09": {"emoji": "🏆", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["herois"]},
	"2024-02-14": {"emoji": "💝", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["valentines_day"]},
    "2024-02-15": {"emoji": "🧪", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["half_life"]},
	"2024-02-23": {"emoji": "🎖", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["deffenses"]},
	"2024-02-27": {"emoji": "🍺", "text": yml_loader.calendar_path["calendar_info"]["calendar_february"]["bavaria"]},
	# Март
	"2024-03-08": {"emoji": "💐", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["women_day"]},
    "2024-03-09": {"emoji": "🧑🏻", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["igor"]},
	"2024-03-16": {"emoji": "🧪2️⃣", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["half_life_two"]},
	"2024-03-21": {"emoji": "🌱", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["equinox"]},
	"2024-03-23": {"emoji": "🌴", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["far_cry_one"]},
	"2024-03-27": {"emoji": "⛪️", "text": yml_loader.calendar_path["calendar_info"]["calendar_march"]["far_cry_five"]},
	# Апрель
	"2024-04-01": {"emoji": "🎭", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["laughter"]},
    "2024-04-12": {"emoji": "🚀", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["astronaut_ru"]},
	"2024-04-14": {"emoji": "🚢", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["titanic"]},
	"2024-04-19": {"emoji": "🛰️", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["satellite"]},
	"2024-04-20": {"emoji": "🔥", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["hitler"]},
    "2024-04-22": {"emoji": "👩🏻‍🦰", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["dinara"]},
	"2024-04-30": {"emoji": "☠️", "text": yml_loader.calendar_path["calendar_info"]["calendar_april"]["dead_hitler"]},
	# Май
	"2024-05-01": {"emoji": "⚒", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["work"]},
    "2024-05-05": {"emoji": "🇫🇷", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["napoleon"]},
	"2024-05-09": {"emoji": "🕊️", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["victory"]},
    "2024-05-17": {"emoji": "🐺2️⃣", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["witcher_two"]},
    "2024-05-19": {"emoji": "🐺3️⃣", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["witcher_three"]},
    "2024-05-23": {"emoji": "⚽", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["lch"]},
	"2024-05-26": {"emoji": "❤️", "text": yml_loader.calendar_path["calendar_info"]["calendar_may"]["mom_slava"]},
	# Июнь
	"2024-06-01": {"emoji": "👧🏻", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["children"]},
    "2024-06-12": {"emoji": "🇷🇺", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["russia"]},
	"2024-06-20": {"emoji": "👩🏻", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["shaman"]},
	"2024-06-26": {"emoji": "🧔🏻", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["nikita"]},
	"2024-06-28": {"emoji": "👑", "text": yml_loader.calendar_path["calendar_info"]["calendar_june"]["аustralia"]},
	# Июль
    "2024-07-08": {"emoji": "👨‍👩‍👧", "text": yml_loader.calendar_path["calendar_info"]["calendar_jule"]["famaly"]},
    "2024-07-15": {"emoji": "👩🏼‍🌾", "text": yml_loader.calendar_path["calendar_info"]["calendar_jule"]["natasha"]},
    "2024-07-17": {"emoji": "👩🏻‍🎨", "text": yml_loader.calendar_path["calendar_info"]["calendar_jule"]["polina"]},
	"2024-07-27": {"emoji": "👨‍🚒", "text": yml_loader.calendar_path["calendar_info"]["calendar_jule"]["mchs"]},
	# Август
    "2024-08-05": {"emoji": "🪖", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["maksim"]},
    "2024-08-06": {"emoji": "👵🏼", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["babyshka"]},
    "2024-08-09": {"emoji": "☢️", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["atomic"]},
	"2024-08-12": {"emoji": "🏳️‍🌈", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["world_of_tank"]},
	"2024-08-14": {"emoji": "👵🏼", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["babyshka_two"]},
    "2024-08-27": {"emoji": "👰🏻‍♀️", "text": yml_loader.calendar_path["calendar_info"]["calender_аugust"]["wedding"]},
    # Сентябрь
	"2024-09-01": {"emoji": "📚", "text": yml_loader.calendar_path["calendar_info"]["calender_september"]["brain"]},
    "2024-09-05": {"emoji": "🐓", "text": yml_loader.calendar_path["calendar_info"]["calender_september"]["tottenham"]},
	"2024-09-14": {"emoji": "👴🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_september"]["dedushka"]},
    "2024-09-17": {"emoji": "🤵🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_september"]["slava"]},
    # Октябрь
	"2024-10-04": {"emoji": "✊🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["brat"]},
    "2024-10-05": {"emoji": "🤡", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["clowns"]},
    "2024-10-07": {"emoji": "🕴️", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["far_cry_six"]},
	"2024-10-14": {"emoji": "👸🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["quen"]},
	"2024-10-21": {"emoji": "🦓", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["far_cry_two"]},
	"2024-10-26": {"emoji": "🐺1️⃣", "text": yml_loader.calendar_path["calendar_info"]["calender_october"]["witcher_one"]},
    # Ноябрь
	"2024-11-05": {"emoji": "⚰️", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["kill_slava"]},
	"2024-11-09": {"emoji": "🧱", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["berlinskia"]},
	"2024-11-16": {"emoji": "👧🏻", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["step_sister"]},
    "2024-11-17": {"emoji": "⛏", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["father"]},
    "2024-11-18": {"emoji": "🐘", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["far_cry_four"]},
	"2024-11-29": {"emoji": "🏝️", "text": yml_loader.calendar_path["calendar_info"]["calender_november"]["far_cry_three"]},
	# Декабрь
	"2024-12-03": {"emoji": "👩🏻‍💻", "text": yml_loader.calendar_path["calendar_info"]["calender_december"]["daria"]},
    "2024-12-10": {"emoji": "🕶️", "text": yml_loader.calendar_path["calendar_info"]["calender_december"]["cyberpank"]},
	"2024-12-31": {"emoji": "🇬🇪🇺🇦 — 🎄", "text": yml_loader.calendar_path["calendar_info"]["calender_december"]["alliance"]}
}

# Список с информацией о каждом месяце и дне
MESSAGES = [
	# Июль
	[
		{
			"month": 7,
			"day": 10,
			"header": yml_loader.news_path['buttons_month']['button_one'],
			"message_text": yml_loader.news_path['message']['message_jule_one'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_0_0"))
		},
		{
			"month": 7,
			"day": 17,
			"header": yml_loader.news_path['buttons_month']['button_two'],
			"message_text": yml_loader.news_path["message"]["message_jule_two"],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_0_1")),
		},
		{
			"month": 7,
			"day": 24,
			"header": yml_loader.news_path['buttons_month']['button_three'],
			"message_text": yml_loader.news_path["message"]["message_jule_three"],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_0_2")),
		},
		{
			"month": 7,
			"day": 31,
			"header": yml_loader.news_path['buttons_month']['button_four'],
			"message_text": yml_loader.news_path["message"]["message_jule_four"],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_0_3")),
		}
	],
	# Август
	[
		{
			"month": 8,
			"day": 7,
			"header": yml_loader.news_path['buttons_month']['button_five'],
			"message_text": yml_loader.news_path['message']['message_august_one'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_1_0"))
		},
		{
			"month": 8,
			"day": 14,
			"header": yml_loader.news_path['buttons_month']['button_six'],
			"message_text": yml_loader.news_path['message']['message_august_two'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_1_1"))
		},
		{
			"month": 8,
			"day": 21,
			"header": yml_loader.news_path['buttons_month']['button_seven'],
			"message_text": yml_loader.news_path['message']['message_august_three'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_1_2"))
		},
		{
			"month": 8,
			"day": 28,
			"header": yml_loader.news_path['buttons_month']['button_eight'],
			"message_text": yml_loader.news_path['message']['message_august_four'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_1_3"))
		}
	],
	# Сентябрь
	[
		{
			"month": 9,
			"day": 4,
			"header": yml_loader.news_path['buttons_month']['button_nine'],
			"message_text": yml_loader.news_path['message']['message_september_one'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_2_0"))
		},
		{
			"month": 9,
			"day": 10,
			"header": yml_loader.news_path['buttons_month']['button_ten'],
			"message_text": yml_loader.news_path['message']['message_september_two'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_2_1"))
		},
		{
			"month": 9,
			"day": 26,
			"header": yml_loader.news_path['buttons_month']['button_one_thousand'],
			"message_text": yml_loader.news_path['message']['message_september_three'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_2_2"))
		},
		{
			"month": 9,
			"day": 26,
			"header": yml_loader.news_path['buttons_month']['button_move'],
			"message_text": yml_loader.news_path['message']['message_september_four'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_2_3"))
		}
	],
    # Октябрь
	[
        {
			"month": 10,
			"day": 3,
			"header": yml_loader.news_path['buttons_month']['button_thirteen'],
			"message_text": yml_loader.news_path['message']['message_october_one'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_path["button_keyboards"]["buttom_news_forward"], callback_data="forward_3_0"))
		}
	],
    # Ноябрь
	[
        
	],
    # Декабрь
	[
        
	]
]

# Список с информацией о каждом месяце и дне
MESSAGES_IGOR = [
	# Сентябрь
	[
		{
            "month": 9,
			"day": 5,
			"header": yml_loader.news_igor_path['buttons_month']['button_nine'],
			"message_text": yml_loader.news_igor_path['message']['message_september_one'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_forward"], callback_data="igor_forward_0_0"))
		},
		{
            "month": 9,
			"day": 12,
			"header": yml_loader.news_igor_path['buttons_month']['button_ten'],
			"message_text": yml_loader.news_igor_path['message']['message_september_two'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_forward"], callback_data="igor_forward_0_1"))
		},
		{
            "month": 9,
			"day": 19,
			"header": yml_loader.news_igor_path['buttons_month']['button_one_thousand'],
			"message_text": yml_loader.news_igor_path['message']['message_september_three'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_forward"], callback_data="igor_forward_0_2"))
		},
		{
            "month": 9,
			"day": 26,
			"header": yml_loader.news_igor_path['buttons_month']['button_move'],
			"message_text": yml_loader.news_igor_path['message']['message_september_four'],
			"inline_keyboard": InlineKeyboardMarkup().add(InlineKeyboardButton(yml_loader.news_igor_path["button_keyboards"]["buttom_news_forward"], callback_data="igor_forward_0_3"))
		}
	],
    # Октябрь
	[
        
	],
    # Ноябрь
	[
        
	],
    # Декабрь
	[
        
	]
]
