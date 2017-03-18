import launcher.dreamcheeky

def main():
    laucher = launcher.dreamcheeky.Launcher()

    print(laucher.info())

    laucher.move_up(500)
    laucher.move_down(500)

if __name__ == '__main__':
    main()
