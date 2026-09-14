import os

from flask import Flask, request, Response, render_template
from functools import wraps

# admin_server.py

app = Flask(__name__, template_folder="admin/templates")

# Credentials must be supplied through environment variables, never stored in
# the repository. The server will refuse to authenticate until both values
# are configured.
USERNAME = os.environ.get("RJP_ADMIN_USERNAME")
PASSWORD = os.environ.get("RJP_ADMIN_PASSWORD")


# -------------------------
# AUTH
# -------------------------
def check_auth(username, password):
    return bool(USERNAME and PASSWORD) and username == USERNAME and password == PASSWORD


def authenticate():
    return Response(
        "Login required",
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'}
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


# -------------------------
# ROUTES
# -------------------------
@app.route("/admin")
@requires_auth
def admin_dashboard():
    return render_template("dashboard.html")


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=False)
