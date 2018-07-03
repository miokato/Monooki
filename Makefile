PARAM:=-la

.PHONY: deploy
deploy:
	git push heroku master

.PHONY: push
push:
	git push origin master

.PHONY: static
static:
	python manage.py collectstatic --noinput

.PHONY: show
show:
	ls $(PARAM)
