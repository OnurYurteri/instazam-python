# instazam-python

For converting url to 20sec mp3..

## How to run

```bash
cd instazam-python
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt

uvicorn main:app
```

## Test

```bash
curl --location --request POST 'localhost:8000/convert' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://instagram.fsaw2-2.fna.fbcdn.net/v/t50.2886-16/121626566_769569767232426_7898949840618761369_n.mp4?_nc_ht=instagram.fsaw2-2.fna.fbcdn.net&_nc_cat=106&_nc_ohc=esmcRlRHnmcAX_jIEZa&oe=5FF1BFCD&oh=75731340e14432609683054471e24d60",
    "recognition": "test-recognition-id"
}'
```
