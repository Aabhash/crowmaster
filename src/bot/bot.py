import logging
import time
from logging.config import fileConfig

import praw
import praw.exceptions
from prawcore.exceptions import PrawcoreException as APIException

import src.bot.helper as helper
import src.bot.config as config

if __name__ == '__main__':
    helper.is_file_present()
    helper.check_post_replied_to_file()
    fileConfig(config.log_config_file)

    logger = logging.getLogger('reddit')
    logger.info("Started Reddit bot")

    environment = helper.get_env('ENV', __file__)
    assert environment is not None

    logger.info(f"Running on environment: {environment}")
    subreddits = helper.check_environment_variables(environment)
    logger.info(
        f"Got subreddit names: bot running on {subreddits.count('+') + 1 } subreddits.")

    try:
        reddit = praw.Reddit('bot')
        logger.info("Instantiated Reddit client")

        triggers = helper.get_trigger_words()

        subreddit = reddit.subreddit(subreddits)

        posts_replied_to = helper.load_replied_comments()
        logger.info("Got posts that were already replied")

    except APIException as e:
        logger.exception(
            f"PRAW Exception received: {str(vars(e))}. Server unable to start.")

    while True:
        try:
            comments = subreddit.stream.comments()
            logger.info("Going through all comments ...")
            for comment in comments:
                username = helper.get_username(comment.author)
                print(comment.id, username)
                if comment.id not in posts_replied_to:

                    if helper.is_triggered(triggers, comment.body):
                        comment.reply(helper.get_random_quote())
                        logger.info(
                            f"Replied to comment in subreddit '{comment.subreddit}'")

                        posts_replied_to.append(comment.id)
                        logger.info("Appended replied posts to list")

                        helper.track_replied_comments(comment.id)
                        logger.info(
                            f"Written to 'posts_replied_to.txt' file, ID '{comment.id}'")

        except KeyboardInterrupt:
            logger.error("Keyboard termination received!")
            break
        except APIException as e:
            logger.exception(
                f"PRAW Exception received: {str(vars(e))}. Retrying...")
            time.sleep(2)
