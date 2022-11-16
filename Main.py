from src.database import all_user_id, restart_one_users_Full_name, delete_results, restart_db, add_question_seven, add_question_eight, add_question_nine, add_question_ten, add_question_three, add_question_four, add_question_five, add_question_six, add_question_two, add_question_one, add_user_and_course, get_state, get_full_name, check_user_id, add_full_name_in_first_table, add_length, get_length, minus_one_length_and_plus_state
from src.dataframe import StudentXls
import src.CallbackLists as CallbackList
import src.inlineKeyboard as inlineKeyboard
import src.questionAdd as questionAdd
from resources import config
import logging
from telegram import *
from telegram.ext import *
from telegram.ext.defaults import Defaults
from telegram.ext.dispatcher import run_async

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

StudentXl = StudentXls("resources\liststudent.xls")

StudentAndDiscipline = StudentXl.list_Student() #in this list saves name students and his lessons in format [(Name, lesson), ... , (name1399, lesson1399)]
allpeople = StudentXl.set_people() #all student list


QUESTIONONE, QUESTIONTWO = range(2)

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
        if StudentXls.binary_search(allpeople, msg):

            add_full_name_in_first_table(msg, user_id)
            add_length(StudentXls.search_length(StudentAndDiscipline, msg), user_id)

            if get_length(user_id) != 0:
                for i in range(len(StudentAndDiscipline)):
                    if msg == StudentAndDiscipline[i][0]:

                        update.message.reply_text(StudentAndDiscipline[i][1], reply_markup=ReplyKeyboardMarkup(nothavedis, resize_keyboard = True))
                        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp1, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons))
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
                        update.message.reply_text(config.qfp1, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons))
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
    queryAnswer = update.callback_query
    queryAnswer.answer()
    queryAnswer.edit_message_text(text=f"Дякую ваша відповідь важлива для нас")

    if query == 'omgg':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Not done")

    if query == 'nowayy':
        delete_results()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Done')

    if query == 'noway':
        restart_db()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Done')

    if query == 'omg':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Not done")


    if query in CallbackList.callback_list:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp2, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons2))
        questionAdd.questionAddOne(StudentAndDiscipline, update.effective_chat.id, query)

    if query in CallbackList.callback_list2:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp3, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons3))
        questionAdd.questionAddTwo(StudentAndDiscipline, update.effective_chat.id, query)

    if query in CallbackList.callback_list3:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp4, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons4))
        questionAdd.questionAddThree(StudentAndDiscipline, update.effective_chat.id, query)

    if query in CallbackList.callback_list4:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp5, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons5))
        questionAdd.questionAddFour(StudentAndDiscipline, update.effective_chat.id, query)

    if query in CallbackList.callback_list5:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp6, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons6))
        questionAdd.questionAddFive(StudentAndDiscipline, update.effective_chat.id, query)

    if query in CallbackList.callback_list6:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp7, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons7))
        questionAdd.questionAddSix(StudentAndDiscipline, update.effective_chat.id, query)

    if query in CallbackList.callback_list7:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp8, reply_markup=InlineKeyboardMarkup(inlineKeyboard.buttons8))
        questionAdd.questionAddSeven(StudentAndDiscipline, update.effective_chat.id, query)

    if query in CallbackList.callback_list8:
        context.bot.send_message(chat_id=update.effective_chat.id, text=config.qfp9)
        questionAdd.questionAddEight(StudentAndDiscipline, update.effective_chat.id, query)
        return QUESTIONONE


def questionone(update: Update, context: CallbackContext):
    questionAdd.questionAddNine(StudentAndDiscipline, update.effective_chat.id, update.message.text)
    update.message.reply_text(config.qfp10)
    return QUESTIONTWO

def questiontwo(update: Update, context: CallbackContext):
    nextdis = [[KeyboardButton('Наступна дисципліна')]]

    questionAdd.questionAddTen(StudentAndDiscipline, update.effective_chat.id, update.message.text)
    update.message.reply_text('Дякую за пройдену дісципліну, для наступної натисніть кнопку знизу', reply_markup = ReplyKeyboardMarkup(nextdis,resize_keyboard = True))
    return ConversationHandler.END



def adminCommand(update: Update, context: CallbackContext):
    msg = update.message.text
    user_id = update.effective_chat.id
    keybo = [
            [KeyboardButton('Spam'), KeyboardButton('Delete(restart one users)')],
            [KeyboardButton('Delete db(bot)'), KeyboardButton('Print users')],
            [KeyboardButton('back'), KeyboardButton('Delete results')]
        ]
    if str(user_id) in config.ADMIN:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome admin', reply_markup = ReplyKeyboardMarkup(keybo,resize_keyboard = True))

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
        entry_points=[CallbackQueryHandler(oprosHandler, pattern='.*')],
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