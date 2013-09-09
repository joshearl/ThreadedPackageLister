import sublime
import sublime_plugin
import threading
import os

class ListPackagesCommand(sublime_plugin.WindowCommand):
    def run(self):
        packages_list = self.get_packages_list()
        print packages_list

    def get_packages_list(self):
        package_set = set()
        package_set.update(self._get_packages_from_directory(sublime.packages_path()))

        return sorted(list(package_set))

    def _get_packages_from_directory(self, directory):
        package_list = []
        for package in os.listdir(directory):
            package_list.append(package)
        return package_list