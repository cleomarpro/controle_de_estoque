DESCRIÇÃO
O sistem fáz todo o controle do estoque dês  da criação do produto até a baixa em estoque

INSTRUÇÕES PARA O DEPLOY

1 - Baixar o repositório do GitHaub (git remote add origin URLdeOrigem)
2 - Entrar em uma branch (git checkout nome_da_branch)
3 - Criar uma virtualenv (Linux:  python3 -m  venv  nome da venv.   Windous: python -m venv myvenv (criar virtula enve na mesma pasta do projeto)
4 - Ativar a virtualenv (Linux: source NomeDaVenv/bin/activate.)
5 - Atualizar o pip (python -m pip install --upgrade pip)
6 - Instalar os requirements.txt(pip install -r requirements.txt)
7 - Fazer as migrações {python manage.py migrate}
8 - Criar um super usuario(python manage.py createsuperuser)
9 - Ligar o servidor (python manage.py runserver)
9.1 Acesse no seu navegador http://127.0.0.1:8000/admin 

INSTRUÇÕES DE USO DA API

