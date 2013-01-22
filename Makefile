clean:
	@find . -name "*.pyc" -delete

development:
	@pip install -r requirements/development

environment:
	@pip install -r requirements/environment

pep8:
	@pep8 --exclude 'migrations' .
	
sass:
	@sass --style compressed --watch atados/atados/sass:atados/atados/static/css
