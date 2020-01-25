import re
import json
import os

from dotenv import load_dotenv

import src.bot.config as config


def get_env(env_key, filepath):
    """ get_env gets environment variables from .env file

    :return: value of key given in .env file
    :rtype: String
    """
    dotenv_path = os.path.join(os.path.dirname(filepath), config.env)
    load_dotenv(dotenv_path)
    try:
        return os.getenv(env_key)
    except Exception as e:
        print("Require env file, not available")


def is_keyword_mentioned(text):
    """Checks if the trigger words to call the bot are present in the string

    :param text: comments form reddit
    :type text: String
    :return: True if keyword mentioned on trigger json file is present else false
    :rtype: Boolean
    """

    with open(config.trigger_file, 'r') as triggers:
        keywords = json.load(triggers)
    for keyword in keywords:
        if re.search(keyword, text, re.IGNORECASE):
            return True
    return False


def get_username(author):
    """Handles author names when comment was deleted before the bot could reply.

    :param author: author of the comment
    :type author: String
    :return: username of author if present else "[deleted]"
    :rtype: String
    """

    if not author:
        name = '[deleted]'
    else:
        name = author.name
    return name


def is_file_present():
    """Checks if all necessary files are present
    """
    assert os.path.isfile(config.env)
    assert os.path.isfile(config.sub_json)
    assert os.path.isfile(config.log_config_file)
    assert os.path.isfile(config.praw_ini)


def check_post_replied_to_file():
    """Checks if the file to record the id of comments replied is present

    :return: Open a file if not present else return True
    :rtype: Boolean
    """
    if not os.path.isfile(config.post_replied_to_file):
        open(config.post_replied_to_file, "w+")
    else:
        return True


def check_environment_variables(envn):
    """Check environment variables

    :param envn: environment value, should be "PROD" or "TEST"
    :type envn: String
    :return: subreddit that are to be checked
    :rtype: String
    """
    with open(config.sub_json, 'r') as subs:
        if envn == 'TEST':
            subreddit = get_env('TST_SUBS', __file__)
        elif envn == 'PROD':
            json_raw = json.load(subs)
            subreddit = '+'.join(json_raw)
    return subreddit


def read_file_in_list(file):
    """Read post replied to file to check if the comments that triggers the bot is already replied

    :param file: file name
    :type file: String
    :return: ids that are replied
    :rtype: String
    """
    with open(file, "r") as f:
        post_replied = f.read()
        post_replied = post_replied.split("\n")
        post_replied = list(filter(None, post_replied))
    return post_replied


def write_posts_that_are_replied(file, cmt_id):
    """Writes the id of comments that are replied

    :param file: filename that keeps records of comment it
    :type file: Strings
    :param cmt_id: comment id of comments that are replied
    :type cmt_id: String
    """
    with open(file, "a") as f:
        f.write(cmt_id + "\n")

def get_random_quote():
    return "HELLO"