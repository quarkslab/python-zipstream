# -*- coding: utf-8 -*-
import os
import enczipstream
import zipfile


with enczipstream.ZipFile(mode='w', compression=enczipstream.ZIP_DEFLATED,
                          pwd=b"password") as z:
    z.write('LICENSE')
    z.write('LICENSE', arcname='stuff/LICENSE')

    with open('tests/sample.rtf', 'rb') as fp:
        z.writestr('sample.rtf', fp.read())

    for root, directories, files in os.walk('zipstream'):
        for filename in files:
            path = os.path.join(root, filename)
            z.write(path, path)

    with open('test.zip', 'wb') as f:
        for chunk in z:
            f.write(chunk)


with zipfile.ZipFile('test.zip') as z:
    z.setpassword(b"password")
    z.testzip()
