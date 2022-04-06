"""
    Description:

    Principal

    Author:           @Renan
    Created:          2022-04-05
    Copyright:        (c) Ampere Consultoria Ltda
"""

try:
    from setup.Control import Control;
    import time;
    import sys;
    import traceback;
    import os, shutil;
    from pprint import *;

    from termcolor import colored
    from src.prompt_data import parametros_prompt
    from dynaconf import Dynaconf
    from src.init_loguru import get_loguru_logger
    settings = Dynaconf(
        envvar_prefix="AMPERE",
        settings_files=["settings.toml", ".secrets.toml"],
        environments=True,
        load_dotenv=True,
    )
    logger = get_loguru_logger()
    logger.add(settings.LOG_MONITOR, rotation="10 MB")

except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")    


logger.info(30 * "-")
logger.info(colored("EXECUTANDO SCRIPT PRINCIPAL", color="yellow"))
logger.info(30 * "-")


lst_args = parametros_prompt()
caminho = lst_args.CAMINHO
planilha = lst_args.PLANILHA


# inicializa os principais objetos
start = time.process_time();
startDate = time.localtime();
try:    
    control = Control(plan_dados = planilha, path = caminho, time = startDate);
except:
    print("Erro de Execucao");
    print("Consulte o arquivo erro.txt");
    # cria o arquivo txt
    # saidaResul = open(caminho + "erro.txt", "w");
    saidaResul = open(caminho + "/" + "erro.txt", "w");
    saidaResul.write(traceback.format_exc());
    sys.exit(1);
elapsed = time.process_time();
elapsed = elapsed - start;

# exporta objetos do python para json se a opcao estiver habilitada na planilha
if control.isExpJsonHabilitada:
    control.exportaObjeto();

# libera a memoria
control = None;

print("Concluido - Tempo Total: " + str(int(float(elapsed))) + " segundos");
