"""
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝

                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                        ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
"""
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.xᴇʀᴏꜰɪʟᴇᴛꜱ.butts import MIB,SIB
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʟɪʙʀᴀʀʏ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʜᴏᴍᴇ import *



@Client.on_message(
filters.group
& ~filters.edited
& Known_admins
& filters.command("shutdown", prefixes=DYNO_COMMANDK))
async def down(client, XS: XeroSpeak):
    event = await XS.reply_text( "`Turing Off Heroku Dynos...`")
    await asyncio.sleep(2)
    await event.edit("**[ ⚠️ ]** \n**Ӽɛʀօռօɨɖ Dynos is now turned off. Manually turn it on to start again.**")
    if HEROKU_APP_NAME is not None:
        HEROKU_APP_NAME.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)