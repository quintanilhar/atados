Atados
======

O Atados é uma rede social que possibilita às pessoas encontrar de maneira
fácil as mais diversas oportunidades de voluntariado. Os usuários podem
compartilhar atividades e experiências e estimular seus amigos a participar de
ações voluntárias.

Nosso principal objetivo é ampliar o senso de comunidade na sociedade, levando
cada vez mais pessoas a entrar nessa corrente de gente boa. Afinal, tudo o que
você faz bem, pode fazer bem a alguém.


Como participar
---------------

Seguem algumas maneiras de colaborar com o projeto:

 * [Reportar bugs](https://github.com/atados/atados/issues/new).
 * Formatar o código de acordo com a [PEP8](http://www.python.org/dev/peps/pep-0008/).
 * Enviar testes unitários.
 * Resolver [nossos bugs](https://github.com/atados/atados/issues). Recomendamos que você comece por [bugs que marcamos como "bons para começar"](https://github.com/atados/atados/issues?labels=good+first+bug&page=1&state=open).


Como rodar o projeto
--------------------

    git clone git@github.com:atados/atados.git
    cd atados
    pip install -r requirements/environment
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver


Licença
-------

Apache License, Version 2.0
