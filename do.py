import os

os.system(f"mkdir docs")

for root, dirs, files in os.walk(os.getcwd()):
    for f in files:
        if f.endswith('.MD') or f.endswith('.md'):
            new_f = f.replace(".MD", ".html")
            new_f = new_f.replace(".md", ".html")
            new_f = new_f.replace("README", "index")

            os.system(f"comrak --gfm --unsafe {f} > docs/{new_f}")

