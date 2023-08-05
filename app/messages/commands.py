from app.messages.environment import environment

HELP = """
Задати питання та знайти інформацію можна тут
"""

START = """
Привіт! Я бот електронної черги на ФІОТ. 
Через мене можна зареєструватись у чергу на подання документів 😊
"""

LAST_NAME = """
Будь ласка, введіть своє прізвище (наприклад: Фітільов)
"""

FIRST_NAME = """
Введіть своє ім'я (наприклад: Микола)
"""

SURNAME = """
Введіть своє по батькові (наприклад: Григорович) або відправте "-", якщо у вас його немає
"""

SPECIALITY = """
Оберіть спеціальність на яку вступаєте

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

EMAIL = """
Вкажіть вашу електронну пошту (наприклад: john@gmail.com)

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

PHONE = """
Вкажіть ваш номер телефону (наприклад: +380961234567)

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

STUDY_TYPE = """
Вступаєш на бюджет чи контракт?

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

STUDY_FORM = """
Оберіть форму навчання

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

PAYMENT_TYPE = """
Оберіть тип оплати

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

DORM = """
Чи плануєш заселятися в гуртожиток?
<b>Це також означає що ви претендуєте на право поселитися у гуртожиток у майбутньому</b>

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

CONFIRM_EDBO = """
Підтвердив вибір місця навчання в електронному кабінеті вступника(ЄДЕБО)?
Це можна зробити за допомогою КЕП або Дія Підпис, а також прикріпити власноруч підписану заяву(тільки для вступників, які перебувають на території, деокупованій після 1 вересня 2022 року, або за кордоном, і не можуть отримати КЕП на ID-картку)

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

PRINTED_EDBO = """
Чи роздрукував заяву з ЄДЕБО?

Ваші особисті дані будуть використані лише для формування заявки на вступ.
"""

MENU = """
<b>Електронна черга ФІОТ</b>

Для реєстрації у черзі на подання документів, натисніть \"Усі черги\" та оберіть необхідну вам.

Якщо у вас виникнуть якісь запитання чи проблеми, натисніть кнопку \"Допомога\" та напишіть нам про це.

Якщо ви хочете прискорити подання документів, натисніть кнопку <b>Продовжити реєстрацію</b>.
"""

SELECT_QUEUE = """
Оберіть чергу, щоб зареєструватись у ній
"""

MY_QUEUES = """
Оберіть чергу, щоб дізнатись свою позицію у ній чи вийти з неї
"""

SEND_GEOLOCATION = """
Надішліть свою геолокацію, щоб підтвердити, що ви знаходитесь на КПІ, та зареєструватись у черзі.
"""

YOU_NOT_IN_QUEUE = """
Вас більше немає у цій черзі!
"""

LEAVE_QUEUE = """
Щоб вийти з черги, натисніть "Так"
"""

THREAD_INFO = environment.from_string("""
ID чата: {{ chat_id }}
ID гілки: {{ thread_id }}
""")
