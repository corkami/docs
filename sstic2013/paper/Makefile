MASTER=_master
FINALPDF=sstic-actes.pdf
SRC=$(MASTER).tex $(wildcard */*.tex)
LATEX=pdflatex
LFLAGS=-halt-on-error

BIB_MISSING = 'No file.*\.bbl|Citation.*undefined'
REFERENCE_UNDEFINED='(There were undefined references|Rerun to get (cross-references|the bars) right)'

$(FINALPDF): $(SRC)
	$(LATEX) $(LFLAGS) $(MASTER).tex
	make $(MASTER).bbl
	make full
	mv $(MASTER).pdf $(FINALPDF)

full: $(MASTER).ind
	$(LATEX) $(LFLAGS) $(MASTER).tex
	-grep --color 'Warning.*' $(MASTER).log
	@grep -Eqc $(BIB_MISSING) $(MASTER).log && $(LATEX) $(MASTER).tex > /dev/null ; true
	@grep -Eqc $(REFERENCE_UNDEFINED) $(MASTER).log && $(LATEX) $(MASTER).tex > /dev/null; true

%.bbl:
	bibtex $(MASTER)
	$(LATEX) $(LFLAGS) $(MASTER).tex

%.ind:
	makeindex $(MASTER)

README: $(SRC)
	@awk  '/^%% / { print substr($$0, 4)}' $(SRC) > $@

.PHONY: snapshot clean
snapshot: $(FINALPDF)
	mv $(FINALPDF) "$(FINALPDF:.pdf=-$(shell git rev-parse HEAD').pdf)"

clean:
	rm -f *.aux *.bbl *.blg *.dvi *.log *.ps *.lof *.toc *.glg *.gls
	rm -f *.ilg *.nlo *.nav *.snm *.glo *.glsmake *.ist *.out *.vrb *.lot *.idx *.ind
	rm -f $(MASTER).pdf $(FINALPDF)
