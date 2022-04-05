"""
    Description:

    Executa um comando com Subprocess

    Author:           @Thales/Palin
    Created:          2021-05-17
    Copyright:        (c) Ampere Consultoria Ltda
"""

import sys

try:
    import subprocess
    from pathlib import Path

    from dynaconf import Dynaconf
    from ecmwf.packages.ecmwf_utils import get_loguru_logger, init_loguru

    settings = Dynaconf(
        envvar_prefix="AMPERE",
        settings_files=["settings.toml", ".secrets.toml"],
        environments=True,
        load_dotenv=True,
    )

    init_loguru(
        sentry_on=True,
        sentry_dsn=settings.sentry_dns,
        sentry_breadcramp_level="INFO",
        sentry_event_level="WARNING",
        file_path=Path(settings.LOG_RUN_COMMAND),
        diagnose=True,
        backtrace=True,
    )
    logger = get_loguru_logger()

except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")
except Exception as exception:
    print(exception)
    sys.exit()


def run_command(strComando: str = None, show_output: bool = True):
    try:
        cmd_exec = subprocess.run(
            strComando,
            shell=True,
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if show_output:
            logger.info("-" * 80)
            logger.info(f"Comando: {strComando}")
            logger.info("-" * 80)
            logger.info(cmd_exec.stdout)

        if cmd_exec.stderr:
            logger.error(cmd_exec.stdout)
            logger.error("-" * 80)
            if "Input does not contain any field" in cmd_exec.stderr:
                logger.error("Abortando o programa!")
            logger.error("-" * 80)
            exit()

        if not cmd_exec.returncode == 0:
            logger.error(f"Error: Cód Saída: {cmd_exec.returncode}")
            logger.error(f"Error: Cód Saída: {cmd_exec.stderr}")
            exit()
    except Exception as err:
        logger.error(err)
