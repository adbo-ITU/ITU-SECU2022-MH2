.PHONY: run
run:
	@python src/player.py

.PHONY: report
report:
	pandoc report.md -o report.pdf
