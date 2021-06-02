from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1699433689:AAGLBcB9C1-3ol33dBvT61nhdvnItBHKdNc"
	APP_ID = 3319662
	API_HASH = "ae3fb7d72d5babfd4315ffb3a9a93a86"
	OWNER_ID = 1508105856 #ID of bot owner
	AUTH_CHANNEL = [-1001151086861]
	UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "uploadasdoc@LeechingsRobot")
