try:
    from .Usina import Usina;
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

class Renovavel (Usina):
    
    def __init__(self, recebe_dados, abaRenov, offset, iRenov):
        
        # define fonte_dados como o objeto da classe RecebeDados e o nome da aba com as usinas UHE
        self.nomeAba = abaRenov;
        self.fonte_dados = recebe_dados;
        self.indexUsinaInterno = iRenov;
        
        # a variavel offset e importante pq a quantidade de linhas que devem ser puladas na planilha
        # pode ser diferente do index da usina. 
        self.linhaOffset = offset;
        
        # metodo referente a classe pai
        super(Renovavel, self).__init__(self.fonte_dados, self.nomeAba, self.linhaOffset);
        
        return;