urlreduce
=========

Um encurtador de URL

Esse projeto foi um desafio proposto.

Curti a ideia e resolvi fazer um negocio legalzin

Para a instalação é bem simples.

Primeiro passo fazer um clone do repositorio:

```shell
$ git clone git@github.com:jesuejunior/urlreduce.git
```

```shell
$ cd urlreduce
```

Se estiver usando virtualenv melhor ainda.

Agora temos que isntalar as dependencias que são milhões(brincadeira).

```shell
$ pip install -r requirements.txt
```
e o padrão de app django.

```shell
$ python manager.py syncdb
```

```shell
$ python manager.py runserver
```

Eu prefiro usar o gunicorn, mas essa configue está diretamnete no meu settings_local.py.


Em breve estarei disponibilizando a app em produção falta apenas(tirando o tempo) adicionar no chef pra ele fazer o deploy.


(http://urlresolve.jesuejunior.com)

Vai ficar grande até eu comprar uma url micro...

Qualquer duvida é só falar.

