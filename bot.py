import config
import telebot
import vk as vk_api
from functools import reduce

session = vk_api.Session(access_token=config.vk_token)
vk = vk_api.API(session)

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["anekdot"])
def get_top10_anekdots(message):
	responce = vk.wall.get(domain='baneks')
	aneks = handleVkResponce(responce)
	top10 = list(map(lambda anek: anek['text'], findTop(10, aneks)))
	send_anek(message.chat.id, top10)

def send_anek(chat_id, aneks):
	text_array = []
	for i, anek in enumerate(aneks):
		meta_text = f'\n\n------№{i + 1}---------\n'
		full_text = meta_text + anek.replace('<br>', '\n')
		text_array.append(full_text)
	bot.send_message(chat_id, ''.join(text_array))

def handleVkResponce(responce):
	mapped = map(lambda anek: {
		'text': anek['text'],
		'likes': anek['likes']['count'], 
		'reposts': anek['reposts']['count']}, responce[1:])
	return filter(lambda anek: anek['text'].strip(), mapped)

factor_of_repost = 1.2
factor_of_like = 1.0

def findTop(count, aneks):
	rated = map(lambda anek: {
		'text': anek['text'], 
		'rate': anek['likes'] * factor_of_like + anek['reposts'] * factor_of_repost}, aneks)
	return sorted(rated, key=lambda anek: anek['rate'], reverse=True)[:count]

if __name__ == '__main__':
    bot.polling(none_stop=True)
