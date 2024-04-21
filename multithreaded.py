import re
from collections import defaultdict
from threading import Thread

KEYWORDS = ["python", "programming", "threads", "processes"]


def find_keywords_in_file(file_path, keywords, results):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().lower()
            for keyword in keywords:
                if re.search(keyword, content):
                    results[keyword].append(file_path)
    except FileNotFoundError as e:
        print(f"File not found: {file_path}. Error: {e}")
    except Exception as e:
        print(f"An error occurred while processing file: {file_path}. Error: {e}")


def multithreaded_file_processing(files, keywords):
    try:
        results = defaultdict(list)
        threads = []

        for file in files:
            thread = Thread(
                target=find_keywords_in_file, args=(file, keywords, results)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return dict(results)
    except Exception as e:
        print(f"An error occurred while processing. Error: {e}")


if __name__ == "__main__":
    try:
        files = [f"file{i}.txt" for i in range(1, 4)]

        print("Багатопотоковий підхід:")
        import time

        start_time = time.time()
        multithreaded_results = multithreaded_file_processing(files, KEYWORDS)
        end_time = time.time()
        print("Час виконання:", end_time - start_time, "секунд")
        print(multithreaded_results)
    except Exception as e:
        print(f"Error: {e}")
