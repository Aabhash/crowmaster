import random
import pandas as pd

import logging
from logging.config import fileConfig
import sklearn
import src.model.model_config as mc

from deeppavlov import train_model
from deeppavlov.core.commands.infer import build_model
from deeppavlov.core.common.file import read_json


class Trainer:
    def __init__(self):
        """
        Constructor for the trainer class
        """
        fileConfig(mc.log_config_file)
        self.logger = logging.getLogger('trainer')
        self.data_path = mc.training_data
        self.answer_data_path = mc.answers_data
        self.model_config = read_json(mc.config_path)

        self.model = None

    def set_config_params(self):
        """Set config parameters for training
        """        
        self.model_config['metadata']['variables']['ROOT_PATH'] = mc.local_path 
        self.model_config["dataset_reader"]["data_path"] = self.data_path
        self.model_config["dataset_reader"]["data_url"] = None
    
    def train(self):
        """
        Train model from config file
        - Set path to data
        - Train model
        - Set Object.model to be trained model
        :return: None
        """
        self.set_config_params()
        
        self.logger.info("Training begun")
        model = train_model(self.model_config)
        self.logger.info("Model and weights saved to file")

        self.model = model

        self.logger.info("************TRAINING COMPLETE *************")

    def classify_intent(self, comment):
        """
        Classifies intent from an incoming comment
        :param comment: Comment to be classified
        :return: Class of the comment sent
        """
        self.model_config['metadata']['variables']['ROOT_PATH'] = mc.local_path 
        try:
            self.model = build_model(self.model_config, download=False)
            return self.model([comment])[0]
        except sklearn.exceptions.NotFittedError:
            self.train()
            return self.model([comment])[0]

    def craft_reply(self, comment):
        """ Creates an reply to the provided comment

        :param question: the comment provided by the user
        :type question: string
        :return:reply generated according to the comment classification and rules
        :rtype: string
        """

        classified_class = self.classify_intent(comment)[0]
        reply = self.pick_random_reply(classified_class)

        return reply

    def get_answers_tuple(self, file_name=mc.answers_data):
        """ Extracts the answers from the specified file
        
        :param file_name: path to csv file with the responses, defaults to config.r_answers_data
        :type file_name: string, optional
        :return: response,domains tuple lists 
        :rtype: list of tuple
        """
        df = pd.read_csv(file_name)
        ans_tuple = [(line, domain) for domain, line in zip(df['intent'], df['answer'])]
        return ans_tuple


    def pick_random_reply(self, classified_label):
        """
        Picks a random reply from csv file of all possible replies

        :param classified_label: Label of the class
        :return: Reply picked from file
        """
        all_ans_tuples = self.get_answers_tuple(self.answer_data_path)
        possible_replies = [dual[0] for dual in all_ans_tuples if dual[1] == classified_label]
        if len(possible_replies) == 1:
            reply = possible_replies[0]            
        else:
            selected_ind = random.randint(0, len(possible_replies) - 1)
            reply = possible_replies[selected_ind]
        return reply


if __name__=="__main__":
    trainer=Trainer()
    trainer.train()
    try:
        trainer.logger.info(trainer.classify_intent("how is it going"))
        trainer.logger.info(trainer.craft_reply("how is it going"))
    except ValueError:
        trainer.logger.info('Error in Training')