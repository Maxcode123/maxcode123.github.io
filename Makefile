install-py-requirements:
	$(PIP) install -r requirements.txt

install-js-requirements:
	npm install tailwindcss

create-css:
	npx tailwindcss -i ./input.css -o ./assets/output.css

build-site:
	cp -r assets output/
	$(INTERPRETER) build.py

run-server:
	$(INTERPRETER) -m http.server --directory output

publish-site:
	ghp-import -b gh-pages output

clean:
	rm -rf output/*
