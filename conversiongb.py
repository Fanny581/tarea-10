import telebot # importamos la libreria de telebot

# token = os.getenv['TOKEN']
bot = telebot.TeleBot('1943118611:AAEBrEMgR5-qyObtX1X8COfUNyesV0k08SU') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['info','hola']) #definimos el comando
def hola(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id,  "Envia  GB para ver formula Gigabytes a Megabytes \n Envia TB para ver formula Terabytes a Gigabytes \n Envia MB para ver formula Megabytes a Kilobytes \n Envia  b para ver formula Bytes a bits \n ")
    print("Mandaron info")

@bot.message_handler(commands=['gb','GB']) 
def GB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "multiplica el valor de tamaño de datos por 1024")
    print("Mandaron gb ,GB")

@bot.message_handler(commands=['tb','TB'])
def TB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "multiplica el valor de tamaño de datos por 1024")
    print("Mandaron tb, TB")

@bot.message_handler(commands=['mb','MB'])
def MB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "multiplica el valor de tamaño de datos por 1024")
    print("Mandaron ,mb ,MB")

@bot.message_handler(commands=['b','b'])
def b(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "multiplica el valor de tamaño de datos por 8")
    print("Mandaron b")

bot.polling()