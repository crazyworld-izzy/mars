from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("ɢʀᴏᴜᴘs", callback_data="mplus HELP_Group")],
    [InlineKeyboardButton("Tᴀɢ-Aʟʟ", callback_data="mplus HELP_TagAll"), 
    [InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("Tʀᴜᴛʜ-ᗪᴀʀᴇ", callback_data="mplus HELP_TD"),InlineKeyboardButton("ʜᴀsᴛᴀɢ", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("ᴛᴛs", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("ғᴜɴ", callback_data="mplus HELP_Fun"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]
