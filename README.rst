Chatbot exercices
=================

The goal of this project is to understand the different ways to implement a
chatbot. All the exercices came from this tutorial: https://blog.link-value.fr/d%C3%A9velopper-un-chatbot-en-python-3a8b0e518df5

Installation
-----------------

This project use virtualenvwrapper to create a virtual environment for python.

.. code-block:: bash

    $ sudo -H pip install virtualenvwrapper
    $ mkdir ~/.virtualenvs
    $ echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
    $ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
    $ bash
    $ mkvirtualenv chatbot --python=/usr/bin/python3
    $ workon chatbot
    $ pip install -r requirements.txt

Naive chatbot
-------------

In this first example, we will implement a naive chatbot that just repeat what
you said.

.. code-block:: bash

    $ python naive_chatbot.py