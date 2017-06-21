# usage:
# 
# gxpc make -j 50 MATRIX=data/sample/matrix SYSL=data/sample/systems -- -a cpu_factor=0.25 -a state_dir=$HOME/public_html/gxpstatus/randtukeyhsd


####################################### set these
SYSL :=
MATRIX :=
NTRIAL := 1000
#######################################

USERNAME := $(shell whoami)
TMP_DIR := $(dir $(MATRIX))randtukeyhsd-work

NICE_VALUE := 19
NICE := nice -n $(NICE_VALUE)
PYTHON := python3
NPYTHON := $(NICE) $(PYTHON)
AWK := $(NICE) gawk

MINMAX_PREFIX := $(TMP_DIR)/minmax.
MINMAX := $(shell $(AWK) 'BEGIN{for (i = 1; i <= $(NTRIAL); i++){ printf("$(MINMAX_PREFIX)%d ", i); }}')
MINMAX_ALL := $(dir $(MATRIX))minmax-all
PVALUES := $(MATRIX).pvalues

default: pvalues

pvalues: $(PVALUES)

clean:
	rm -r $(TMP_DIR)

$(PVALUES): $(MINMAX_ALL) $(SYSL)
	$(NPYTHON) calc_pvalues.py $(MATRIX) $(MINMAX_ALL) $(SYSL) > $@

$(MINMAX_ALL): $(MINMAX)
	cat $(MINMAX_PREFIX)* > $@

$(MINMAX): $(MATRIX)
	mkdir -p $(dir $@) && $(NPYTHON) permutation.py $(MATRIX) $@ --seed-by-name
