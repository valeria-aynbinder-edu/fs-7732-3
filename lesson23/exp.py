import os.path
import pickle

if __name__ == '__main__':

    library = None
    if os.path.exists('library.pickle'):
        with open('library.pickle', 'rb') as f:
            library = pickle.load(f)
    else:
        library = Library()

    try:
        # very long code with menus etc
        pass
    except:
        print("error occurred, saving and exiting")
    finally:
        with open('library.pickle', 'wb') as f:
            pickle.dump(library, f)

