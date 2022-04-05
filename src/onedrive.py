"""
    Description: Funções Específicas deste Projeto

    - Este arquivo contém funções que NÃO SÃO GENERALIZÁVEIS e que se utilizam
    de Classes de Módulos já consolidados tais como: Argparser, Requests
    para executar determinadas ações importantes para este projeto.

    Author:           @Palin
    Created:          2021-05-06
    Copyright:        (c) Ampere Consultoria Ltda
"""
import sys

try:
    from datetime import datetime

    from dynaconf import Dynaconf

    settings = Dynaconf(
        envvar_prefix="AMPERE",
        settings_files=["settings.toml", ".secrets.toml"],
        environments=True,
        load_dotenv=True,
    )

    import json
    from datetime import datetime

    import jwt
    import msal
    import requests

    from src.srequest import requests_retry_session

except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")
except Exception as exception:
    print(exception)
    sys.exit()


def get_header_msgraph_auth(debug=False):
    """
    Retorna o Header com o TOKEN de autenticação
    """

    tenantID = settings.tenantID
    authority = "https://login.microsoftonline.com/" + tenantID
    client_id = settings.client_azure_id
    client_secret = settings.client_azure_secret
    scope = ["https://graph.microsoft.com/.default"]

    app = msal.ConfidentialClientApplication(
        client_id, authority=authority, client_credential=client_secret
    )

    try:
        accessToken = app.acquire_token_silent(scope, account=None)
        if not accessToken:
            try:
                accessToken = app.acquire_token_for_client(scopes=scope)
                if accessToken["access_token"]:
                    # print('-'*80)
                    # print('TOKEN requerido com SUCESSO...')
                    # print('-'*80)
                    requestHeaders = {
                        "Authorization": "Bearer " + accessToken["access_token"]
                    }
                else:
                    print("-" * 80)
                    print(
                        "Error aquiring authorization token. Check your tenantID, client_id and client_secret."
                    )
                    print("-" * 80)
                    exit()
            except Exception as err:
                print(f"OneDrive Error: {accessToken['error']}")
                print(f"OneDrive Error Description: {accessToken['error_description']}")
                print(err)
                sys.exit()
        else:
            print("-" * 80)
            print("TOKEN recebido do MSAL CACHE...")
            print("-" * 80)

        if debug:
            decodedAccessToken = jwt.decode(accessToken["access_token"], verify=False)
            accessTokenFormatted = json.dumps(decodedAccessToken, indent=2)
            print("Decoded Access Token")
            print(accessTokenFormatted)
            # Token Expiry
            tokenExpiry = datetime.fromtimestamp(int(decodedAccessToken["exp"]))
            print("Token Expires at: " + str(tokenExpiry))

        return requestHeaders

    except Exception as err:
        print(err)


def get_figure_onedrive(url_file: str):

    requestHeaders = get_header_msgraph_auth()
    try:
        res = requests_retry_session().get(
            url_file, stream=False, timeout=5, headers=requestHeaders
        )
        if res.status_code == 200:
            return res.content
        else:
            print("-" * 80)
            print(f"Error: status {res.status_code} url: {url_file}!")
            print("-" * 80)
            return None

    except requests.ConnectionError as e:
        print("Request URI - Connection Error. Pode ser sua internet!\n")
        print(str(e))
    except requests.Timeout as e:
        # Podemos tratar de tentar novamente aqui dentro
        print("Request URI - Timeout Error - server busy")
        print(str(e))
    except requests.TooManyRedirects as e:
        # URI ou URL que não exista
        print("Request URI - TooManyRedirects Error")
        print(str(e))
    except requests.RequestException as e:
        # Catástrofe! Não sabemos o que deu errado.
        print("Erro geral - verifique se a uri_estacoes está correta!")
        print(str(e))
    except KeyboardInterrupt:
        print("Você teclou CTRL+C! Parada forçada!")
        exit()
