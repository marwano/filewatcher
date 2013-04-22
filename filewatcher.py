# filewatcher.py - watch paths for any changes in their subdirectories
# Copyright (C) 2013 Marwan Alsabbagh
# license: BSD, see LICENSE for more details.

__version__ = '0.1'

import fnmatch
import os
from os.path import join, getmtime, exists


def list_files(path, include=None, exclude=None):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        filenames = [join(dirpath, i) for i in filenames]
        files.extend(filenames)
    if include:
        files = fnmatch.filter(files, include)
    if exclude:
        files = [i for i in files if not fnmatch.fnmatch(i, exclude)]
    return sorted(files)


def safe_mtime(path, default=None):
    try:
        return getmtime(path)
    except OSError:
        return default


class FileWatcher(object):
    def __init__(self, paths, include=None, exclude=None):
        self.paths = [paths] if isinstance(paths, basestring) else paths
        self.filters = dict(include=include, exclude=exclude)
        self.update()

    def update(self):
        snapshot = []
        for path in self.paths:
            snapshot.extend([(i, safe_mtime(i)) for i in list_files(path, **self.filters)])
        self.snapshot = sorted(snapshot)

    def changed(self):
        last_snapshot = self.snapshot
        self.update()
        return last_snapshot != self.snapshot
