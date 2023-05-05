import telebot as t
bot=t.TeleBot("6145885447:AAH7xogWd7qbvkNNuwmLxU9ePdvtYPA5XNU")
@bot.message_handler(commands=['start'])
def start(message): 	
      bot.reply_to(message, """
      راهنمای بات:
      	
      	ثبت نام در دوره => register/
      	
      	سایت ما => khashayaar.ir/wp
      	
      	دوره ها => courses/
      """)
@bot.message_handler(commands=['courses'])
def courses(message): 	
      bot.reply_to(message,""" 
      دوره های موجود:
      	
      	> کلاس آنلاین وردپرس
      	
      	> کلاس آنلاین آموزش php
     
     """)
     
@bot.message_handler(commands=['register'])
def register(message): 	
      bot.reply_to(message, """ 
      فرم زیر را تکمیل کنید :
      		
      		نام :
      		
      		ایمیل :
      			
      			دوره :
      """)     
bot.infinity_polling()
