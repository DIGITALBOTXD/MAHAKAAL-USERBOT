"""WikiMedia.ORG
Syntax: .wikimedia Query"""
import requests
from mahakaalbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="wikimedia (.*)"))
@bot.on(sudo_cmd(pattern="wikimedia (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://commons.wikimedia.org/w/api.php?action={}&generator={}&prop=imageinfo&gimlimit={}&redirects=1&titles={}&iiprop={}&format={}".format(
        "query",
        "images",
        "5",
        input_str,
        "timestamp|user|url|mime|thumbmime|mediatype",
        "json",
    )
    r = requests.get(url).json()
    result = ""
    results = r["query"]["pages"]
    for key in results:
        current_value = results[key]
        pageid = current_value["pageid"]
        title = current_value["title"]
        imageinfo = current_value["imageinfo"][0]
        timestamp = imageinfo["timestamp"]
        user = imageinfo["user"]
        descriptionurl = imageinfo["descriptionurl"]
        mime = imageinfo["mime"]
        mediatype = imageinfo["mediatype"]
        result += """\n
        pageid: {}
        title: {}
        timestamp: {}
        user: [{}]({})
        mime: {}
        mediatype: {}
        """.format(
            pageid, title, timestamp, user, descriptionurl, mime, mediatype
        )
    await event.edit("**Search**: {} \n\n **Results**: {}".format(input_str, result))

CmdHelp("wikimedia").add_command(
  "wikimedia", "<query>", "Searchs the query from WikiMedia"
).add()