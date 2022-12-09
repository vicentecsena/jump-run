Projeto baseado no exemplo disponível em [The ultimate introduction to Pygame](https://www.youtube.com/watch?v=AY9MnQ4x3zk)

Recriou-se o codigo do projeto utilizado como exemplo e acrescentaram-se novas funcionalidades:

* Passagem das classes paras ficheiros próprios (*obstacle.py* e *player.py*)
* Criação de ficheiro para valores de configuração globais (*settings.py*)
* Alterada a música ambiente do jogo pelo tema [Let the Games Begin](https://pixabay.com/music/electronic-let-the-games-begin-21858/)
* Introduzida a funcionalidade de mover o jogador para a esquerda e para a direita (apenas permitia saltar)
* Alteração das imagens utilizadas no jogador
* Alteração/Criação da lógica associada às colisões entre objetos e de limitação de movimentos
* Criação deste ficheiro com comentários (README.md)
* Criação de repositório no github com o código do projeto: [https://github.com/vicentecsena/jump-run](https://github.com/vicentecsena/jump-run)
* Foi utilizado o Visual Studio Code para desenvolver

### Instalação

1. Fazer uma cópia do projeto a partir do github
   `git clone https://github.com/vicentecsena/jump-run`
2. Mover para a diretoria do projeto
   `cd jump-run`
3. Instalar ambiente virtual do python
   `C:\python310\python -m venv venv`
4. Ativar o ambiente virtual
   `venv\scripts\activate`
5. Instalar dependências (pygame)
   `pip install -r requirements.txt`
6. Executar a aplicação
   `python main.py`

