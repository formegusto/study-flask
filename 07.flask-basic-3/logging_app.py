from logging import log
from flask import Flask
import requests as req

app = Flask(__name__)
app.debug = False
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(
        "./log/app.log", maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)
    # add Handler를 설정해줘야 app.logger로 이용가능
    app.logger.addHandler(file_handler)


@app.errorhandler(404)
def not_found(err):
    app.logger.error(err)
    return "<h1>404 Not Found</h1>", 404


if __name__ == "__main__":
    app.run(host="localhost", port=80)
