import re
from slackbot.bot import Bot, listen_to, respond_to

import slackbot_settings as settings


def send_message(prompt, text):
    client = prompt._client
    client.send_message(settings.CHANNEL, text,
                        attachments=None, as_user=True)


def username_from_message(prompt):
    try:
        msguser = prompt._client.users.get(prompt._get_user_id())
        return msguser['name']
    except KeyError:
        return 'An unknown pokemon'


def decide_to_send(message):
    user = username_from_message(message)
    if user in settings.TEAM_VALOR_MEMBERS:
        return False
    else:
        return user


def make_gym_message(user):
    return '{} is talkin\' about gyms, look out!'.format(user)


def make_team_member_message(user, team_member):
    return '{} is talkin\' about {}, look out!'.format(user, team_member)


@listen_to(r'.*gym.*', re.IGNORECASE)
def whose_talkin_bout_gyms(message):
    user = decide_to_send(message)
    if user:
        send_message(message,
                     make_gym_message(user))


@listen_to(r'.*(' + '|'.join(settings.TEAM_VALOR_MEMBERS) + ').*',
           re.IGNORECASE)
def whose_talkin_bout_valor(message, valor_member):
    user = decide_to_send(message)
    send_message(message,
                 make_team_member_message(user, valor_member))


@listen_to(r'.*(' + '|'.join(settings.POKEMON_LIST) + ').*',
           re.IGNORECASE)
def whose_talkin_bout_pokemon(message, pokemon):
    user = decide_to_send(message)
    if user:
        send_message(message,
                     '{} is talking about {}'.format(user, pokemon))


@respond_to(r'.*')
def omni_response(message):
    message.reply(settings.MOTTO())


def main():
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    main()
