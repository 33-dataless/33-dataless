from parser.parser import build_readme

def main():
    try:
        readme = build_readme()
    finally:
        with open('readme.md', 'w', encoding='utf-8') as file:
            file.write(readme)

if __name__ == '__main__':
    main()

