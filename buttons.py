from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup

products = KeyboardButton('Товары')
cart = KeyboardButton('Корзина')
registration = KeyboardButton('Регистрация')

btns = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3).row(products, cart, registration)

phone = KeyboardButton(text='поделиться телефоном', request_contact=True)
geo = KeyboardButton(text='поделиться местоположением', request_location=True)

reg_btns = ReplyKeyboardMarkup(resize_keyboard=True).add(phone).add(geo)
url_btn = InlineKeyboardButton(text="Ссылка на гугл", url='https://google.com')
inline_btn = InlineKeyboardButton(text="Текстовая кнопка", callback_data="test")

inline_btns = InlineKeyboardMarkup(row_width=2).add(url_btn, inline_btn)