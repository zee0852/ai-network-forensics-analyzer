import pandas as pd
import subprocess
from datetime import datetime
import re

print("Loading UNSW attack traffic sample...")

df = pd.read_csv("unsw_attack_sample.csv")

# Basic forensic statistics
total_records = len(df)
attack_distribution = df["attack_cat"].value_counts()
protocol_distribution = df["proto"].value_counts()
service_distribution = df["service"].value_counts()
state_distribution = df["state"].value_counts()

avg_spkts = round(df["spkts"].mean(), 2)
avg_dpkts = round(df["dpkts"].mean(), 2)
avg_sbytes = round(df["sbytes"].mean(), 2)
avg_dbytes = round(df["dbytes"].mean(), 2)

# Build evidence summary for AI
evidence = f"""
Total suspicious records analysed: {total_records}

Attack category distribution:
{attack_distribution.to_string()}

Protocol distribution:
{protocol_distribution.to_string()}

Service distribution:
{service_distribution.to_string()}

Connection state distribution:
{state_distribution.to_string()}

Average source packets: {avg_spkts}
Average destination packets: {avg_dpkts}
Average source bytes: {avg_sbytes}
Average destination bytes: {avg_dbytes}
"""

print("Traffic evidence extracted.")
print("Contacting local AI forensic analyst...")

prompt = f"""
Act as a professional network forensic investigator.

Based on the following suspicious network traffic evidence from the UNSW-NB15 intrusion dataset, provide:

1. Summary of suspicious findings
2. Likely attack behaviour present
3. Severity assessment
4. Why this traffic would require forensic attention
5. Recommended investigative actions

Network Evidence:
{evidence}
"""

result = subprocess.run(
    ["ollama", "run", "mistral:7b"],
    input=prompt,
    text=True,
    capture_output=True,
    encoding="utf-8"
)

ai_report = re.sub(r'\x1b\[[0-9;?]*[A-Za-z]', '', result.stdout)

# Save report
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("forensic_report.txt", "w", encoding="utf-8") as file:
    file.write("=== AI AUTOMATED NETWORK FORENSICS REPORT ===\n")
    file.write(f"Generated: {timestamp}\n\n")
    file.write("=== EXTRACTED TRAFFIC EVIDENCE ===\n")
    file.write(evidence)
    file.write("\n\n=== AI FORENSIC ANALYSIS ===\n")
    file.write(ai_report)

print("AI forensic report generated successfully.")
print("Saved as forensic_report.txt")