
# Parce block
PATH_WEBSITE = "https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B5_%D0%BD%D0" \
               "%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%83%D0%BD%D0%BA%D1%82%D1%8B_%D" \
               "0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8"
OPTION_1 = "--headless"
OPTION_2 = "--disable-dev-shm-usage"
OPTION_3 = "--no-sandbox"
OPTION_4 = "--incognito"
NAME_DRIVER = "chromedriver"
TABLE_1 = '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]'
TABLE_BODY_1 = '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/tbody'
TABLE_2 = '/html/body/div[3]/div[3]/div[5]/div[1]/table[2]'
TABLE_BODY_2 = '/html/body/div[3]/div[3]/div[5]/div[1]/table[2]/tbody'
TABLE_TAG_TR = 'tr'
TABLE_TAG_TD = 'td'
TABLE_TAG_A = 'a'
ATTRIBUTE_HREF = 'href'
DATA_BASE = 'city_&_region.db'
COMMAND_SAVE = 'INSERT INTO cities VALUES'


# Bot block
COMMAND_START = 'start'
TYPE_CONTENT = 'text'
START_TEXT = "Здравствуйте.\n\n" \
             "Начался парсинг, в течение 1-ой минуты\n" \
             "вас оповесит бот, когда он закончится."

STOP_PARCE_TEXT = "Парсинг закончился.\n\n" \
                  "Можете вводить данные. " \
                  "Бот чувствителен к регистру. " \
                  "Пишите город или регион с большой буквы, " \
                  " например 'Балашиха' "

BUTTON_CITY = 'Город'
BUTTON_REGION = 'Регион'

BUTTON_RESTART = 'Обновить данные'
TEXT_RESTART_2 = 'Данные обновлены. Введите город или регион, соблюдайте регистр, ' \
                 'например "Балашиха" '

COMMAND_CITY = 'SELECT city FROM cities'
COMMAND_CITY_HREF = 'SELECT city_href FROM cities'
COMMAND_REGION = 'SELECT region FROM cities'
COMMAND_POPULATION = 'SELECT population FROM cities'
COMMAND_DELETE = 'DELETE FROM cities;'

TWINS_TEXT = 'C такими названием есть и Город и Регион\n\n' \
             'Выберете нужное:'

TEXT_HREF = 'Ссылка: '
TEXT_POPULATION = 'Население: '
TEXT_REGION = 'В этом регионе, такие города: '
NEXT_TEXT = 'Введите еще или можете обновить данные'
TEXT_RESTART_1 = "Данные начали обновляться, бот оповесит через 1 минуту об окончании."
