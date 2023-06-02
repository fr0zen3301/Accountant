from aiogram import types
from dispatcher import dp
import re
from bot import BotDB
from aiogram import md

@dp.message_handler(commands="start")
async def start(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

    await message.bot.send_message(message.from_user.id, "Welcome!")


@dp.message_handler(commands=("spent", "s", "earned", "e"), commands_prefix="/!")
async def record(message: types.Message):
    cmd_variants = (('/spent', '/s', '!spent', '!s' ), ('/earned', '!earned', '/e', '!e'))
    operation = '-' if message.text.startswith((cmd_variants[0])) else '+'

    value = message.text
    for i in cmd_variants:
        for j in i:
            value = value.replace(j, '').strip()

    if(len(value)):
        x = re.findall(r"\d+(?:.\d+)?", value) # regex101.com

        if(len(x)):
            value = float(x[0].replace(',', '.'))

            BotDB.add_record(message.from_user.id, operation, value)

            if(operation == '-'):
                await message.reply("☑️ Expense successfully received!")
            else:
                await message.reply("☑️ Income successfully received!")

        else:
            await message.reply("😣Failed to determine the amount!")
    else:
        await message.reply("🫠 Entries not found!")


@dp.message_handler(commands=("records", "r"), commands_prefix="/!")
async def records(message: types.Message):
    cmd_variants = ('/records', '/r', '!records', '!r' )
    within_als ={
        "day": ('today', 'day'),
        "week": ('week', 'w'),
        "month": ('month', 'm'),
        "year": ('year', 'y')
    }

    cmd = message.text
    for r in cmd_variants:
        cmd = cmd.replace(r, '').strip()

    within = 'day' # set as default
    if(len(cmd)):
        for k in within_als:
            for als in within_als[k]:
                if(als == cmd):
                    within = k

    # fetch
    records = BotDB.get_records(message.from_user.id, within)

    if(len(records)):
        answer = f"🕛Your records for {within_als[within][-1]}:\n"

        for r in records:
            answer += ("➖Expense" if not r[2] else "➕ Income")
            answer += f" - {r[3]} $"
            answer += f" ({r[4]})\n"

        await message.reply(answer) # await message.answer(f"Sender name: {md.quote_html(answer)}")
        ''''''
    else:
        await message.reply("🫠No records!")






