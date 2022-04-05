"""
    Description:

    Funções personalizadas para criar o PPTX

    Author:           @Thales
    Created:          2021-04-08
    Copyright:        (c) Ampere Consultoria Ltda
"""
try:
    from dynaconf import Dynaconf

    settings = Dynaconf(
        envvar_prefix="AMPERE",
        settings_files=["settings.toml", ".secrets.toml"],
        environments=True,
        load_dotenv=True,
    )
    import logging
    import os
    import sys
    from logging.handlers import RotatingFileHandler
    from pathlib import Path

    from pythonjsonlogger import jsonlogger

except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")
except Exception as exception:
    print(exception)
    sys.exit()


def get_logger(LOG_FILENAME):
    """Imprime o Log em arquivo no formato JSON e na tela em formato string"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    json_formatter = jsonlogger.JsonFormatter(
        fmt="%(levelname) %(lineno) " "%(message) %(asctime)",
        datefmt="%d/%m/%Y %I:%M:%S %p",
    )
    Path(settings.LOGS_DIR).mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        os.path.join(settings.LOGS_DIR, LOG_FILENAME),
        encoding="utf-8",
        maxBytes=2 * 1024 * 1024,
        backupCount=2,
    )
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter("%(asctime)-15s %(levelname)-8s %(message)s")
    file_handler.setFormatter(json_formatter)
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
