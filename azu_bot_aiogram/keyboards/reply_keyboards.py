# from datetime import datetime, timedelta, timezone
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_kbd():
    """Клавиатура запуска бота."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Начать')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(
        resize_keyboard=True
    )


def back_kbd():
    """Клавиатура возвращения назад."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Назад')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(
        resize_keyboard=True
    )


def cafe_select_kbd():
    """Клавиатура выбора кафе."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='ул. Чистопольская, 2')
    keyboard_builder.button(text='ул. Петербургская, 52')
    keyboard_builder.button(text='ул. Павлюхина, 91')
    keyboard_builder.button(text='ул. Петербургская, 14')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Выберите адрес кафе.'
    )


def main_cafe_kbd():
    """Основная клавиатура навигации по кафе."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Посмотреть меню')
    keyboard_builder.button(text='Забронировать стол')
    keyboard_builder.button(text='Как добраться')
    keyboard_builder.button(text='Контакты и режим работы')
    keyboard_builder.button(text='Вернуться к выбору кафе')
    keyboard_builder.adjust(2, 2, 1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Чем я могу помочь?'
    )


def table_or_back_kbd():
    """Перейти к бронированию стола или вернуться назад."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Забронировать стол')
    keyboard_builder.button(text='Назад')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Забронировать стол?'
    )


def reserve_or_back_kbd():
    """Выбрать дату бронирования стола или вернуться назад."""
#    offset = timezone(timedelta(hours=3))
#    day_after_tommorow = datetime.now(offset) + timedelta(days=2)
#    day_after_tommorow = day_after_tommorow.strftime('%d.%m.')
#    after_day_after_tommorow = datetime.now(offset) + timedelta(days=3)
#    after_day_after_tommorow = after_day_after_tommorow.strftime('%d.%m.')

    keyboard_builder = ReplyKeyboardBuilder()
#    keyboard_builder.button(text='Сегодня')
#    keyboard_builder.button(text='Завтра')
#    keyboard_builder.button(text=f'{day_after_tommorow}')
#    keyboard_builder.button(text=f'{after_day_after_tommorow}')
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Введите дату в формате ДД.ММ'
    )


def people_per_table_kbd():
    """Выбрать количество персон или вернуться назад."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='1')
    keyboard_builder.button(text='2')
    keyboard_builder.button(text='3')
    keyboard_builder.button(text='4')
    keyboard_builder.button(text='5')
    keyboard_builder.button(text='6')
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(3, 3, 2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Сколько персон будет за столом?'
    )


def move_tables_or_change_cafe_kbd():
    """Сдвигать столы или сменить кафе."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Выбрать другое кафе')
    keyboard_builder.button(text='Сдвигать столы')
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Нет подхоящего стола. Как поступим?'
    )


def choose_another_cafe_kbd():
    """Выбрать другое кафе, если в текущем нет столов."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Чистопольская, 2')
    keyboard_builder.button(text='Петербургская, 52')
    keyboard_builder.button(text='Павлюхина, 91')
    keyboard_builder.button(text='Петербургская, 14')
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Выберите адрес кафе.'
    )


def enter_name_kbd():
    """Отправить имя или вернуться назад."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='На моё имя')
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='На чьё имя бронируем стол?'
    )


def enter_phone_kbd():
    """Отправить номер телефона или вернуться назад."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(
        text='Отправить мой номер телефона', request_contact=True
    )
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Введите номер телефона.'
    )


def go_to_pay_or_choose_food_kbd():
    """Продолжить выбор еды или перейти к оплате."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Продолжить выбор')
    keyboard_builder.button(text='Оплатить')
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(1, 1, 2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Продолжить выбор или оплатить?'
    )


def check_order_kbd():
    """Проверить заказ и перейти к оплате."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Перейти к оплате')
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Проверьте Ваш заказ.'
    )


def choose_pay_type_kbd():
    """Выбрать способ оплаты."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Оплатить через ЮКасса')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Выберите способ оплаты.'
    )


def no_free_tables_kbd():
    """Появляется в случае отсутствия свободных столов в кафе."""
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Выбрать другое кафе')
    keyboard_builder.button(text='Сдвигать столы')
    keyboard_builder.button(text='Назад')
    keyboard_builder.button(text='Отмена')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Как поступим?'
    )


#  !!!Оставил на всякий случай (сделано по старой версии юзер флоу)!!!
# def go_next_or_menu_kbd():
#    """Знает ли пользователь, что будет заказывать или перейдёт в меню."""
#    keyboard_builder = ReplyKeyboardBuilder()
#    keyboard_builder.button(text='Да')
#    keyboard_builder.button(text='Посмотреть меню')
#    keyboard_builder.button(text='Назад')
#    keyboard_builder.button(text='Отмена')
#    keyboard_builder.adjust(1, 1, 2)
#    return keyboard_builder.as_markup(
#        resize_keyboard=True,
#        one_time_keyboard=True,
#        input_field_placeholder='Вы знаете, что хотите заказать?'
#    )


#  !!!Оставил на всякий случай (сделано по старой версии юзер флоу)!!!
# def choose_food_kbd():
#    """Показать сеты или вернуться назад."""
#    keyboard_builder = ReplyKeyboardBuilder()
#    keyboard_builder.button(text='Сет № 1')
#    keyboard_builder.button(text='Сет № 2')
#    keyboard_builder.button(text='Сет № 3')
#    keyboard_builder.button(text='Сет № 4')
#    keyboard_builder.button(text='Сет № 5')
#    keyboard_builder.button(text='Сет № 6')
#    keyboard_builder.button(text='Сет № 7')
#    keyboard_builder.button(text='Сет № 8')
#    keyboard_builder.button(text='Сет № 9')
#    keyboard_builder.button(text='Назад')
#    keyboard_builder.button(text='Отмена')
#    keyboard_builder.adjust(3, 3, 3, 2)
#    return keyboard_builder.as_markup(
#        resize_keyboard=True,
#        one_time_keyboard=True,
#        input_field_placeholder='Выберите сет для ифтара.'
#    )


#  !!!Оставил на всякий случай (сделано по старой версии юзер флоу)!!!
# def choose_amount_of_food_kbd():
#    """Выбрать количество порций."""
#    keyboard_builder = ReplyKeyboardBuilder()
#    keyboard_builder.button(text='1')
#    keyboard_builder.button(text='2')
#    keyboard_builder.button(text='3')
#    keyboard_builder.button(text='4')
#    keyboard_builder.button(text='5')
#    keyboard_builder.button(text='6')
#    keyboard_builder.button(text='Назад')
#    keyboard_builder.button(text='Отмена')
#    keyboard_builder.adjust(3, 3, 2)
#    return keyboard_builder.as_markup(
#        resize_keyboard=True,
#        one_time_keyboard=True,
#        input_field_placeholder='Укажите количество сетов.'
#    )