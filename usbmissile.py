import launcher.dreamcheeky


def sample_with_context():
    with launcher.dreamcheeky.Launcher() as laucher:
        print(laucher.info())

        laucher.move_up(500)
        laucher.move_down(500)

def sample_without_context():
    try:
        laucher = launcher.dreamcheeky.Launcher()
        print(laucher.info())

        laucher.move_up(500)
        laucher.move_down(500)
    finally:
        laucher.close()

def main():
    sample_with_context()

if __name__ == '__main__':
    main()
