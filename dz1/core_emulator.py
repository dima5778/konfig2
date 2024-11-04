import os
import tarfile
import xml.etree.ElementTree as ET
from datetime import datetime
import time

class ShellEmulator:
    def __init__(self, config_path):
        self.config_path = config_path
        self.current_dir = "/"
        self.load_config()

    def load_config(self):
        tree = ET.parse(self.config_path)
        root = tree.getroot()
        self.archive_path = root.find('archivePath').text
        self.start_script = root.find('startScript').text
        self.init_virtual_fs()

    def init_virtual_fs(self):
        with tarfile.open(self.archive_path, 'r') as archive:
            archive.extractall('/tmp/virtual_fs')
    
    def ls(self):
        return os.listdir('/tmp/virtual_fs' + self.current_dir)

    def cd(self, path):
        if path == "..":
            self.current_dir = os.path.dirname(self.current_dir)
        else:
            self.current_dir = os.path.join(self.current_dir, path)

    def exit(self):
        return "exit"

    def cal(self):
        return datetime.now().strftime("%B %Y")

    def uptime(self):
        return time.time() - os.stat('/proc/1').st_ctime  # Время с запуска системы

    def find(self, filename):
        results = []
        for root, dirs, files in os.walk('/tmp/virtual_fs'):
            if filename in files:
                results.append(os.path.join(root, filename))
        return results
