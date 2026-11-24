import os

def log_message(message):
    log_file_path = os.path.join(os.getcwd(), "log.txt")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{message}\n")
    print(f"Log written: {message}")

# Test logging
log_message("Test log entry: Logging functionality is working.")
