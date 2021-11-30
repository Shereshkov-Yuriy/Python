import os

folder = 'some_data'
size_files = [os.stat(item).st_size for item in os.scandir(folder)]
max_len = len(str(max(size_files)))
min_len = len(str(min(size_files)))
stat_dict = {10 ** x: 0 for x in range(min_len, max_len + 1)}
for key, val in stat_dict.items():
    for item in os.scandir(folder):
        if key / 10 < item.stat().st_size < key:
            stat_dict[key] += 1
print(stat_dict)
