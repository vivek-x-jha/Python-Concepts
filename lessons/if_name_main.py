print('<This prints regardless>')


def main():
    print(f'{__name__} ran the main function!')


if __name__ == '__main__':
    main()
else:
    print(f'{__name__} ran from import')
