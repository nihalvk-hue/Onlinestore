import os
from django.core.files.storage import FileSystemStorage
from django.core.files import locks

# Override the _save method to bypass file locking
class NoLockingStorage(FileSystemStorage):
    def _save(self, name, content):
        full_path = self.path(name)
        
        directory = os.path.dirname(full_path)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except FileExistsError:
                pass
        
        if self.file_permissions_mode is not None:
            old_umask = os.umask(0o777 & ~self.file_permissions_mode)
        
        try:
            # Don't use locks.lock() here - that's the key change
            with open(full_path, 'wb') as f:
                for chunk in content.chunks():
                    f.write(chunk)
        finally:
            if self.file_permissions_mode is not None:
                os.umask(old_umask)
        
        return name