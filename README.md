Crow Master Bot
================

AI enabled reddit bot.

Getting up and running
===

Set up a virtual environment. 

```
conda create -n bot_env python=3.7 conda
```

Setting up requirements

```
conda install -c conda-forge praw
conda install -c conda-forge python-dotenv
```

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Training the model
===

```
python -m src.model.train
```

Running server
===

```
python -m src.bot.bot
```

Contributing
===

Please see [CONTRIBUTING.md](/CONTRIBUTING.md) for details on contributing.


###### tags: `dragon-prince` `reddit` `bot` `crow-master`