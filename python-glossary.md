---
title: "Python Glossary"
date: "2018-08-12 17:24"
author: "YoungKoung Kim"
---

## Introduction
The goal of *Python Glossary* game is to check if a user knows important Python *terms*, which was created based on Python 3.7.0 website (https://docs.python.org/3/glossary.html) - *YK's Python Glossary (python_glossary.csv)*. Once the game starts, screen will display a brief description of the game. A user is prompted to choose the number of Python terms she or he wants to play. Then, the game will display the list of Python terms randomly selected from *YK's Python Glossary*. A user is supposed to write down the most appropriate term given the definition (or a description) of a Python *term*.
Once a user finishes the game, the screen will display her or his score. If a user quits the game before she or he finishes the game, the screen will display her or his performance based only on the completed answers.

## Rules of Game
Here are the rules of *Python Glossary* game.
* A user chooses the number of terms to play.
* When all questions are asked, the game will be terminated.
* For each question, a user can
 * Answer a question or
 * Skip a question or
 * Quit the game
* If a user answers a question correctly, she or he will get 10 points.
* If a user answers a question incorrectly or skip a question, she or he will get 0 points.

## Requirement
To run this program, a user needs to save the following files in a directory:
* python_glossary.py : Python program including the main as welll all necessary functions to play this game.
* python_glossary.csv : YK's Python Glossary file. When the game starts, the program will load this file to the game. 

## Reference
https://docs.python.org/3/glossary.html
https://www.pythonforbeginners.com/cheatsheet/python-glossary
