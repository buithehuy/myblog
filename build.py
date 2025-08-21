import os

# build
os.system("pelican content -o output -s pelicanconf.py")

# serve
print("Serving on http://localhost:8000 ...")
os.system("pelican --listen")
