import os
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG

__author__ = 'colla69'


def play_player():
    os.system("cmus-remote -p")


def pause_player():
    os.system("cmus-remote -u")


def search_player(self, text):
    os.system("cmus-remote -C " + text)
    os.system("cmus-remote -n")


def stop_player():
    os.system("killall cmus")


class CmusPlayerSkill(MycroftSkill):

    def __init__(self):
        super(CmusPlayerSkill, self).__init__(name="TemplateSkill")
        # Initialize working variables used within the skill.
        self.running = False

    @intent_file_handler('play.music.intent')
    def handle_play_music_ntent(self, message):
        if not self.running:
            self.start_player()
        play_player()

    @intent_file_handler('pause.music.intent')
    def handle_pause_music_intent(self, message):
        pause_player()

    @intent_file_handler('search.music.intent')
    def handle_search_music_intent(self, message):
        if not self.running:
            start_player()
        LOG.info(message)
        search_player(message)

    def start_player(self):
        self.running = True
        os.system("cmus  </dev/null>/dev/null 2>&1 &")

    def converse(self, utterances, lang="en-us"):
        # contains all triggerwords for second layer Intents
        LOG.info(self.dictation_words)
        ####
        return False

    def stop(self):
        if self.running:
            stop_player()


def create_skill():
    return CmusPlayerSkill()
