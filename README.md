# Accountant
# made by khamidullojon. Soonchunhyang University, South Korea


                                 <! -- DOCUMENTATION --!>

DESCRIPTION. 

Telegram bot that uses Telegram API and own database to store user’s data. Telegram bot for accountant that has simple functions like store your data, and show it again to you via history. 

HOW TO USE:

Go to DM with the bot and use /start button to start using this bot. 
There some commands that will help you:
1.	/spent , /s , !spent, !s – after that command input an amount of your expense. For example: /spent 2000
2.	/earned , /e , !earned , !e - after that command input an amount of your income. For example: /earned 2000
3.	/history , /h - after this command input a period of your history. For example: /history day , /history week


database.py to describe methods to interaction with DB:

•	 Method to check user existence in Database
•	Adding a user into Database
•	Adding incomes/expenses 
•	Getting records

actions.py to write bot’s commands. There 3 commands here:

•	/start Bot gets this command every time when a user runs the bot. Initializes the user in database and greets him.
•	/spent /earned makes record about income and expense. Added them two into one command, because they are the same task, only operation changes(+ income, - expense).
•	/records to check your records for a certain period


WARNING:

1.	If you have trouble with displaying your records and getting error(CANTParseEntities), import md from aiogram 
from aiogram import md
and change line 76 in actions.py into 
await message.reply({md.quote_html(answer)})
2.	To get more information about it go to: 
https://docs.aiogram.dev/en/latest/_modules/aiogram/types/message.html#Message.parse_entities

