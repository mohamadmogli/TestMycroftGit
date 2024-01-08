from mycroft import MycroftSkill, intent_file_handler


class Icecream(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('icecream.intent')
    def handle_icecream(self, message):
        flavour = message.data.get('flavour')

        self.speak_dialog('icecream', data={
            'flavour': flavour
        })


def create_skill():
    return Icecream()

