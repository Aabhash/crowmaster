import re
import json
import os

from dotenv import load_dotenv

import src.bot.config as config
from src.model.train import Trainer


def get_env(env_key, filepath):
    """ get_env gets environment variables from .env file

    :return: value of key given in .env file
    :rtype: String
    """
    dotenv_path = config.env
    load_dotenv(dotenv_path)
    return os.getenv(env_key)

def get_trigger_words(file_path = config.trigger_file):
    """Get list of trigger words from file
    
    :param file_path: path of file where trigger words are stored, defaults to config.trigger_file
    :type file_path: String
    :return: List of Trigger words
    "rtype: list
    """        
    with open(file_path, 'r') as triggers:
        keywords = json.load(triggers)
    return keywords

def is_triggered(trigger_words, text):
    """Checks if the trigger words to call the bot are present in the string

    :param trigger_words: List of trigger_words
    :param trigger_words: list
    :param text: comments form reddit
    :type text: String
    :return: True if keyword mentioned on trigger json file is present else false
    :rtype: Boolean
    """

    for keyword in trigger_words:
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


def load_replied_comments(file_path = config.post_replied_to_file):
    """Load comments that have already been written to

    :param file: file name
    :type file: String
    :return: ids that are replied
    :rtype: String
    """
    with open(file_path, "r") as f:
        post_replied = f.read()
        post_replied = post_replied.split("\n")
        post_replied = list(filter(None, post_replied))
    return post_replied


def track_replied_comments(cmt_id, file_path=config.post_replied_to_file):
    """Store replied comment ids to file

    :param file_path: path to file that tracks previously replied comments
    :type file_path: Strings
    :param cmt_id: replied comment id
    :type cmt_id: String
    """
    with open(file_path, "a") as f:
        f.write(cmt_id + "\n")

def get_random_quote(comment):
    """ Calls trainer class to retrieve answer from model
    
    :param comment: Commend made by the user
    :type comment: String
    :return: Reply to the user
    :rtype: String
    """    
    trainer = Trainer()
    return trainer.craft_reply(comment)