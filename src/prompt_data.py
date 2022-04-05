"""
    Description:

    Leitura dos parâmetros do prompt.

    Author:           @Palin
    Created:          2021-03-29
    Copyright:        (c) Ampere Consultoria Ltda
"""
import sys

try:
    import argparse
    from datetime import datetime
except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")
except Exception as exception:
    print(exception)
    sys.exit()


def parametros_prompt():
    """Parametros Prompt

    Returns:
        args_user: List: argumentos que o usuário passou.
    """
    parser = argparse.ArgumentParser(
        prog="Principal.py",
        description="Projeto MDI - Ex: python Principal.py -caminho 'C:/dev/MDI' -planilha 'C:/dev/MDI/MDI2.XLSX'",
        epilog="python3 Principal.py -h",
    )
    parser.add_argument("-v", "--version", action="version", version="%(prog)s vs. 1.0")
    parser.add_argument(
        "-caminho",
        action="store",
        dest="CAMINHO",
        type=str,
        default="C:/dev/MDI",
        help="Ex: -caminho 'C:/dev/MDI'",
    )
    parser.add_argument(
        "-planilha",
        action="store",
        dest="PLANILHA",
        type=str,
        default="C:/dev/MDI/MDI2.XLSX",
        help="Ex: -planilha 'C:/dev/MDI/MDI2.XLSX'",
    )
    return parser.parse_args()
