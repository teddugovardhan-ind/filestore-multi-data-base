import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 5665480584

MSG_EFFECT = 5046509860389126442

SHORT_URL = "arolinks.com" 
SHORT_API = "04f5d3b71c9e51a3ef466de1f6e079280f6af1bc" 
SHORT_TUT = "https://t.me/Anime_Telugu_English_VS/4156"

# Bot Configuration
SESSION = "yato"
TOKEN = "7640828023:AAE21zys6yCzJ2U-fce-76PYQT_ua3GEDxk"
API_ID = "28408609"
API_HASH = "d6ddeafb0c189d91b8197ad49103e806"
WORKERS = 5

DB_URI = "mongodb+srv://teddugovardhan544_db_user:WVjIA96jQ31net0j@cluster0.kwkkleo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "filestoremultidatabase"

FSUBS = [[-1002522308350, True, 10]] 

DB_CHANNEL = -1002599753693   # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002761663485": {"Data base 3": "Primary DB", "is_primary": True, "is_active": True},
#     "-1002498858164": {"Data base": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [5665480584, 6557934214]
# Bot Settings
DISABLE_BTN = True
PROTECT = True

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>ʟᴏᴠᴇ ᴘᴏʀɴʜᴡᴀ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ aʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
   "ABOUT": "<b><blockquote> ◈ ᴄʀᴇᴀᴛᴏʀ: <a href='https://t.me/ind_gamer_1'>Ind_gamer_1</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href='https://t.me/All_animes_in_telugu_Go'>Govar Orginals</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Telugu_English_VS'>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>\n◈ sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Marvel_movies_in_telugu_vs'>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/ind_gamer_1'>Ind_gamer_1</a></blockquote></b>",
    "REPLY": "<b>For More Join - @All_animes_in_teluguu_vs</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://graph.org/file/510affa3d4b6c911c12e3.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
