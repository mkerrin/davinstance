import zope.interface
import zope.component

from zope.container.interfaces import IContainer

from zope.filerepresentation.interfaces import IWriteFile
from zope.filerepresentation.interfaces import IFileFactory

import zope.file.file

class FileFactory(object):
    zope.interface.implements(IFileFactory)
    zope.component.adapts(IContainer)

    def __init__(self, container):
        self.container = container

    def __call__(self, name, content_type, data):
        f = zope.file.file.File(mimeType = content_type)
        f.open("w").write(data)

        return f
