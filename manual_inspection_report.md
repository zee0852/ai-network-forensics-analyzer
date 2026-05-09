## Manual Findings

The selected sample contained 1000 malicious traffic records extracted from the UNSW-NB15 dataset.

Attack category distribution:

- Fuzzers: 635 records
- Backdoor: 242 records
- Analysis: 105 records
- Reconnaissance: 15 records
- Shellcode: 3 records

The dominant category within the sample was Fuzzers activity. This type of traffic is commonly associated with vulnerability discovery attempts where attackers send malformed or unexpected inputs to test system behaviour and identify weaknesses.

A significant number of Backdoor records were also identified, which may indicate attempts to establish unauthorized remote access or persistence mechanisms within a target environment. The Analysis category suggests probing or investigative behaviour against systems before exploitation attempts occur.

The protocol distribution showed that TCP traffic represented the largest proportion of suspicious records, followed by UDP and several uncommon protocol types. The presence of a wide range of unusual protocols may indicate attempts to evade standard monitoring or generate abnormal traffic patterns.

Most records were associated with unidentified services, while a smaller number involved FTP and HTTP services. This suggests that much of the malicious traffic did not map cleanly to common application-layer services.

The connection state distribution showed a high number of INT states compared with FIN states. This indicates that many connections were interrupted or not completed normally, which may reflect unstable or intentionally abnormal communication attempts during malicious activity.

Average packet and byte statistics also showed higher source-side activity compared with destination responses, which is consistent with aggressive outbound probing or attack-oriented traffic behaviour.