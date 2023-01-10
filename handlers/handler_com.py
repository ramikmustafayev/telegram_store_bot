from handlers.handler import Handler
import telebot

class HandlerCommands(Handler):

    def __init__(self, bot) -> None:
        super().__init__(bot)



    def pressed_start_button(self,message:telebot.types.Message):
        self.bot.send_message(message.chat.id,
        f'{message.from_user.username},'
        f' здравствуйте! Жду дальнейших задач.',
        reply_markup=self.keyboards.start_menu()
        )

    def handle(self):
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text=='/start':
                self.pressed_start_button(message)
