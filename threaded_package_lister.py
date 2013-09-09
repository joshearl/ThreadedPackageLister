import sublime
import sublime_plugin
import threading
import os

class ListPackagesCommand(sublime_plugin.WindowCommand):
    def run(self):
        threaded_package_lister = ThreadedPackageLister()
        print "Starting thread ..."
        threaded_package_lister.start()

        print "Setting thread handler on main thread ..."
        self.handle_thread(threaded_package_lister)

    def handle_thread(self, thread):
        if thread.is_alive():
            print "Thread is still running ..."
            sublime.set_timeout(lambda: self.handle_thread(thread), 20)
            return

        packages_list = thread.result
        print "Thread is finished."
        print packages_list

class ThreadedPackageLister(threading.Thread):
    def __init__(self):
        self.result = None
        threading.Thread.__init__(self)

    def run(self):
        print "Starting work on background thread ..."
        self.result = self.get_packages_list()
    
    def get_packages_list(self):
        package_set = set()
        package_set.update(self._get_packages_from_directory(sublime.packages_path()))

        return sorted(list(package_set))

    def _get_packages_from_directory(self, directory):
        package_list = []
        for package in os.listdir(directory):
            package_list.append(package)
        print "Package list retrieved ..."
        return package_list