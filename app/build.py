# build.py
import os
import shutil

def build():
    out = "dist"
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    with open(os.path.join(out, "app.txt"), "w") as f:
        f.write("This is a build artifact.\n")
    print("Build complete. Artifact in", out)

if __name__ == "__main__":
    build()
