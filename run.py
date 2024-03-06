import os
from watchreviews import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

# import os
# from flask import (Flask, flash, render_template,
#     redirect, request, session, url_for)


# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("base.html")

# if __name__ == "__main__":
#     app.run(
#         host=os.environ.get("IP, 0.0.0.0"),
#         port=int(os.environ.get("PORT", "5000")),
#         debug=True
#     )