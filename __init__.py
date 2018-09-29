# skill-bbc-radio
#
# A Mycroft skill to play BBC radio stations. Currently only configured
# for Radio 1 whilst I figure out how to select multiple from array of
# some sort.
#
# Based on the mycroft-skill-cbc-news skill by chrison999
#
# Modified by jubbathejack
#
# This skill is licensed under the GNU General Public License v3.
# You should have received a copy of the GNU General Public License
# along with this skill.  If not, see <http://www.gnu.org/licenses/>.

import time

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util import play_mp3
from mycroft.util.log import getLogger

__author__ = 'jubbathejack'

LOGGER = getLogger(__name__)


class BBCRadioSkill(MycroftSkill):
    def __init__(self):
        super(BBCRadioSkill, self).__init__(name="BBCRadioSkill")
        self.process = None

    def initialize(self):
        intent = IntentBuilder("BBCRadioIntent").require(
            "BBCRadioKeyword").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        try:

            rstation = "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"
            self.speak_dialog('start.radio')
            time.sleep(5)

            self.process = play_mp3(rstation)

        except Exception as e:
            LOGGER.error("Error: {0}".format(e))

    def stop(self):
        if self.process and self.process.poll() is None:
            self.speak_dialog('stop.radio')
            self.process.terminate()
            self.process.wait()


def create_skill():
    return BBCRadioSkill()