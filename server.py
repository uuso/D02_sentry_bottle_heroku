import sentry_key
from bottle import Bottle, run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn=sentry_key.dsn,
    integrations=[BottleIntegration()]
)

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


app.run(host = "10.186.0.248", port=8080)