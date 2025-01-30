class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7172020159" , "7172020159"
    sudo_users = "7361622601"
    GROUP_ID = -1002382022736
    TOKEN = "7527408650:AAEB-iYs6N9kAbnkSukqmXU28LEQubTOgOk"
    mongo_url = "mongodb+srv://xdragxt:drag123@dragtest.2b4zj.mongodb.net/?retryWrites=true&w=majority&appName=dragtest"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002393685933"
    api_id = 7155513
    api_hash = "aea00e5d96c3eb15647ca25c0f93a234"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
