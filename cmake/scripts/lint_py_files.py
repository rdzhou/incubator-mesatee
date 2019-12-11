'''
Use pylint to lint all *.py files in the current git repository.
'''
import os
import subprocess

# for each py_file, pylint
def get_py_files():
    """Find *.py files in the current git repository"""
    cmd = "git ls-files '*.py'"
    output = subprocess.check_output(cmd, shell=True).decode('utf-8')
    files = output.strip().split('\n')
    print(files)
    return files

def lint(files):
    for fl in files:
        cmd = 'pylint --rcfile=cmake/scripts/pylintrc {}'.format(fl)
        print('[PYLINT]', cmd)
        # os.system(cmd)

def get_repo_root():
    """Return root of the git repository"""
    cmd = 'git rev-parse --show-toplevel'
    return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()

def main():
    os.chdir(get_repo_root())
    files = get_py_files()
    lint(files)

if __name__ == "__main__":
    main()