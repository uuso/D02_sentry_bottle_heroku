import os
from bottle import Bottle, run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration


app = Bottle()

@app.route('/')
def index():
    raise ValueError("It's a test message only!")

@app.route('/success')
def success():
    return "It's OK!"
    
@app.route('/fail')
def fail():
    raise RuntimeError("Failure!")

sentry_sdk.init(dsn=os.environ.get("DSN"),integrations=[BottleIntegration()])

if os.environ.get("APP_LOCATION") == "heroku":    
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host = "10.186.0.248", port=8080)