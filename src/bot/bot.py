import re
import time
import datetime
import json
import sys
import os
import logging
from logging.config import fileConfig

import praw
import praw.exceptions
from prawcore.exceptions import PrawcoreException as APIException

import src.bot.handler as handler
import src.bot.config as config

if __name__ == '__main__':
    handler.is_file_present()
    handler.check_post_replied_to_file()
    fileConfig(config.log_config_file)
    logger = logging.getLogger('reddit')
    logger.info("Started Reddit bot")

    try:
        environment = handler.get_env('ENV', __file__)
        logger.info(f"Running on environment: {environment}")
        subreddits = handler.check_environment_variables(environment)
        logger.info("Got subreddit names: bot running on {} subreddits".format(subreddits.count('+') + 1))

    except Exception as e:
        logger.exception(f"Could not get environment variables: {str(vars(e))}")

    while True:
        try:
            reddit = praw.Reddit('bot')
            logger.info("Instantiated Reddit client")

            posts_replied_to = handler.read_file_in_list(config.post_replied_to_file)
            logger.info("Got posts that were already replied")

            subreddit = reddit.subreddit(subreddits)
            comments = subreddit.stream.comments()

            for comment in comments:
                logger.info("Inside the loop to check comments")
                username = handler.get_username(comment.author)

                if comment.id not in posts_replied_to and username:

                    if handler.is_keyword_mentioned(comment.body):
                        print(handler.get_random_quote())
                        # comment.reply(handler.get_random_quote())
                        logger.info(f"Replied to comment in subreddit '{comment.subreddit}'")

                        posts_replied_to.append(comment.id)
                        logger.info("Appended replied posts to list")

                        handler.write_posts_that_are_replied(config.post_replied_to_file, comment.id)
                        logger.info("Written to 'posts_replied_to.txt' file, ID '{}'".format(comment.id))

        except KeyboardInterrupt:
            logger.error("Keyboard termination received. Bye!")
            break
        except APIException as e:
            logger.exception("PRAW Exception received: {}. Retrying...".format(str(vars(e))))
            time.sleep(2)
