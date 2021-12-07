import os


def make_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


folder_structure = ('my_project', ('settings', 'mainapp', 'adminapp', 'authapp'))

for i, name in enumerate(folder_structure):
    if isinstance(name, tuple):
        for f_name in name:
            make_folder(os.path.join(folder_structure[i - 1], f_name))
