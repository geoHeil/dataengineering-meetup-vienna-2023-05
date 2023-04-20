PROJECT_NAME = demeetup
ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

# Need to specify bash in order for conda activate to work.
SHELL=/bin/bash
# Note that the extra activate is needed to ensure that the activate floats env to the front of PATH
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
# https://stackoverflow.com/questions/53382383/makefile-cant-use-conda-activate

## set up python interpreter environment
create_environment: ## create conda environment for analysis
ifeq (True,$(HAS_CONDA))
		@echo ">>> Detected conda, creating conda environment."
		mamba env create --force --name $(PROJECT_NAME) --file environment.yml
		($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dagteam/analytics_project && pip install --editable .)
		($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dagteam/ml_project && pip install --editable .)
		($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dagteam/utils && pip install --editable .)
		($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd hooli-data-eng-pipelines && pip install --editable .)
		# ($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dbt_fal_ml_example && pip install --editable .)
		@echo ">>> New conda env created. Activate with:\nsource activate $(PROJECT_NAME)"
endif


## set up python interpreter environment OSX (apple silicon in case of missing packages)
create_environment_osx: ## create conda environment for analysis
ifeq (True,$(HAS_CONDA))
		@echo ">>> Detected conda, creating conda environment."
		CONDA_SUBDIR=osx-64 mamba env create --force --name $(PROJECT_NAME) --file environment.yml
		($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dagteam/analytics_project && pip install --editable .)
		($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dagteam/ml_project && pip install --editable .)
		($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dagteam/utils && pip install --editable .)
		($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd hooli-data-eng-pipelines && pip install --editable .)
		# ($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dbt_fal_ml_example && pip install --editable .)
		@echo ">>> New conda env created. Activate with:\nsource activate $(PROJECT_NAME)"
endif


## start notebook (jupyter lab)
notebook:
	($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; jupyter lab)


## Case 1: DAG team
case1-dagteam:
	($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dagteam && dagster dev)


## Case 2: DBt + Dagster (conversion of fals example to dagster)
case2-dbt-fal-dagster:
	($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd dbt_fal_ml_example && dagster dev)


## Case 3: Hoolie
case3-hoolie:
	($(CONDA_ACTIVATE) "${PROJECT_NAME}" ; cd hooli-data-eng-pipelines && dagster dev)


#################################################################################
# PROJECT RULES                                                                 #
#################################################################################
#################################################################################
# Self Documenting Commands                                                     #
#################################################################################
.DEFAULT_GOAL := help
# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
