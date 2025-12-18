from collections import Counter

def analyze_log_file(log_file_path):
    ip_counter = Counter()
    page_counter = Counter()
    error_404_count = 0

    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 9:
                continue  # Skip malformed lines

            ip = parts[0]
            status_code = parts[8]
            page = parts[6]

            ip_counter[ip] += 1
            page_counter[page] += 1

            if status_code == '404':
                error_404_count += 1

    print("Log File Analysis Report")
    print("------------------------")
    print(f"Total 404 Errors: {error_404_count}")
    print(f"Most Requested Page: {page_counter.most_common(1)[0]}")
    print(f"Top IP Address: {ip_counter.most_common(1)[0]}")

if __name__ == "__main__":
    analyze_log_file("access.log")
