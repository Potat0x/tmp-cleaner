import glob
import os
import sys


def delete_files(files):

    print("usuwam: ")
    for file in files:
        print(file)


def list_files(extensions, path="."):

    files = []
    for ftype in extensions:
        for filename in glob.glob(os.path.abspath(path) + '/' + '**/' + ftype, recursive=True):
            if os.path.isfile(filename):
                files.append(filename)
    return files


def print_list(files):

    max_len = len(max(files, key=len))
    print('Plik'.ljust(max_len + 3, ' ') + "Rozmiar (b)")
    for filename in files:
        print(filename.ljust(max_len + 3, ' ') + str(os.stat(filename).st_size))


def confirm():

    while True:
        print('Usunac? tak/nie')
        decision = input()

        if decision == 'tak':
            return True
        elif decision == 'nie':
            return False


def delete(files):

    confirming_answer = "usun"
    print(str(len(files)) + " plikow zostanie usunietych wpisz \"" + confirming_answer + "\"")

    if confirming_answer == input():
        delete_files(files)
        print("\npliki zostaly usuniete.")
    else:
        print("Pliki nie zostaly usuniete.")


def specify_extensions():

    default_extensions = ['*.o', '*.obj', '*.class', '*.out']   # EXTENSIONS LIST

    print("Domyslna lista rozszerzen (enter, aby uzyc): " + ' '.join(default_extensions) +
          "\nlub wprowadz teraz własną liste, oddzielajac rozszerzenia spacjami (bez gwiazdek i kropek):")

    custom_extensions = input()

    if custom_extensions == "":
        print("Zostanie uzyta domyslna lista.")
        return default_extensions
    else:
        print("Zostanie uzyta lista użytkownika.")
        return ["*." + ext for ext in custom_extensions.split()]


def prepare_directories():

    if len(sys.argv) > 1:
        directories = sys.argv
        directories[0] = "."    # delete program name from directories list and add default . directory
        print(directories)

        for dirct in directories:
            if not os.path.isdir(dirct):
                print("\""+dirct+"\" nie jest katalogiem")
                exit(1)

        return list(set(directories))   # delete duplicates from list

    else:
        return ["."]


def main():

    directories = prepare_directories()

    extensions = specify_extensions()

    print("Pliki z rozszerzeniami " + ' '.join(extensions) + " zostana usuniete.")

    files = []

    for directory in directories:
        files += list_files(extensions, directory)

    if len(files) != 0:
        print_list(files)

        if confirm():
            delete(files)
        else:
            print("Zadne pliki nie zostaly usuniete.")
    else:
        print("Nie znaleziono pasujacych plikow.")


if __name__ == "__main__":
    main()
