import glob

from valamis.exceptions import InvalidFilenameError


class UrlFixer:
    # replace all string starting with a single or double quote and keywords
    @staticmethod
    def combine_with_prefix(replacements: list, data: str) -> str:
        for orig, prefix in replacements:
            # skip lines with the word @expose
            newdata = ""
            for line in data.splitlines(True):
                if "@expose" not in line:
                    # replace all occurrences of the required string but skip lines with @expose word
                    line = line.replace(f"'/{orig}/", f"'/{prefix}/{orig}/")
                    line = line.replace(f"`/{orig}/", f"`/{prefix}/{orig}/")
                    line = line.replace(f'"/{orig}/', f'"/{prefix}/{orig}/')
                newdata += line
            data = newdata
        return data

    @staticmethod
    def replace_keyword(replacements: list, data: str) -> str:
        for orig, dest in replacements:
            data = data.replace(orig, dest)
        return data

    @staticmethod
    def find_files(path: str, ext: str) -> list:
        if not ext.startswith('.'):
            raise InvalidFilenameError("extension must be start wit a dot")
        if not path.endswith('/'):
            raise InvalidFilenameError("path must be ended with a slash")
        return glob.glob(f'{path}**/*{ext}', recursive=True)

    @staticmethod
    def simple_replace(replacements: list, path: str, ext: str) -> None:
        UrlFixer._run(replacements, path, ext, UrlFixer.replace_keyword)

    @staticmethod
    # Wrap the string with slashes and add double, single quoutes or
    # tick to the beginning of the string for searching
    def smart_replace(replacements: list, path: str, ext: str) -> None:
        UrlFixer._run(replacements, path, ext, UrlFixer.combine_with_prefix)

    @staticmethod
    def _run(replacements: list, path: str, ext: str, func) -> None:
        for filename in UrlFixer.find_files(path, ext):
            fin = open(filename, "rt")
            content = fin.read()
            new_content = func(replacements, content)
            fin.close()
            if content == new_content:
                continue
            print(f'Writing new content to the file: {filename}')
            fin = open(filename, "wt")
            fin.write(new_content)
            fin.close()
