import os
import pyrogram
from pyrogram import Client

api_id = 9972455
api_hash = "5b1fd83b698e4e6670f3dcb053eecc06"

try:
   os.remove("techvj.session")
except:
     pass
with Client("techvj", api_id=api_id, api_hash=api_hash) as app:
    session = f"**🥀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 » 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 💞**\n\n`{app.export_session_string()}`\n\n**💥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [VJ Server](https://t.me/VJ_Botz) ✨**"
    app.send_message("me", session, disable_web_page_preview=True)
    try:
        app.join_chat("")
        app.join_chat("")
        app.join_chat("")
        app.join_chat("")
    except:
        pass
    print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")
    os.remove("techvj.session")

