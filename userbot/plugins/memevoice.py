# Credits to @spechide and his team for @TROLLVOICEBOT
# made by @h1m4n5hu0p_the_badass from the snippets of waifu AKA stickerizerbot....
# kang karega kya madarchod?
# aukaat h bsdk teri...jake baap ka loda chus ke aa....


import re

from userbot import bot
from mahakaalbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(Belongs_to_Lord_Shiva_nd_Haryana):
    mahakaal = Belongs_to_Lord_Shiva_nd_Haryana.pattern_match.group(1)
    if not mahakaal:
        if Belongs_to_Lord_Shiva_nd_Haryana.is_reply:
            (await Belongs_to_Lord_Shiva_nd_Haryana.get_reply_message()).message
        else:
            await edit_or_reply(Belongs_to_Lord_Shiva_nd_Haryana, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(mahakaal))}")

    await troll[0].click(
        Belongs_to_Lord_Shiva_nd_Haryana.chat_id,
        reply_to=Belongs_to_Lord_Shiva_nd_Haryana.reply_to_msg_id,
        silent=True if Belongs_to_Lord_Shiva_nd_Haryana.is_reply else False,
        hide_via=True,
    )
    await Belongs_to_Lord_Shiva_nd_Haryana.delete()
    

CmdHelp("memevoice").add_command(
  "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()