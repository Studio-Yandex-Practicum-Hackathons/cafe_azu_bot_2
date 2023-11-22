from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def cart(user_cart):
    """Главная клавиатура меню сетов."""
    keyboard = InlineKeyboardMarkup()
    if user_cart is not False:
        keyboard.add(
            InlineKeyboardButton(text='✅ Оформить', callback_data='checkout')
        )
    keyboard.add(
        InlineKeyboardButton(text='💰 Каталог', callback_data='catalog')
    )
    return keyboard


def catalog():
    """Клавиатура каталога выбора сетов."""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text='Сеты за 400 рублей', callback_data='catalog_set400'
        ),
        InlineKeyboardButton(
            text='Сеты за 500 рублей', callback_data='catalog_set500'
        ),
        InlineKeyboardButton(
            text='Сеты за 700 рублей', callback_data='catalog_set700'
        ),
    )
    return keyboard


def catalog_set400():
    """Клавиатура сетов за 400 рублей."""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text='Сет №1', callback_data='get_eat_set1_400'),
        InlineKeyboardButton(text='Cет №2', callback_data='get_eat_set2_400'),
        InlineKeyboardButton(text='Cет №3', callback_data='get_eat_set3_400'),
    )
    keyboard.add(
        InlineKeyboardButton(text='🎓 Корзина', callback_data='go_to_cart')
    )
    keyboard.add(
        InlineKeyboardButton(text='Вернуться', callback_data='catalog')
    )
    return keyboard


def catalog_set500():
    """Клавиатура сетов за 500 рублей."""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text='Сет №4', callback_data='get_eat_set4_500'),
        InlineKeyboardButton(text='Cет №5', callback_data='get_eat_set5_500'),
        InlineKeyboardButton(text='Cет №6', callback_data='get_eat_set6_500'),
    )
    keyboard.add(
        InlineKeyboardButton(text='🎓 Корзина', callback_data='go_to_cart')
    )
    keyboard.add(
        InlineKeyboardButton(text='Вернуться', callback_data='catalog')
    )
    return keyboard


def catalog_set700():
    """Клавиатура сетов за 700 рублей."""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text='Сет №7', callback_data='get_eat_set7_700'),
        InlineKeyboardButton(text='Cет №8', callback_data='get_eat_set8_700'),
        InlineKeyboardButton(text='Cет №9', callback_data='get_eat_set9_700'),
    )
    keyboard.add(
        InlineKeyboardButton(text='🎓 Корзина', callback_data='go_to_cart')
    )
    keyboard.add(
        InlineKeyboardButton(text='Вернуться', callback_data='catalog')
    )
    return keyboard


def item_add(item, catalog_tag, price, user_cart):
    """Клавиатура для корзины - добавить/убрать сет."""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text='Добавить',
            callback_data='add_{item}_{price}'.format(
                item=item, price=price
            )
        ),
        InlineKeyboardButton(
            text='Убрать',
            callback_data='del_{item}_{price}'.format(
                item=item, price=price
            )
        ),
    )
    if user_cart is not False:
        keyboard.add(
            InlineKeyboardButton(
                text='🎓 Корзина', callback_data='go_to_cart'
            ),
            InlineKeyboardButton(
                text='✅ Оформить', callback_data='checkout'
            )
        )
    keyboard.add(
        InlineKeyboardButton(
            text='Вернуться', callback_data='catalog_{tag}'.format(
                tag=catalog_tag
            )
        )
    )
    return keyboard
