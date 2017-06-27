import glob
import os
import sys


def delete_files(files):

    print("usuwam: ")
    for file in files:
        print(file)
        os.remove(file)


def list_files(extensions, path="."):

    files = []
    for ftype in extensions:
        for filename in glob.glob(os.path.abspath(path) + '/' + '**/' + ftype, recursive=True):
            if os.path.isfile(filename):
                files.append(filename)
    return files


def print_list(files):

    max_len = len(max(files, key=len))
    total_size = 0
    print('Plik'.ljust(max_len + 3, ' ') + "Rozmiar (b)")
    for filename in files:
        print(filename.ljust(max_len + 3, ' ') + str(os.stat(filename).st_size))
        total_size += os.stat(filename).st_size

    print("\nLiczba plikow: ".ljust(max_len + 3 + 1, ' ') + str(len(files)))
    print("Calkowity rozmiar (b): ".ljust(max_len + 3, ' ') + str(total_size))


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
          "\nlub wprowadz teraz wlasna liste, oddzielajac rozszerzenia spacjami (bez gwiazdek i kropek):")

    custom_extensions = input()

    if custom_extensions == "":
        print("Zostanie uzyta domyslna lista.")
        return default_extensions
    else:
        print("Zostanie uzyta lista uzytkownika.")
        return ["*." + ext for ext in custom_extensions.split()]


def prepare_directories():

    if len(sys.argv) > 1:
        directories = sys.argv
        directories.pop(0)

        result = []

        print("Wybrane katalogi: ")

        for dirct in directories:

            cut_size = 0
            for i in range(len(dirct)-1, -1, -1):
                if dirct[i] == "\\":
                    cut_size += 1
                else:
                    break

            if cut_size > 0:
                dirct = dirct[:-cut_size]

            if not os.path.isdir(dirct):
                print("Blad: \""+dirct+"\" nie jest katalogiem")
                exit(1)
            else:
                result.append(dirct)

        result = list(set(result))
        result.sort()

        for dirct in result:
            print(dirct)

        return result   # delete duplicates from list

    else:
        return ["."]


def create_filelist(directories, extensions):

    files = []
    for directory in directories:
        files += list_files(extensions, directory)

    files = list(set(files))
    files.sort()

    return files


def main():

    directories = prepare_directories()
    extensions = specify_extensions()

    print("Pliki z rozszerzeniami " + ' '.join(extensions) + " zostana usuniete.")

    files = create_filelist(directories, extensions)

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
