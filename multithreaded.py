import re
from threading import Thread


KEYWORDS = ["python", "programming", "threads", "processes"]


def find_keywords_in_file(file_path, keywords, results):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().lower()
        for keyword in keywords:
            if re.search(keyword, content):
                results[keyword].append(file_path)


def multithreaded_file_processing(files, keywords):

    results = []
    threads = []

    for file in files:
        thread = Thread(target=find_keywords_in_file, args=(file, keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


if __name__ == "__main__":

    files = [f"file{i}.txt" for i in range(1, 4)]

    print("Багатопотоковий підхід:")
    import time

    start_time = time.time()
    multithreaded_results = multithreaded_file_processing(files, KEYWORDS)
    end_time = time.time()
    print("Час виконання:", end_time - start_time, "секунд")
    print(multithreaded_results)
