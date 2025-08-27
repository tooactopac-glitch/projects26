from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from gtts import gTTS
from fastapi.responses import FileResponse
from uuid import uuid4

app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost",
    "https://yourfrontend.com"
]

# Apply CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class TextAudio(BaseModel):
    text:str

@app.post("/text")
def create_text(ta: TextAudio):
    fname = str(uuid4()) + ".mp3"
    text = ta.text
    tts = gTTS(text=text,lang='en')
    tts.save("audios/"+fname)
    return FileResponse("audios/"+fname)

@app.get('/')
def index():
    # text = "this is FastAPI and gtts"
    # tts = gTTS(text=text,lang='en')
    # tts.save('output.mp3')
    return FileResponse('audios/output.mp3',
                        media_type="audio/mpeg",
                        filename="output.mp3",
                        headers={"Content-Disposition":"attachment; filename=output.mp3"})