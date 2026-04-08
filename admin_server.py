from flask import Flask, request, Response, render_template

# admin_server.py

app = Flask(__name__, template_folder="admin/templates")

USERNAME = "rjp"
PASSWORD = "dashboard"


# -------------------------
# AUTH
# -------------------------
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD


def authenticate():
    return Response(
        "Login required",
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'}
    )


def requires_auth(f):
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
    app.run(debug=True)
