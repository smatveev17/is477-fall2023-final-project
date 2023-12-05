rule prepare:
    output:
        "data/wine/Index",
        "data/wine/wine.data",
        "data/wine/wine.names"
    shell:
        "python scripts/prepare_data.py"
rule profile:
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"
rule analyze:
    output:
        "results/summary_statistics.csv",
        "results/classification_report.txt",
        "results/wine_classification_plot.pdf"
    shell:
        "python scripts/analysis.py"