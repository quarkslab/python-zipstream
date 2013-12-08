import os
import zipstream
import zipfile


f = open('test.zip', 'wb')

with zipstream.ZipFile(mode='w', compression=zipstream.ZIP_DEFLATED) as z:
    z.write('LICENSE')
    z.write('LICENSE', arcname='stuff/LICENSE')

    for root, directories, files in os.walk('zipstream'):
        for filename in files:
            path = os.path.join(root, filename)
            z.write(path, path)

    with open('test.zip', 'wb') as f:
        for chunk in z:
            f.write(chunk)

f.close()


with zipfile.ZipFile('test.zip') as z:
    z.testzip()
