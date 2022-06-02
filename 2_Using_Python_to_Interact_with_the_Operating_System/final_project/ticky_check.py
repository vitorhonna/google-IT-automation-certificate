import re
import csv

error_messages = [
    "Timeout while retrieving information",
    "The ticket was modified while updating",
    "Connection to DB failed",
    "Tried to add information to a closed ticket",
    "Permission denied while closing ticket",
    "Ticket doesn't exist",
]

errors_freq = {}
usage = {}

with open("syslog.log") as fh:
    for line in fh:

        log_entry = re.findall(r"ticky: (ERROR|INFO):? (.*) \((.*)\)", line)
        # Return a list of tuples with the format:
        # [("ERROR", "The ticket was modified while updating", "err2")]
        # [("ERROR", "Connection to DB failed", "err3")]

        # Ignore uninteresting lines
        if not log_entry:
            continue

        # Unpack the search result
        entry_type, message, user = log_entry[0]

        # Parse ERRORs
        if entry_type == "ERROR":
            # Create an error ID using the error message
            error_id = message
            # Count the frequency of occurences of each type of error
            errors_freq[error_id] = errors_freq.get(error_id, 0) + 1

        # Count the usage for each user (get the usage statistics)
        if user in usage:
            usage[user][entry_type] = usage[user].get(entry_type, 0) + 1
        else:
            if entry_type == "ERROR":
                usage[user] = {"Username": user, "INFO": 0, "ERROR": 1}
            else:
                usage[user] = {"Username": user, "INFO": 1, "ERROR": 0}


# Sort the errors by the most common error to the least common error
errors_freq_sorted = sorted(
    errors_freq.items(), reverse=True, key=lambda x: x[1])
# Sort the usage by username
usage_sorted = sorted(usage.items())

errors_freq_sorted_dicts = []
for error, count in errors_freq_sorted:
    errors_freq_sorted_dicts.append({"Error": error, "Count": count})

usage_sorted_dicts = []
for username, user_usage in usage_sorted:
    usage_sorted_dicts.append(user_usage)

# Export data in CSV:
with open("error_message.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Error", "Count"])
    writer.writeheader()
    writer.writerows(errors_freq_sorted_dicts)

with open("user_statistics.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Username", "INFO", "ERROR"])
    writer.writeheader()
    writer.writerows(usage_sorted_dicts)
