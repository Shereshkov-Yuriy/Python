import os
import shutil


def make_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


folder_out = 'templates_7_3'
make_folder(folder_out)
folder_in = r'my_project'
files_founds = []
for root, dir, file in os.walk(folder_in):
    for f in file:
        if '.html' in f:
            files_founds.append(os.path.join(root, f))
for path in files_founds:
    folder_in = os.path.join(folder_out, os.path.basename(os.path.dirname(path)))
    make_folder(folder_in)
    shutil.copy(path, os.path.join(folder_in, os.path.basename(path)))
