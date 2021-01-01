from fastapi import FastAPI
from pydantic import BaseModel
from download import download_file
from trim_and_convert import get_audio

app = FastAPI()


class ConvertRequest(BaseModel):
    recognition: str
    url: str


@app.post("/convert")
def convert(request: ConvertRequest):
    saved_path = download_file(request.url, request.recognition)
    converted_path = get_audio(saved_path, request.recognition)
    return {"path": converted_path}
