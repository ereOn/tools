PROJECT_NAME=$(shell basename ${PWD} )
VIRTUALENV_NAME=.${PROJECT_NAME}

### DO NOT TOUCH ANYTHING BELOW THIS LINE ###

default: develop

clean: clean-develop

# Build

install:
	@echo "Installing ${PROJECT_NAME} system-wide for real use..."
	python setup.py install

develop: env
	@echo "Installing ${PROJECT_NAME} in virtualenv for development..."
	. ${VIRTUALENV_NAME}/bin/activate && python setup.py develop

clean-develop: clean-env
	rm -rf *.egg-info

# Virtual environment
#
env: ${VIRTUALENV_NAME}

${VIRTUALENV_NAME}:
	@echo "No virtualenv exists. Creating one in '${VIRTUALENV_NAME}'..."
	virtualenv ${VIRTUALENV_NAME}

clean-env:
	rm -rf ${VIRTUALENV_NAME}
