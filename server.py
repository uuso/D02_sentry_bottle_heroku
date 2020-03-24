
from bottle import Bottle, run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://b0747e52ceec422280144fa1100e6372@sentry.io/5173623",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/')
def index():
    raise ValueError("It's a test message only!")
    # return


app.run(host = "10.186.0.248", port=8080)