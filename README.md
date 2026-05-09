<<<<<<< HEAD
# AI-Assisted Network Forensics Analyzer

## Project Overview

This project compares traditional manual network forensic inspection against an AI-assisted automated network forensics triage workflow using the UNSW-NB15 intrusion detection dataset.

The objective of the project was to evaluate whether Python automation and local large language models (LLMs) can reduce the repetitive workload involved in early-stage forensic traffic analysis while still producing useful investigative findings.

The project was developed as part of a cybersecurity network forensics research assessment.

---

# Research Workflow

## Stage 1 — Dataset Preparation

The original UNSW-NB15 training dataset was provided in Parquet format.

A Python preprocessing script was used to:

- load the dataset
- isolate malicious traffic (`label = 1`)
- select relevant forensic traffic features
- export suspicious records into CSV format

Generated file:

```text
unsw_attack_sample.csv
```

---

## Stage 2 — Traditional Manual Inspection

The exported CSV traffic sample was manually inspected to identify:

- attack category distribution
- protocol diversity
- service behaviour
- connection state behaviour
- suspicious traffic observations

This simulated a conventional network forensic workflow where an analyst manually reviews suspicious traffic evidence and prepares written findings.

Generated file:

```text
manual_inspection_report.md
```

---

## Stage 3 — AI-Assisted Automated Analysis

A Python forensic analyzer was developed to:

- ingest the suspicious traffic CSV
- calculate forensic distributions
- generate traffic statistics
- build a structured evidence summary
- send the evidence to a local LLM through Ollama
- automatically generate an investigator-style forensic report

The local model used was:

```text
mistral:7b
```

Generated output:

```text
forensic_report.txt
```

---

# Comparative Goal

The project compares:

| Traditional Workflow | AI-Assisted Workflow |
|---|---|
| Manual evidence inspection | Automated evidence extraction |
| Manual report writing | AI-generated forensic report |
| High analyst workload | Reduced analyst workload |
| Slower triage speed | Faster triage speed |

---

# Technologies Used

- Python
- Pandas
- Ollama
- Mistral 7B
- Parquet dataset processing
- CSV traffic analysis
- Local LLM inference

---

# Project Structure

```text
project-1-ai-network-forensics-analyzer/
│
├── screenshots/
├── export_unsw_sample.py
├── UNSW_NB15_training-set.parquet
├── unsw_attack_sample.csv
├── manual_inspection_report.md
├── network_forensics_analyzer.py
├── forensic_report.txt
├── comparison_report.md
├── methodology_flowchart.png
├── README.md
└── final_report.pdf
```

---

# Key Finding

The experiment demonstrated that traditional packet inspection remains valuable for human validation, but AI-assisted automated triage significantly reduces repetitive forensic workload and accelerates initial investigative reporting.

---

# Status

Completed as part of the Network Forensics Automation / AI Security Engineering Lab.
=======
# ai-network-forensics-analyzer
AI-assisted network forensics automation project using Python, UNSW-NB15 dataset, and local LLM forensic triage workflows.
>>>>>>> 02ca1b289546db6d952aba22c37ce7e93faedf4f
