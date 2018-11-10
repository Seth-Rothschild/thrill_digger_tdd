all:
	@echo "\t\`make test\` to run tests"
	@echo "\t\`make dev\` to install development version"
	@echo "\t\`make lint\` to run static typing tests"

dev :
	@conda create --name thrill_digger_tdd_shell
	@conda activate thrill_digger_tdd_shell 
	@pip install -e .
	@deactivate
	@echo "installed development version; run \`conda activate thrill_digger_tdd_shell\` to enter activated environment."

test:
	@conda activate thrill_digger_tdd_shell
	@pytest --cov-report term-missing --cov=thrill_digger_tdd tests/
	@deactivate


lint :
	@conda activate thrill_digger_tdd_shell
	@echo "======== PYLINT ======="
	@pylint --rcfile=.pylintrc thrill_digger_tdd -f parseable -r n
	@echo "======== MYPY ======="
	@mypy --ignore-missing-imports --follow-imports=skip thrill_digger_tdd
	@echo "======== PYCODESTYLE ======="
	@pycodestyle thrill_digger_tdd --max-line-length=120
	@echo "======== PYDOCSTYLE  ======="
	@pydocstyle thrill_digger_tdd
	@deactivate

remove:
	@echo "removing virtual environment..."
	@conda remove --name thrill_digger_tdd_shell --all


