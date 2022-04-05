try:
    from .RecebeDados import RecebeDados;

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

class Usina(object):
    
    def __init__(self, recebe_dados, abaUsina, offset):
        # define fonte_dados como o objeto da classe RecebeDados e recebe a aba com o tipo de usina em quest�o
        self.fonte_dados = recebe_dados;
        self.nomeAba = abaUsina;
        self.fonte_dados.defineAba(self.nomeAba);
        
        # a variavel offset e importante pq a quantidade de linhas que devem ser puladas na planilha
        self.linhaOffset = offset;
        
        # importa dados gerais de Usinas
        self.importaDadosUsina();
        
        return;
    
    def importaDadosUsina(self):
        self.nomeUsina = self.fonte_dados.pegaEscalar("B3", lin_offset=self.linhaOffset);
        
        if (self.nomeAba != "Renov Ind."):
            
            # indica se o projeto e existente ou nao - existente > 0
            self.isProjeto = self.fonte_dados.pegaEscalar("D3", lin_offset=self.linhaOffset);
        
        return;
