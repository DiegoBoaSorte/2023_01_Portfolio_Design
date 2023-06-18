## Como Utilizar o Sistema:

## Requisitos:

Para que a execução do sistema e seu uso sejam efetivados, seguir o passo a passo abaixo:

1. Intalação do Git:
  - Você precisará do git instalado para poder fazer a clonagem deste repositório; https://git-scm.com/downloads

2. Python:
  - No momento em que for instalar o python, escolha uma versão superior à 3.6. Durante a instalação, não se esqueça de marcar a opção da instalação do "pip"; https://www.python.org/downloads/

## Clonando o repositório

Com o Git e o Python instalados em sua máquina, siga os próximos passos:

1. Clone o repositório através de um terminal, utilize o comando:

```
git clone https://github.com/DiegoBoaSorte/portfolio_diegodias
``` 

2. Ainda no terminal vá para a pasta src:
```
cd .\portfolio_diegodias\src\

```

## Iniciando o ambiente virtual

Com o repositório clonado e no diretório correto, você deverá criar um ambiente virtual para rodar o sistema. Siga os próximos passos:

1. Ao entrar na pasta src, digite os seguintes comandos:
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
flask run
```

> O comando flask run, irá inicializar o site dentro do ambiente virtual.

> Provavelmente irá aparecer um link no próprio terminal, basta segurar a tecla "CONTROL" e clicar sobre o link ou então simplesmente acessar no seu navegador o link: http://127.0.0.1:5000

## Desativando o ambiente

Para encerrar o uso do site e sair do ambiente virtual vá ao seu terminal, (onde o Flask está rodando) aperte a tecla CONTROL, em seguida a tecla "C" e execute o seguinte comando no terminal:
```
deactivate
```

## Obrigado!


