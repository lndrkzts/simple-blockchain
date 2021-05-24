
# Simple blockchain

## Setup

First, create the virtual enviroment
```sh
python -m venv env
```
Then, activate it and run 
```sh
pip install -r requirements.txt
```

## Start

To start the app we need to run
```sh
uvicorn main:app --reload
```
## Enpoints documentation

All endpoints, request and responses are documented using OAS3 in:
```sh
http://localhost:<port>/docs
```

