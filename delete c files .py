import os, time
to_delete = r"C:\Users\SRINATH\Desktop\c program\\"
for x in os.listdir(to_delete):
    if x.endswith('.c'):
        print('deleting file:',x)
        os.unlink(to_delete+x)
        time.sleep(2)
        print('file is wiped.')

