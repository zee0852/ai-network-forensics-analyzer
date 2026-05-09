# Comparative Evaluation Report

## Project Overview

This project compared traditional manual network forensic inspection against an AI-assisted automated network forensics triage workflow using suspicious traffic records extracted from the UNSW-NB15 intrusion detection dataset.

Both workflows used the same 1000-record malicious traffic sample in order to compare analyst workload, reporting speed, evidence extraction, and investigative consistency.

---

# Workflow Comparison

## Method A — Traditional Manual Inspection

The traditional workflow required the analyst to manually inspect the exported CSV traffic sample and identify suspicious patterns by reviewing:

- attack category distribution
- protocol behaviour
- service usage
- connection states
- packet and byte statistics

The analyst then manually prepared written findings based on the observed traffic behaviour.

This method provided detailed human interpretation but required repeated counting, comparison, observation, and written summarisation.

Generated output:

```text
manual_inspection_report.md