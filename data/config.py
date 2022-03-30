# from environs import Env

# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()


# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

# DB_HOST = env.str("DB_HOST")
# DB_USER = env.str("DB_USER")
# DB_PASS = env.str("DB_PASS")
# DB_NAME = env.str("DB_NAME")


import os

BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))
ADMINS = ['155460463',"1672039210"] # adminlar ro'yxati
IP = str(os.environ.get('ip'))

DB_USER = str(os.environ.get("DB_USER"))
DB_PASS = str(os.environ.get("DB_PASS"))
DB_NAME = str(os.environ.get("DB_NAME"))
DB_HOST = str(os.environ.get("DB_HOST"))

