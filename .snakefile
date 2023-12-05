rule prepare:
    output:
        "lab6/output1.txt",
        "lab6/output2.txt"
    shell:
        "python lab6/step1.py"
rule profile:
    output:
        "lab6/output3.txt"
    shell:
        "python lab6/step2.py"
rule analyze:
    input:
        "lab6/output1.txt",
        "lab6/output2.txt",
        "lab6/output3.txt"
output:
    "lab6/output4.txt"
shell:
    "python lab6/step3.py"