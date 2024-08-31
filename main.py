# pip install -r req.txt
from telebot.types import BotCommand
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytube import YouTube
from rembg import remove
from PIL import Image
from gtts import gTTS
from googletrans import Translator
from datetime import datetime
from googlesearch import search
import speedtest
import moviepy.editor
import telebot
import os
import math
TOKEN = "7113724596:AAE4yYczuklB_raJ2pi4vObn7BzCUpO9YwE"
bot = telebot.TeleBot(TOKEN)
print('-'*50)
print("SAZOM v1.4")
print('-')
#-----------------------------------------------------------folders
bot.set_my_commands([BotCommand("start","لإعادة تشغيل البوت")])
DOWNLOADS = "./downloads/"
if os.path.exists(DOWNLOADS):
    print("alredy - [downloads]")
    pass
else:
    os.makedirs("downloads")
    print("creat folder - [downloads]")
TEMP = "./temp/"
if os.path.exists(TEMP):
    print("alredy - [temp]")
    pass
else:
    os.makedirs("temp")
    print("creat folder - [temp]")
PROCESSED = "./processed/"
if os.path.exists(PROCESSED):
    print("alredy - [processed]")
    pass
else:
    os.makedirs("processed")
    print("creat folder - [processed]")
SPEECH = "./speech/"
if os.path.exists(SPEECH):
    print("alredy - [processed]")
    pass
else:
    os.makedirs("speech")
    print("creat folder - [speech]")
CONVERT = "./convert/"
if os.path.exists(CONVERT):
    print("alredy - [convert]")
    pass
else:
    os.makedirs("convert")
    print("creat folder - [convert]")
LOCATION = "./location/"
if os.path.exists(LOCATION):
    print("alredy - [location]")
    pass
else:
    os.makedirs("location")
    print("creat folder - [location]")
STICKER = "./sticker/"
if os.path.exists(STICKER):
    print("alredy - [sticker]")
    pass
else:
    os.makedirs("sticker")
    print("creat folder - [sticker]")
TRANSLATE = "./translate/"
if os.path.exists(TRANSLATE):
    print("alredy - [translate]")
    pass
else:
    os.makedirs("translate")
    print("creat folder - [translate]")
SEARCH = "./search/"
if os.path.exists(SEARCH):
    print("alredy - [search]")
    pass
else:
    os.makedirs("search")
    print("creat folder - [search]")
#---------------------------------------------------------------
try:
    ADMIN_ID = 6020331913
    def check_user_id(user_id):
        with open("users.txt", "r") as file:
            users = file.readlines()
        if f"{user_id}\n" in users:
            return True
        return False

    def register_user(user_id):
        if not check_user_id(user_id):
            with open("users.txt", "a") as file:
                file.write(f"{user_id}\n")
    @bot.message_handler(commands=["start"])
    def start(message):
        user_id = message.from_user.id
        register_user(user_id)
        if user_id == ADMIN_ID:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("إرسال رسالة لجميع المستخدمين", callback_data="send_to_all"))
            markup.add(InlineKeyboardButton("إلغاء",callback_data="cancell"))
            bot.send_message(message.chat.id, "مرحبا بك، لقد تم التعرف عليك كمدير. يمكنك استخدام الأزرار أدناه.", reply_markup=markup)
        else:
            bot.send_message(message.chat.id,f"""SAZOM Company
        ____________________________
        مرحبا ({message.from_user.first_name})
        هذا هو بوت شركة SAZOM الرسمي هناك الكثير من الخدمات المجانية والتي ستجدها عن الآخرين بالدفع الإلكتروني.
    حسنا:
    1) ما هي شركة SAZOM ؟
    في الواقع SAZOM هي شركة برمجية ظهرت في الفترة الأخيرة لها الكثير من الخدمات البرمجية التي تتيح للمستخدم سهولة العمل بكافة الخدمات المجانية المتاحة لدى هذه الشركة.
    2) ما الخدمات التي تقدمها الشركة بشكل مختصر؟
    1️⃣ download وهي تعني تنزيل أي فيديو من اليوتيوب حصرا بأعلى دقة ممكنة
    2️⃣ remove وهي تعني حذف خلفية أي صورة بالذكاء الإصطناعي يعني: اذا كانت لديك صورة وورائك خلفية لا تريدها فقط ارسلها للبوت وهو سيقوم بحذف هذه الخلفية لك.
    3️⃣ speech وهي تعني تحويل أي نص تكتبه الى كلام باللغة العربية مع مراعاة التشكيل, مثلا: مازنٌ يمشي في الحديقةِ.
    4️⃣ convert وهي تعني تحويل الفيديو الى موسيقى, أي: أنا لدي فيديو وأريد تحويله الى موسيقى كل ما عليك فعله فقط إرسال هذا الفيديو الى بوت وهو سيقوم بتحويله
    5️⃣ location هي خدمة جديدة وقوية ولكن هي قيد التطوير فكرتها ببساطة أنها تستطيع من خلال الرقم الذي ترسله لها معرفة اسم الدولة مثلا: +963 ستعرف مباشرة أنها لدولة سوريا وتعرف أيضا اسم الشركة الصانعة مثلا: 51****** هذه لشركة MTN ومن خلال هذه المعلومات تأخذ إحداثيات هذا الرقم وعندها ترسل ملف بلاحقة HTML لتعرف مكان صاحب هذا الرقم. ولكن للأسف الشديد هذه الخدمة قيد التطوير وسيتم تشغيلها قريبا
    6️⃣ speed وهي تعني Speed Test Internet يعني قياس سرعة الانترنت لديك.
    7️⃣ sticker وهي تعني تحويل صورة ترسلها للبوت الى ملصق.
    8️⃣ trans وهي تعني ترجمة أي نص إلى اللغة العربية
    9️⃣ search وهي تعني بحث عن أي شيء في محرك البحث جوجل بمجرب ما إن تبحث عن أي شيء سيظهر لك رابط به الشيء الذي بحثت عنه

    ملاحظة:📝 كل هذه الخدمات تحافظ على خصوصية المستخدم بمجرد ما إن تنتهي ال function من العمل تحذف كل الوسائط والرسائل التي حفظت بالبوت من أجل الاستخدام والمعالجة.
    ملاحظة2: 📝 البوت في حالة تطوير دائمة لذلك يتوقف لمدة لا تتجاوز ال 8 ساعات للتطوير ولا تقلق سيتم إعلام المستخدمين بالوقت الذي سيتم إطفاء البوت فيه.
    عموما: أرجو الاستفادة من هذا البوت ونشره لأكبر قدر من المستخدمين على الأقل لأصدقائك ❤️‍🩹💯
    إذا أردت التواصل مع المبرمجين 📨📩:
    Alaa Safi علاء صافي 
    @AlaaSafiProgrammer218 
    +96395144936
    ___________________________________

    Zaid Makhzoom  زيد مخزوم
    @Zaidmakhzoom
    +963 992 883 477""")
    @bot.callback_query_handler(func=lambda call: call.data == "send_to_all")
    def prompt_for_message(call):
        if call.from_user.id == ADMIN_ID:
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = ReplyKeyboardMarkup()
            markup.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(call.message.chat.id, "يرجى كتابة الرسالة التي تريد إرسالها لجميع المستخدمين.",reply_markup=markup)
            bot.register_next_step_handler(call.message, broadcast_message)
        else:
            bot.send_message(call.message.chat.id, "عذرا، لا يمكنك استخدام هذا الزر.")
    @bot.callback_query_handler(func=lambda call: call.data == "cancell")
    def cancel_admin(call):
        if  call.from_user.id == ADMIN_ID:
            bot.delete_message(call.message.chat.id,call.message.message_id)
            bot.send_message(call.message.chat.id,"تمت إلغاء العملية بنجاح.")
            home(call.message)
        else:
            bot.send_message(call.message.chat.id, "عذرا، لا يمكنك استخدام هذا الزر.")
    def broadcast_message(message):
        if message.text == 'إلغاء ❌':
            bot.send_message(message.chat.id,"تمت إلغاء العملية بنجاح.")
            home(message)
        elif message.from_user.id == ADMIN_ID:
            with open("users.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    bot.send_message(user.strip(), message.text)
            bot.send_message(message.chat.id, "تم إرسال الرسالة لجميع المستخدمين.")
        else:
            bot.send_message(message.chat.id, "عذرا، لا يمكنك إرسال الرسالة.")
    #---------------------------------------------------buttons
        markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        markup.add(KeyboardButton("تنزيل فيديوهات 📥"))
        markup.add(KeyboardButton("حذف الخلفية 📷"))
        markup.add(KeyboardButton("تحويل النص إلى كلام 🔀"))
        markup.add(KeyboardButton("تحويل أي فيدو إلى موسيقى 🔁"))
        markup.add(KeyboardButton("معرفة الموقع من الرقم 📲"))
        markup.add(KeyboardButton("معرفة سرعة الإنترنت 🌐"))
        markup.add(KeyboardButton("تحويل الصورة إلى ملصق 🖼"))
        markup.add(KeyboardButton("ترجمة النصوص من أي لغة إلى العربية 🔠"))
        markup.add(KeyboardButton("البحث عن اي يخطر في بالك في غوغل 🔍"))
        b1 = KeyboardButton("التواصل مع الدعم 📞")
        b2 = KeyboardButton("كيفية الاستخدام 📝")
        markup.row(b1,b2)
        bot.send_message(message.chat.id,"الرجاء إختيار طلبك من القائمة:",reply_markup=markup)
    def home(message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        markup.add(KeyboardButton("تنزيل فيديوهات 📥"))
        markup.add(KeyboardButton("حذف الخلفية 📷"))
        markup.add(KeyboardButton("تحويل النص إلى كلام 🔀"))
        markup.add(KeyboardButton("تحويل أي فيدو إلى موسيقى 🔁"))
        markup.add(KeyboardButton("معرفة الموقع من الرقم 📲"))
        markup.add(KeyboardButton("معرفة سرعة الإنترنت 🌐"))
        markup.add(KeyboardButton("تحويل الصورة إلى ملصق 🖼"))
        markup.add(KeyboardButton("ترجمة النصوص من أي لغة إلى العربية 🔠"))
        markup.add(KeyboardButton("البحث عن اي يخطر في بالك في غوغل 🔍"))
        b1 = KeyboardButton("التواصل مع الدعم 📞")
        b2 = KeyboardButton("كيفية الاستخدام 📝")
        markup.row(b1,b2)
        bot.send_message(message.chat.id,"الرجاء إختيار طلبك من القائمة:",reply_markup=markup)
    #---------------------------- show download
    def show_download(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تنزيل من اليوتيوب",callback_data="youtube"))
        bot.send_message(message.chat.id,"الجاء الإختيار من القائمة:",reply_markup=markup)
    #-------------------------------- show remove
    def show_remove(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("باستخدام AI", callback_data="remove"))
        bot.send_message(message.chat.id,"هل تريد حذف خلفية الصورة باستخدام:",reply_markup=markup)
    #--------------------------------------- show gtts
    def show_gtts(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("باستخدام غوغل.",callback_data="gtts"))
        bot.send_message(message.chat.id,"تحويل النص إلى كلام باستخدام:",reply_markup=markup)
    #-------------------------------------- show convert
    def show_convert(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تحويل عادي",callback_data="convert"))
        bot.send_message(message.chat.id,"نوع التحويل:",reply_markup=markup)        
    #-------------------------------------- show convimg
    def show_convimg(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تحويل عادي",callback_data="convimg"))
        bot.send_message(message.chat.id,"نوع تحويل الصورة:",reply_markup=markup)
    #------------------------------------------- show translate
    def show_trans(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("العربية",callback_data="arabic"))
        bot.send_message(message.chat.id,"ترجمة النص من أي لغة إلى:",reply_markup=markup)
    #--------------------------------------------- show google
    def show_google(message):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("غوغل",callback_data="google"))
        bot.send_message(message.chat.id,"البحث في:",reply_markup=markup)
    #---------------------- keyboard buttons
    @bot.message_handler(func=lambda message: True)
    def respond_buttons_keyboard(message):
        if message.text == 'إلغاء ❌':
            home(message)
        elif message.text == 'تنزيل فيديوهات 📥':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_download(message)
        elif message.text == 'حذف الخلفية 📷':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_remove(message)
        elif message.text == 'تحويل النص إلى كلام 🔀':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))    
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_gtts(message)
        elif message.text == 'تحويل أي فيدو إلى موسيقى 🔁':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_convert(message)
        elif message.text == 'معرفة الموقع من الرقم 📲':
            bot.send_message(message.chat.id,"""عذرا 🙁
هذه الخدمة متوقفة حاليا وقيد التطوير 💔
سيتم توفر هذه الخدمة قريبا 🔜""")
        elif message.text == 'معرفة سرعة الإنترنت 🌐':
            bot.send_message(message.chat.id,"""عذرا 🙁
هذه الخدمة متوقفة حاليا وقيد التطوير 💔
سيتم توفر هذه الخدمة قريبا 🔜""")
        elif message.text == 'تحويل الصورة إلى ملصق 🖼':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_convimg(message)
        elif message.text == 'ترجمة النصوص من أي لغة إلى العربية 🔠':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_trans(message)
        elif message.text == 'البحث عن اي يخطر في بالك في غوغل 🔍':
            mark = ReplyKeyboardMarkup()
            mark.add(KeyboardButton("إلغاء ❌"))
            bot.send_message(message.chat.id,"جاري التحميل...",reply_markup=mark)
            show_google(message)
        elif message.text == 'التواصل مع الدعم 📞':
            bot.send_message(message.chat.id,"""للتواصل معنا 📞:
علاء صافي
Alaa Safi
00963951449364
alaasafi218k15@gmail.com
@AlaaSafiProgrammer218 
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
زيد مخزوم
Zaid Makhzoom
00963992883477
zaidmakzoom@gmail.com
@Zaidmakhzoom""")
        elif message.text == 'كيفية الاستخدام 📝':
            start(message)
        else:
            bot.send_message(message.chat.id,"عذرا, يرجى الإختيار من القائمة فقط.")
    @bot.callback_query_handler(func=lambda call: True)
    def callback_data(call):
        if call.data == 'youtube':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defdown = bot.send_message(call.message.chat.id,"تمام, يرجى إرسال رابط الفيديو.")
            bot.register_next_step_handler(defdown,download_sazom)
        elif call.data == 'remove':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defrembg = bot.send_message(call.message.chat.id,"يرجى ارسال الصورة.")
            bot.register_next_step_handler(defrembg,remove_sazom)
        elif call.data == 'gtts':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defgtts = bot.send_message(call.message.chat.id,"يرجى كتابة النص المراد تحويله إلى كلام.")
            bot.register_next_step_handler(defgtts,gtts_sazom)
        elif call.data == 'convert':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defconvert = bot.send_message(call.message.chat.id,"يرجى إرسال الفيديو.")
            bot.register_next_step_handler(defconvert,convert_sazom)
        elif call.data == 'convimg':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defconvimg = bot.send_message(call.message.chat.id,"يرجى إرسال الصورة.")
            bot.register_next_step_handler(defconvimg,convimg_sazom)
        elif call.data == 'arabic':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defarabic = bot.send_message(call.message.chat.id,"يرجى ارسال النص")
            bot.register_next_step_handler(defarabic,arabic_sazom)
        elif call.data == 'google':
            bot.delete_message(call.message.chat.id,call.message.message_id)
            defgoogle = bot.send_message(call.message.chat.id,"يرجى كتابة البحث الذي تريده.")
            bot.register_next_step_handler(defgoogle,google_sazom)
        else:
            bot.send_message(call.message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
    def google_sazom(message):
        user_id = message.from_user.id
        query = message.text
        try:
            with open(f"./search/{user_id}.txt", "a", encoding="utf-8") as file:
                file.write(f"{query}\n")
            results = []
            for result in search(query, num_results=5):
                results.append(result)
            bot.send_message(message.chat.id, "إليك أفضل 5 نتائج:")
            if results:
                for result in results:
                    bot.send_message(message.chat.id, result)
            else:
                bot.send_message(message.chat.id, "لم أتمكن من العثور على أي نتائج.")  
            os.remove(f"./search/{user_id}.txt")
            home(message)
        except Exception as e:
            print(f"Error on [SEARCH] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
    def arabic_sazom(message):
        try:
            chat_id=message.chat.id
            user_id = message.from_user.id
            translator = Translator()
            with open(f"./translate/{user_id}.txt",'w',encoding="utf-8") as file:
                file.write(message.text)
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة النص الذي ارسلته, الرجاء الإنتظار...")
            with open(f"./translate/{user_id}.txt","r",encoding="utf-8") as file:
                SAZOM_file = file.read()
            SAZOM_ar = translator.translate(text=SAZOM_file,src="auto",dest="ar").text
            with open(f"./translate/{user_id}_SAZOM.txt","w", encoding="utf-8") as file:
                file.write(SAZOM_ar)
            text = open(f"./translate/{user_id}_SAZOM.txt","rb")
            bot.send_message(chat_id=chat_id,text=text,parse_mode="Markdown")
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            text.close()
            os.remove(f"./translate/{user_id}_SAZOM.txt")
            os.remove(f"./translate/{user_id}.txt")
            home(message)
        except Exception as e:
            print(f"Error on [Trans ARABIC] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
    def convert_to_sticker(image_path,message):
        try:
            user_id = message.from_user.id
            input_image = Image.open(image_path)
            sticker_size = (512, 512)
            input_image.thumbnail(sticker_size)
            if input_image.size[0] != sticker_size[0] or input_image.size[1] != sticker_size[1]:
                background = Image.new('RGBA', sticker_size, (255, 255, 255, 0))
                background.paste(input_image, ((sticker_size[0] - input_image.size[0]) // 2, (sticker_size[1] - input_image.size[1]) // 2))
                input_image = background
            sticker_path = f'./sticker/{user_id}.webp'
            input_image.save(sticker_path)
            return sticker_path
        except Exception as e:
            print(f"Error on [STICKER] ({e})")
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
    def convimg_sazom(message):
        try:
            user_id = message.from_user.id
            file_id = message.photo[-1].file_id
            chat_id=message.chat.id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الصورة التي ارسلتها , الرجاء الإنتظار...")
            with open(f'./sticker/{user_id}.jpg', 'wb') as new_file:
                new_file.write(downloaded_file)
            sticker_path = convert_to_sticker(f'./sticker/{user_id}.jpg')
            if sticker_path:
                sticker_file = open(sticker_path, 'rb')
                bot.send_sticker(message.chat.id, sticker_file)
                bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
                sticker_file.close()
                os.remove(f"./sticker/{user_id}.jpg")
                os.remove(f"./sticker/{user_id}.webp")
                home(message)
            else:
            
                print(f"Error on [CONVIMG] ({e})")
                bot.send_message(chat_id,"""للاسف ☹️
    حدث خطأ ما ❌
    الرجاء المحاولة لاحقا 🔄""")
        except Exception as e:
            print(f"Error on [CONVIMG] ({e})")
            bot.send_message(chat_id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
        
    def convert_sazom(message):
        try:
            user_id = message.from_user.id
            chat_id=message.chat.id
            video = message.video
            file_id = video.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            save_path = f"convert/{user_id}.mp4"
            downloaded_file = bot.download_file(file_path)
            with open(save_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الفيديوالذي ارسلته. الرجاء الإنتظار...")
            input= f"./convert/{user_id}.mp4"
            mp4 = moviepy.editor.VideoFileClip(input)
            mp3 = mp4.audio
            mp3.write_audiofile(f"./convert/{user_id}.mp3")
            mediaconvert=open(f"./convert/{user_id}.mp3",'rb')
            bot.send_audio(chat_id=chat_id,audio=mediaconvert)
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            mediaconvert.close()
            mp4.close()
            os.remove(f"./convert/{user_id}.mp3")
            os.remove(f"./convert/{user_id}.mp4")
            home(message)
        except Exception as e:
            print(f"Error on [CONVERT] ({e})")
            bot.send_message(chat_id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
    def gtts_sazom(message):
        try:
            chat_id = message.chat.id
            user_id = message.from_user.id
            text = message.text
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة النص الذي كتبته. الرجاء الإنتظار...")
            tts = gTTS(text=text, lang='ar', slow=False)
            tts.save(f"./speech/{user_id}.mp3")
            mediaspeech = open(f"./speech/{user_id}.mp3","rb")
            bot.send_audio(chat_id=chat_id,audio=mediaspeech)
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            mediaspeech.close()
            os.remove(f"./speech/{user_id}.mp3")
            home(message)
        except Exception as e:
            print(f"Error on [GTTS] ({e})")
            bot.send_message(chat_id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
    def remove_sazom(message):
        try:
            chat_id = message.chat.id
            user_id = message.from_user.id
            photo = message.photo[-1]
            file_id = photo.file_id
            bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الصورة. الرجاء الإنتظار...")
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            save_path = f"temp/{user_id}.jpg"
            downloaded_file = bot.download_file(file_path)
            with open(save_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            input_path = f"./temp/{user_id}.jpg"
            output_path = f"./processed/{user_id}.png"
            input = Image.open(input_path)
            output = remove(input)
            output.save(output_path)
            os.remove(f"./temp/{user_id}.jpg")
            mediarembg = open(f"./processed/{user_id}.png",'rb')
            bot.send_photo(chat_id=chat_id,photo=mediarembg)
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            mediarembg.close()
            os.remove(f"./processed/{user_id}.png")
            home(message)
        except Exception as e:
            print(f"Error on [REMOVE] ({e})")
            bot.send_message(chat_id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
    def download_sazom(message):
        try:
            url = message.text
            yt = YouTube(url)
            bot.send_message(message.chat.id,text=f"نحن نقوم بتنزيل الفيديو الخاص بك ('{yt.title}')(720p) الرجاء الإتظار...")
            video = yt.streams.get_highest_resolution()
            filename = f"./downloads/{message.from_user.id}.mp4"
            video.download(filename=filename)
            mediadownload = open(f"./downloads/{message.from_user.id}.mp4",'rb')
            bot.send_video(message.chat.id,video=mediadownload)
            bot.send_message(message.chat.id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            mediadownload.close()
            os.remove(f"./downloads/{message.from_user.id}.mp4")
            home(message)
        except:
            bot.send_message(message.chat.id,"""للاسف ☹️
حدث خطأ ما ❌
الرجاء المحاولة لاحقا 🔄""")
except:
    print("ERROR*2")         
print("The bot is running!!!!")
bot.infinity_polling()      
