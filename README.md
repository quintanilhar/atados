Atados
======

A ideia é simples: uma rede social na qual pessoas predispostas a praticar o bem
encontram oportunidades de voluntariado.

Nosso principal objetivo é ampliar o senso de comunidade na sociedade, levando
cada vez mais pessoas a entrar nessa corrente de gente boa. Afinal, tudo o que
você faz bem, pode fazer bem a alguém.


Por que colaborar com o projeto?
--------------------------------

Porque você quer viver em uma sociedade melhor!

Porque colaborando com o Atados você estará ajudando todas as causas! Sejam
elas lutar pelo direito dos animais, pelo meio ambiente, por educação de
qualidade, por mais respeito aos direitos humanos entre outras. Isso mesmo!
Você vai contribuir com o trabalho de diversas ONGs que juntas apoiam todas as
causas!

Já que você está aqui, provavelmente você é alguém envolvido com tecnologia.
Suas habilidades são muito valiosas para a sociedade. Colaborar com o Atados é
uma forma de contribuir para o desenvolvimento coletivo fazendo algo que você
faz muito bem!


Quero colaborar!
----------------

Você pode entrar em contato com <contato@atados.com.br> para nos contar um
pouco mais sobre você, e como você gostaria de ajudar, ou então:

 * [Reportar bugs](https://github.com/atados/atados/issues/new).
 * Formatar o código de acordo com a [PEP8](http://www.python.org/dev/peps/pep-0008/).
 * Enviar testes unitários.
 * Resolver [nossos bugs](https://github.com/atados/atados/issues). Recomendamos que você comece por [bugs que marcamos como "bons para começar"](https://github.com/atados/atados/issues?labels=good+first+bug&page=1&state=open).

Pré-requisitos
--------------
    [python-pip](https://pypi.python.org/pypi/pip) instalado.
    [python-mysqldb](http://sourceforge.net/projects/mysql-python) instalado.

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
