class script(object):
    CMD_LIST = """ððĒ {},
âĒ /id - get id of a specifed user. 
âĒ /info  - get information about a user. 
âĒ /imdb  - get the film information from IMDb source. 
âĒ /search  - get the film information from various sources. 
âĒ /whois :-give a user full details 

 áīĘÉŠs ÉŠs ŌáīĘ áīáīáīÉŠÉīs 

âĒ /logs - to get the rescent errors 
âĒ /stats - to get status of files in db. 
âĒ /delete - to delete a specific file from db. 
âĒ /users - to get list of my users and ids. 
âĒ /chats - to get list of the my chats and ids 
âĒ /leave  - to leave from a chat. 
âĒ /disable  -  do disable a chat. 
âĒ /ban  - to ban a user. 
âĒ /unban  - to unban a user. 
âĒ /channel - to get list of total connected channels 
âĒ /broadcast - to broadcast a message to all users. 
âĒ /connect  - connect a particular chat to your PM. 
âĒ /disconnect  - disconnect from a chat. 
âĒ /connections - list all your connections. 
âĒ /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members. 
âĒ /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message. 
âĒ /filter - add a filter in chat. 
âĒ /filters - list all the filters of a chat. 
âĒ /del - delete a specific filter in chat. 
âĒ /delall - delete the whole filters in a chat (chat owner only)"""

    HELP_TXT = """ð·ðīð {}
ð·ðīððī ðļð ðð·ðī ð·ðīðŧðŋ ðĩðūð ðžð ðēðūðžðžð°ð―ðģð."""

    FILE_TXT = """âĪ ðððĨðĐ: ððĒðĨð ðð­ðĻðŦð ððĻððŪðĨð../
<b>ðąð ðððļð―ðķ ðð·ðļð ðžðūðģððŧðī ððūð ðēð°ð― ðððūððī ðĩðļðŧðīð ðļð― ðžð ðģð°ðð°ðąð°ððī ð°ð―ðģ ðļ ððļðŧðŧ ðķðļððī ððūð ð° ðŋðīððžð°ð―ðīð―ð ðŧðļð―ðš  ððū ð°ðēðēðīðð ðð·ðī ðð°ððīðģ ðĩðļðŧðīð.ðļðĩ ððūð ðð°ð―ð ððū ð°ðģðģ ðĩðļðŧðīð ðĩððūðž ð° ðŋððąðŧðļðē ðēð·ð°ð―ð―ðīðŧ ððīð―ðģ ðð·ðī ðĩðļðŧð ðŧðļð―ðš ðūð―ðŧð  ðūð ððūð ðð°ð―ð ððū ð°ðģðģ ðĩðļðŧðīð ðĩððūðž ð°  ðŋððļðð°ððī ðēð·ð°ð―ð―ðīðŧ ððūð ðžððð ðžð°ðšðī ðžðī ð°ðģðžðļð― ðūð― ðð·ðī ðēð·ð°ð―ð―ðīðŧ ððū ð°ðēðēðīðð ðĩðļðŧðīð...//</b>
âŠž ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð âš
âŠ /plink âšâš <b>ððīðŋðŧð ððū ð°ð―ð ðžðīðģðļð° ððū ðķðīð ðŧðļð―ðš.</b>
âŠ /pbatch âšâš <b>ðððī ððūðð ðžðīðģðļð° ðŧðļð―ðš ððļðð· ðð·ðļð ðēðūðžðžð°ð―ðģ.</b>
âŠ /batch âšâš <b>ððū ðēððīð°ððī ðŧðļð―ðš ðĩðūð ðžððŧððļðŋðŧðī ðĩðļðŧðīð.</b>
âŠž ððąððĶðĐðĨð âš
<code>/batch https://t.me/beta_updates/201 https://t.me/beta_updates/257</code>"""
 
    MUSIC_TXT = """ð·ðīð ðžð°ð―!
ð·ðīððī ðļð ððūð ðēð°ð― ðģðūðð―ðŧðūð°ðģ ðžðððļðē | ððļðģðīðū ðąð ðð·ðī ðēðūðžðžð°ð―ðģ /song ð°ð―ðģ /video"""

    BOT_TXT = """ððĒ {},
âŠ How To Use This Bot

/update - To Join Our Main Channel, You can use this ð"""
    UPDATE_CMD = """ððĒ {}, 
âŠ To Working of This Bot, Join the Main Channel Below 

âŠ Joining Because of Updates of Bots and All Others are through Main Channel

âŠ It is because of Copyright Issue is Very Low Compairing to Other Channels ð"""
    START_TXT = """HáīĘ {},
ðžð ð―ð°ðžðī ðļð <a href=https://t.me/{}>{}</a>,\n ðļ ðēð°ð― ðŋððūððļðģðī ðžðūððļðīð, ðđððð ð°ðģðģ ðžðī ððū ððūðð ðķððūððŋ ð°ð―ðģ ðžð°ðšðī ðžðī ð°ðģðžðļð―..."""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a Eva Mari clone Project
- ððūðððēðī ðēðūðģðī :<a href=https://github.com/Jeolpaul/George-MalarAutofilter>ðķðīðūððķðī ðžð°ðŧð°ð ð°ðððūðĩðļðŧððīð</a>
<b>DEVS:</b>
- ðģðð 1 <a href=https://t.me/TeamEvamaria>ððīð°ðž ðīðð°ðžð°ððļð°</a>
- ðģðð 2 <a href=https://t.me/JP_Jeol_org>áEOáŠ</a>

<b>ð Team â <a href=https://t.me/beta_bot_updates>ðŦ ðąðīðð° ðąðūðð ðŦ</a>\nâŊ âââââ â§ âââââ âŊ</b>\n"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. George Malar Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĒ /filter - <code>add a filter in chat</code>
âĒ /filters - <code>list all the filters of a chat</code>
âĒ /del - <code>delete a specific filter in chat</code>
âĒ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- This Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. George Malar Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Beta_Bot_Updates)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĒ /connect  - <code>connect a particular chat to your PM</code>
âĒ /disconnect  - <code>disconnect from a chat</code>
âĒ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features

<b>Commands and Usage:</b>
âĒ /id - <code>get id of a specified user.</code>
âĒ /info  - <code>get information about a user.</code>
âĒ /imdb  - <code>get the film information from IMDb source.</code>
âĒ /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĒ /logs - <code>to get the rescent errors</code>
âĒ /stats - <code>to get status of files in db.</code>
âĒ /delete - <code>to delete a specific file from db.</code>
âĒ /users - <code>to get list of my users and ids.</code>
âĒ /chats - <code>to get list of the my chats and ids </code>
âĒ /leave  - <code>to leave from a chat.</code>
âĒ /disable  -  <code>do disable a chat.</code>
âĒ /ban  - <code>to ban a user.</code>
âĒ /unban  - <code>to unban a user.</code>
âĒ /channel - <code>to get list of total connected channels</code>
âĒ /broadcast - <code>to broadcast a message to all users</code>"""

    ABOUT_TXT = """ð·ðīð {}
ð·ðīððī ðļð ðžð ð·ðīðŧðŋ ðēðūðžðžð°ð―ðģð."""
    ABOUT_TXT = """<b>âŊ ðžð ð―ð°ðžðī : {}
<b>âŊ ðēððīð°ððūð : <a href=https://t.me/JP_Jeol_org>áīáīáīĘ</a></b>
<b>âŊ ððŋðģð°ððīð : <a href=https://t.me/beta_bot_updates>Ęáīáīáī áīáīáīáīáīáīs</a></b>
<b>âŊ ðŧðļðąðð°ðð : ðŋðððūðķðð°ðž</b>
<b>âŊ ðŧð°ð―ðķðð°ðķðī : ðŋððð·ðūð― ðđ</b>
<b>âŊ ðģð°ðð° ðąð°ððī : ðžðūð―ðķðū-ðģðą</b>
<b>âŊ ðąðūð ððīðððīð : ĘáīĘáīáīáī</b>
<b>âŊ ðąððļðŧðģ ððð°ððð : ð1.0.43 [ðžð°ðđðūð]</b>"""

    STATUS_TXT = """áâš ððūðð°ðŧ ðĩðļðŧðīð: <code>{}</code>
áâš ððūðð°ðŧ ðððīðð: <code>{}</code>
áâš ððūðð°ðŧ ðēð·ð°ðð: <code>{}</code>
áâš ðððīðģ ðððūðð°ðķðī: <code>{}</code> """
 
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
 
