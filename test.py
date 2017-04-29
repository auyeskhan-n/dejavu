import warnings, json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

config = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": "q", 
        "db": "dejavu",
    }
}
djv = Dejavu(config)

song = djv.recognize(FileRecognizer, "/home/nazarbek/Desktop/test2.mp3")
if (song['confidence'] < 100):
	print "Music not found"
else:
	print song['song_name'] 