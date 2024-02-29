from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("7056885961:AAH8EqIPbkzgNmiI0gsBAK1AKaT_7EHmEns")  # Bot toekn
ADMINS = env.list("6279700039")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili

kanal= ["@Dilmurod2001"]
