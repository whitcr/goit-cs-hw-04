import re
from multiprocessing import Process, Manager


KEYWORDS = ["python", "programming", "threads", "processes"]


def find_keywords_in_file(file_path, keywords, results):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().lower()
        for keyword in keywords:
            if re.search(keyword, content):
                results[keyword].append(file_path)


def multiprocessing_file_processing(files, keywords):

    manager = Manager()
    results = {keyword: manager.list() for keyword in keywords}
    processes = []

    for file in files:
        process = Process(target=find_keywords_in_file, args=(file, keywords, results))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results_dict = {
        keyword: list(file_paths) for keyword, file_paths in results.items()
    }

    return results_dict


if __name__ == "__main__":

    files = [f"file{i}.txt" for i in range(1, 4)]

    print("Багатопроцесорний підхід:")
    import time

    start_time = time.time()
    multiprocessing_results = multiprocessing_file_processing(files, KEYWORDS)
    end_time = time.time()
    print("Час виконання:", end_time - start_time, "секунд")
    print(multiprocessing_results)
