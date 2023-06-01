import os, sys


def requirements():
    print("\nModule installing...")
    modules_to_install = ['scikit-learn', 'pandas', 'numpy', 'seaborn','matplotlib']
    for module in modules_to_install:
        try:
            os.system(f"pip3 install {module}\npython3 -m pip install {module}")
        except:
            continue
    
    print("\nModules are successfully installed.")

if __name__ == "__main__":
    requirements()

