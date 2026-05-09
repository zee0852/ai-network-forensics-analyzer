import pandas as pd

df = pd.read_parquet("UNSW_NB15_training-set.parquet")

# label = 1 means attack traffic
attack_df = df[df["label"] == 1]

selected_columns = [
    "dur", "proto", "service", "state",
    "spkts", "dpkts", "sbytes", "dbytes",
    "rate", "sload", "dload",
    "ct_src_dport_ltm", "ct_dst_sport_ltm",
    "is_ftp_login", "ct_ftp_cmd", "ct_flw_http_mthd",
    "attack_cat", "label"
]

attack_sample = attack_df[selected_columns].head(1000)

attack_sample.to_csv("unsw_attack_sample.csv", index=False)

print("Export complete. 1000 attack traffic records saved as unsw_attack_sample.csv")
print("Attack categories in sample:")
print(attack_sample["attack_cat"].value_counts())