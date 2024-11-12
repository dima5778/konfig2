import tarfile

# Укажите путь к вашему архиву
tar_path = 'C:/emulator-shell-os/virtual_files.tar'  # Или полный путь, если архив находится в другой папке

# Открываем tar-архив
with tarfile.open(tar_path, 'r') as tar:
    # Выводим все файлы и папки в архиве
    for member in tar.getmembers():
        print(member.name)
