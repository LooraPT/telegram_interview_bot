from src.database import all_user_id, restart_one_users_Full_name, delete_results, restart_db, add_question_seven, add_question_eight, add_question_nine, add_question_ten, add_question_three, add_question_four, add_question_five, add_question_six, add_question_two, add_question_one, add_user_and_course, get_state, get_full_name, check_user_id, add_full_name_in_first_table, add_length, get_length, minus_one_length_and_plus_state
from src import dataframe
from resources import config
import logging
from telegram import *
from telegram.ext import *
from telegram.ext.dispatcher import run_async

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

StudentAndDiscipline = dataframe.list_Student() #in this list saves name students and his lessons in format [(Name, lesson), ... , (name1399, lesson1399)]
allpeople = dataframe.set_people() #all student list

QUESTIONONE, QUESTIONTWO = range(2)

buttons = [  [InlineKeyboardButton("1️⃣", callback_data = 'odin')  , InlineKeyboardButton('2️⃣', callback_data = "dva"),
                     InlineKeyboardButton('3️⃣', callback_data = "tri"), InlineKeyboardButton('4️⃣', callback_data = "chetiry"),
                     InlineKeyboardButton('5️⃣', callback_data = "pyat")], [InlineKeyboardButton('6️⃣', callback_data = "sheshch"),
                     InlineKeyboardButton('7️⃣', callback_data = "shedem"), InlineKeyboardButton('8️⃣', callback_data = "osiem"),
                     InlineKeyboardButton('9️⃣', callback_data = "devyat"), InlineKeyboardButton('🔟', callback_data = "desyat")] ]

buttons2 = [  [InlineKeyboardButton("1️⃣", callback_data = '1')  , InlineKeyboardButton('2️⃣', callback_data = "2"),
                     InlineKeyboardButton('3️⃣', callback_data = "3"), InlineKeyboardButton('4️⃣', callback_data = "4"),
                     InlineKeyboardButton('5️⃣', callback_data = "5")], [InlineKeyboardButton('6️⃣', callback_data = "6"),
                     InlineKeyboardButton('7️⃣', callback_data = "7"), InlineKeyboardButton('8️⃣', callback_data = "8"),
                     InlineKeyboardButton('9️⃣', callback_data = "9"), InlineKeyboardButton('🔟', callback_data = "10")] ]

buttons3 = [  [InlineKeyboardButton("1️⃣", callback_data = '11')  , InlineKeyboardButton('2️⃣', callback_data = "12"),
                     InlineKeyboardButton('3️⃣', callback_data = "13"), InlineKeyboardButton('4️⃣', callback_data = "14"),
                     InlineKeyboardButton('5️⃣', callback_data = "15")], [InlineKeyboardButton('6️⃣', callback_data = "16"),
                     InlineKeyboardButton('7️⃣', callback_data = "17"), InlineKeyboardButton('8️⃣', callback_data = "18"),
                     InlineKeyboardButton('9️⃣', callback_data = "19"), InlineKeyboardButton('🔟', callback_data = "20")] ]

buttons4 = [  [InlineKeyboardButton("1️⃣", callback_data = '21')  , InlineKeyboardButton('2️⃣', callback_data = "22"),
                     InlineKeyboardButton('3️⃣', callback_data = "23"), InlineKeyboardButton('4️⃣', callback_data = "24"),
                     InlineKeyboardButton('5️⃣', callback_data = "25")], [InlineKeyboardButton('6️⃣', callback_data = "26"),
                     InlineKeyboardButton('7️⃣', callback_data = "27"), InlineKeyboardButton('8️⃣', callback_data = "28"),
                     InlineKeyboardButton('9️⃣', callback_data = "29"), InlineKeyboardButton('🔟', callback_data = "30")] ]

buttons5 = [  [InlineKeyboardButton("1️⃣", callback_data = '31')  , InlineKeyboardButton('2️⃣', callback_data = "32"),
                     InlineKeyboardButton('3️⃣', callback_data = "33"), InlineKeyboardButton('4️⃣', callback_data = "34"),
                     InlineKeyboardButton('5️⃣', callback_data = "35")], [InlineKeyboardButton('6️⃣', callback_data = "36"),
                     InlineKeyboardButton('7️⃣', callback_data = "37"), InlineKeyboardButton('8️⃣', callback_data = "38"),
                     InlineKeyboardButton('9️⃣', callback_data = "39"), InlineKeyboardButton('🔟', callback_data = "40")] ]

buttons6 = [  [InlineKeyboardButton("1️⃣", callback_data = '41')  , InlineKeyboardButton('2️⃣', callback_data = "42"),
                     InlineKeyboardButton('3️⃣', callback_data = "43"), InlineKeyboardButton('4️⃣', callback_data = "44"),
                     InlineKeyboardButton('5️⃣', callback_data = "45")], [InlineKeyboardButton('6️⃣', callback_data = "46"),
                     InlineKeyboardButton('7️⃣', callback_data = "47"), InlineKeyboardButton('8️⃣', callback_data = "48"),
                     InlineKeyboardButton('9️⃣', callback_data = "49"), InlineKeyboardButton('🔟', callback_data = "50")] ]

buttons7 = [  [InlineKeyboardButton("1️⃣", callback_data = '51')  , InlineKeyboardButton('2️⃣', callback_data = "52"),
                     InlineKeyboardButton('3️⃣', callback_data = "53"), InlineKeyboardButton('4️⃣', callback_data = "54"),
                     InlineKeyboardButton('5️⃣', callback_data = "55")], [InlineKeyboardButton('6️⃣', callback_data = "56"),
                     InlineKeyboardButton('7️⃣', callback_data = "57"), InlineKeyboardButton('8️⃣', callback_data = "58"),
                     InlineKeyboardButton('9️⃣', callback_data = "59"), InlineKeyboardButton('🔟', callback_data = "60")] ]

buttons8 = [  [InlineKeyboardButton("1️⃣", callback_data = '61')  , InlineKeyboardButton('2️⃣', callback_data = "62"),
                     InlineKeyboardButton('3️⃣', callback_data = "63"), InlineKeyboardButton('4️⃣', callback_data = "64"),
                     InlineKeyboardButton('5️⃣', callback_data = "65")], [InlineKeyboardButton('6️⃣', callback_data = "66"),
                     InlineKeyboardButton('7️⃣', callback_data = "67"), InlineKeyboardButton('8️⃣', callback_data = "68"),
                     InlineKeyboardButton('9️⃣', callback_data = "69"), InlineKeyboardButton('🔟', callback_data = "70")] ]


def startCommand(update: Update, context: CallbackContext):
    if check_user_id(update.effective_chat.id, update.effective_chat.username):
         update.message.reply_text('You have already complete interview,you want go through again?')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.starthello)
        update.message.reply_text('Write your Full Name')

def fullname(update: Update, context: CallbackContext):
    nothavedis = [[KeyboardButton("I don't have this is discipline")]]
    msg = update.message.text
    user_id = update.effective_chat.id
    if get_state(user_id) == 0:
        if dataframe.binary_search(allpeople, msg):

            add_full_name_in_first_table(msg, user_id)
            add_length(dataframe.search_length(StudentAndDiscipline, msg), user_id)

            if get_length(user_id) != 0:
                for i in range(len(StudentAndDiscipline)):
                    if msg == StudentAndDiscipline[i][0]:

                        update.message.reply_text(StudentAndDiscipline[i][1], reply_markup=ReplyKeyboardMarkup(nothavedis, resize_keyboard = True))
                        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp1, reply_markup=InlineKeyboardMarkup(buttons))
                        minus_one_length_and_plus_state(user_id)

                        add_user_and_course(user_id, StudentAndDiscipline[i][1])

                        break
            else:
                update.message.reply_text('Error')
        else:
            update.message.reply_text('I not see u')


    if msg in ['Наступна дисципліна', "I don't have this is discipline"]:
        if get_state(user_id) != 0:
            if get_length(user_id) != 0:
                for i in range(len(StudentAndDiscipline)):
                    if get_full_name(user_id) == StudentAndDiscipline[i][0]:

                        add_user_and_course(user_id, StudentAndDiscipline[i + get_state(user_id)][1])

                        update.message.reply_text(StudentAndDiscipline[i + get_state(user_id)][1], reply_markup=ReplyKeyboardMarkup(nothavedis, resize_keyboard = True))
                        update.message.reply_text(config.qfp1, reply_markup=InlineKeyboardMarkup(buttons))
                        minus_one_length_and_plus_state(user_id)
                        break
            else:
                update.message.reply_text('The End')

    if str(user_id) in config.ADMIN:
        keyboard = [[InlineKeyboardButton("нет", callback_data = 'omg'), InlineKeyboardButton("да", callback_data = 'noway')]]
        keyboard1 = [[InlineKeyboardButton("нет", callback_data='omgg'), InlineKeyboardButton("да", callback_data='nowayy')]]
        if msg == 'Delete db(bot)':
            update.message.reply_text('WTF are u sure?', reply_markup=InlineKeyboardMarkup(keyboard))
        if msg == 'Delete results':
            update.message.reply_text('WTF are u sure?', reply_markup=InlineKeyboardMarkup(keyboard1))
        if msg == 'back':
            update.message.reply_text('Okay, but remember i can destroyed this bot', reply_markup=ReplyKeyboardRemove())
        if msg == 'Delete(restart one users)':
            update.message.reply_text('/restartusers *full name users*')
        if 'Spam' == msg:
            update.message.reply_text('Write in format /spam (text)')




def oprosHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    query1 = update.callback_query
    query1.answer()
    query1.edit_message_text(text=f"Дякую ваша відповідь важлива для нас")

    if query == 'omgg':
        context.bot.send_message(chat_id=update.effective_chat.id, text="huh")

    if query == 'nowayy':
        delete_results()
        context.bot.send_message(chat_id=update.effective_chat.id, text='cunt')

    if query == 'noway':
        restart_db()
        context.bot.send_message(chat_id=update.effective_chat.id, text='cunt')

    if query == 'omg':
        context.bot.send_message(chat_id=update.effective_chat.id, text="huh")

    call_back_list = ['odin', 'dva', 'tri', 'chetiry', 'pyat', 'shedem', 'sheshch', 'osiem', 'devyat', 'desyat']
    call_back_list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    call_back_list3 = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    call_back_list4 = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    call_back_list5 = ['31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
    call_back_list6 = ['41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
    call_back_list7 = ['51', '52', '53', '54', '55', '56', '57', '58', '59', '60']
    call_back_list8 = ['61', '62', '63', '64', '65', '66', '67', '68', '69', '70']

    if query in call_back_list:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp2, reply_markup=InlineKeyboardMarkup(buttons2))
        for i in range(len(StudentAndDiscipline)):
            if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
                add_question_one(query, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
                break
    if query in call_back_list2:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp3, reply_markup=InlineKeyboardMarkup(buttons3))
        for i in range(len(StudentAndDiscipline)):
            if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
                add_question_two(query, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
                break
    if query in call_back_list3:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp4, reply_markup=InlineKeyboardMarkup(buttons4))
        for i in range(len(StudentAndDiscipline)):
            if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
                add_question_three(query, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
                break
    if query in call_back_list4:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp5, reply_markup=InlineKeyboardMarkup(buttons5))
        for i in range(len(StudentAndDiscipline)):
            if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
                add_question_four(query, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
                break
    if query in call_back_list5:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp6, reply_markup=InlineKeyboardMarkup(buttons6))
        for i in range(len(StudentAndDiscipline)):
            if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
                add_question_five(query, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
                break
    if query in call_back_list6:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp7, reply_markup=InlineKeyboardMarkup(buttons7))
        for i in range(len(StudentAndDiscipline)):
            if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
                add_question_six(query, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
                break
    if query in call_back_list7:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp8, reply_markup=InlineKeyboardMarkup(buttons8))
        for i in range(len(StudentAndDiscipline)):
            if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
                add_question_seven(query, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
                break
    if query in call_back_list8:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp9)
        for i in range(len(StudentAndDiscipline)):
            if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
                add_question_eight(query, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
                break
        return QUESTIONONE


def questionone(update: Update, context: CallbackContext):
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
            add_question_nine(update.message.text, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
            break
    update.message.reply_text(config.qfp10)
    return QUESTIONTWO

def questiontwo(update: Update, context: CallbackContext):
    nextdis = [[KeyboardButton('Наступна дисципліна')]]
    for i in range(len(StudentAndDiscipline)):
        if get_full_name(update.effective_chat.id) == StudentAndDiscipline[i][0]:
            add_question_ten(update.message.text, update.effective_chat.id, StudentAndDiscipline[i - 1 + get_state(update.effective_chat.id)][1])
            break
    update.message.reply_text('Дякую за пройдену дісципліну, для наступної натисніть кнопку знизу', reply_markup = ReplyKeyboardMarkup(nextdis,resize_keyboard = True))
    return ConversationHandler.END



def adminCommand(update: Update, context: CallbackContext):
    msg = update.message.text
    user_id = update.effective_chat.id
    keybo = [[KeyboardButton('Spam'), KeyboardButton('Delete(restart one users)')],
                [KeyboardButton('Delete db(bot)'), KeyboardButton('Print users')],
             [KeyboardButton('back'), KeyboardButton('Delete results')]]
    if str(user_id) in config.ADMIN:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome ginius', reply_markup = ReplyKeyboardMarkup(keybo,resize_keyboard = True))

def spamCommand(update: Update, context: CallbackContext):
    if str(update.effective_chat.id) in config.ADMIN:
        for i in all_user_id():
            try:
                context.bot.send_message(chat_id=i, text=i)
            except:
                pass

def deleteoneusersCommand(update: Update, context: CallbackContext):
    if str(update.effective_chat.id) in config.ADMIN:
        a = update.message.text[update.message.text.find(' ') + 1:]
        restart_one_users_Full_name(a)



def main():
    logger.info('Start bot')
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(oprosHandler)],
        states= {
            QUESTIONONE: [MessageHandler(Filters.text & ~Filters.command, questionone)],
            QUESTIONTWO: [MessageHandler(Filters.text & ~Filters.command, questiontwo)],
        },
        fallbacks=[MessageHandler(Filters.text & ~Filters.command, questiontwo)],
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler("start", startCommand))
    dispatcher.add_handler(CommandHandler("spam", spamCommand))
    dispatcher.add_handler(CommandHandler("admin", adminCommand))
    dispatcher.add_handler(CommandHandler("restartusers", deleteoneusersCommand))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, fullname))

    updater.start_polling()
    updater.idle()
    logger.info('Closing connect with API')

if __name__ == '__main__':
    main()