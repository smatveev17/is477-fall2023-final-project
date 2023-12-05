rule prepare:
    output:
        "data/wine/Index",
        "data/wine/wine.data",
        "data/wine/wine.names"
    shell:
        "python scripts/prepare_data.py"
rule profile:
    input:
        "data/wine/wine.data"
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"
rule analyze:
    input:
        "data/wine/wine.data"
    output:
        "results/summary_statistics.csv",
        "results/classification_report.txt",
        "results/wine_classification_plot.pdf"
    shell:
        "python scripts/analysis.py"

rule run_all:
    input:
        "profiling/report.html",
        "results/summary_statistics.csv",
        "results/classification_report.txt",
        "results/wine_classification_plot.pdf"