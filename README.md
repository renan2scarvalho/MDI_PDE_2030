# PROJETO MDI EPE - PDE 2030

https://github.com/renan2scarvalho/MDI_PDE_2030

# Instalação do Python 2.7 no Pyenv

As instalações de versões antigas podem acarretar erros como:

```s
pyenv install 2.7.12
Downloading Python-2.7.12.tar.xz...
-> https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz
Installing Python-2.7.12...
ERROR: The Python ssl extension was not compiled. Missing the OpenSSL lib?

Please consult to the Wiki page to fix the problem.
https://github.com/pyenv/pyenv/wiki/Common-build-problems


BUILD FAILED (Ubuntu 20.04 using python-build 20180424)

Inspect or clean up the working tree at /tmp/python-build.20220325171437.19875
Results logged to /tmp/python-build.20220325171437.19875.log

Last 10 log lines:
rm -f /home/renan/.pyenv/versions/2.7.12/share/man/man1/python.1
(cd /home/renan/.pyenv/versions/2.7.12/share/man/man1; ln -s python2.1 python.1)
if test "xno" != "xno"  ; then \
        case no in \
                upgrade) ensurepip="--upgrade" ;; \
                install|*) ensurepip="" ;; \
        esac; \
         ./python -E -m ensurepip \
                $ensurepip --root=/ ; \
fi
```

Neste caso, cheque se o OpenSSL está mesmo instalado com o seguinte comando, e caso não, instale-o

```s
openssl version
```

OBS: para versões antigas do Python (para CPython, <3.5.3 e <2.7.13) demandam OpenSSL 1.0 enquanto as versões mais novas demandam a versão 1.1.


Primeiramente, instalar das dependencias binárias e ferramentas do Python em https://github.com/pyenv/pyenv/wiki#suggested-build-environment

Os demais pré-requisitos podem ser encontrados em https://github.com/pyenv/pyenv/wiki/Common-build-problems





# Instalação do Coopr

Baixe o arquivo: https://files.pythonhosted.org/packages/aa/94/86bf0a9a39eca96358990677f7f5d75b627688fca4e1cfcefd74dbec5eb2/Coopr-4.0.9597.tar.gz

```s
tar -zxvf Coopr-4.0.9597.tar.gz
Coopr-4.0.9597/
Coopr-4.0.9597/AUTHORS.txt
Coopr-4.0.9597/CHANGELOG.txt
Coopr-4.0.9597/coopr/
Coopr-4.0.9597/coopr/__init__.py
Coopr-4.0.9597/coopr/pyomo/
Coopr-4.0.9597/coopr/pyomo/__init__.py
Coopr-4.0.9597/Coopr.egg-info/
Coopr-4.0.9597/Coopr.egg-info/dependency_links.txt
Coopr-4.0.9597/Coopr.egg-info/PKG-INFO
Coopr-4.0.9597/Coopr.egg-info/requires.txt
Coopr-4.0.9597/Coopr.egg-info/SOURCES.txt
Coopr-4.0.9597/Coopr.egg-info/top_level.txt
Coopr-4.0.9597/LICENSE.txt
Coopr-4.0.9597/PKG-INFO
Coopr-4.0.9597/README.txt
Coopr-4.0.9597/setup.cfg
Coopr-4.0.9597/setup.py
```

```s
cd Coopr-4.0.9597
python setup.py install --user
```

# Instruções Básicas do Modelo Computacional MDI

## Introdução

O modelo computacional MDI (modelo de decisão de investimentos), empregado na elaboração do Plano Decenal de Expansão de Energia 2030 (PDE 2030), é disponibilizado em código-fonte aberto para permitir máxima transparência na modelagem matemática e implementação. Esta disponibilização também permite que instituições, centros de pesquisa e agentes do setor, bem como a comunidade acadêmica, possam contribuir efetivamente para o aprimoramento do modelo.

Pré-requisitos mínimos:
- Python 3.x (Windows)
- Bibliotecas da própria linguagem importadas ao longo do código ;
- Coopr
- pypiwin32
- Pyomo
- DateTime
- Jsonpickle
- Openpyxl
- Xlrd
- Xlwt
- python-dateutil
- Pacote de otimização (CPLEX, COIN-OR, Gurobi, etc).

Ambiente computacional utilizado nos estudos do PDE 2030
•	Python 3.8
•	CPLEX Studio 12.9
•	MS Windows Server 2012 R2
•	MS Excel 2013

# Instruções básicas para execução

## Interface para execução

A execução é feita a partir da pasta de trabalho MS Excel `Dados_MDI_PDE_2030.xlsx` (disponibilizada junto com o código-fonte), que também contém todos os dados necessários para a montagem do problema de otimização resolvido pelo MDI.

## Configurações Iniciais

Inicialmente é necessário configurar o caminho para o pacote de otimização, editando-se o arquivo “Control.py” (linha 36), conforme figura a seguir:


```py
        # habilita o cplex
        optsolver = SolverFactory("cplex", executable= "C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio129\\cplex\\bin\\x64_win64\\cplex.exe");
        print ("Modelo Criado");
        self.problema.modelo.preprocess();
        print ("Pre-process executado");
```

Em seguida, é necessário configurar, na planilha “Inicial” da pasta de trabalho “Dados_MDI_PDE_2030.xlsx”, o caminho completo do arquivo “Principal.py”, que deve estar salvo na mesma pasta dos demais arquivos de código-fonte. Outra informação declarada nesta planilha é o executável do Python 3.x, conforme destacado na figura a seguir:

![Fig](docs/figuras/opcoes_entrada.png)

# Execução

A execução é feita a partir do botão “Executar MDI” disponível na mesma planilha onde foram feitas as configurações iniciais.

# Saídas

As saídas (em formato texto) são geradas no mesmo caminho onde se encontra a pasta de trabalho que iniciou a execução.
A pasta de trabalho “Resumo.xlsx”, que deve também estar no mesmo caminho, ao final da execução, será preenchida com o resumo da expansão bem como os valores de CME solicitados anualmente.

# Contato

Para comentários, dúvidas e sugestões sobre o MDI, favor enviar e-mail para modelos.sgr@epe.gov.br.

