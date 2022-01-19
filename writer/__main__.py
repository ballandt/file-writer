import argparse
import cmd
import os

desc = """Simple command line code writer for python
Version 0.6
Syntax:

- indents after `:` sign.
- dedents 4 spaces if an empty line is inserted.
- saves if three empty lines are inserted.
"""

parser = argparse.ArgumentParser(description="Simple commandline code writer")
parser.add_argument("name", type=str, help="specifies the file name")
parser.add_argument("-w", "--overwrite",
                    action="store_true",
                    help="Overwrites the file if existant")
parser.add_argument("-c", "--cls", action="store_true",
                    help="Clears command prompt if given")
args = parser.parse_args()

name = f"{args.name}.py" if not args.name[-3:] == ".py" else args.name

if args.cls:
    os.system("cls")

if args.overwrite:
    file_content = ""
    opening_manner = "w"
else:
    try:
        previous_file = open(name, "r", encoding="utf-8")
        file_content = previous_file.read()
        previous_file.close()
        opening_manner = "a"
    except FileNotFoundError:
        opening_manner = "w"
        file_content = ""


class Editor(cmd.Cmd):
    intro = 10*"=" + " " + name + " " + 10*"=" + "\n" + file_content
    prompt = ""
    content = ""
    empty_line_count = 0
    saving_entered = False

    def emptyline(self):
        Editor.empty_line_count += 1
        if len(Editor.prompt) > 0:
            Editor.prompt = Editor.prompt[:-4]
        if Editor.empty_line_count > 2:
            with open(name, opening_manner, encoding="utf-8") as file:
                file.write(Editor.content[:-2])
                file.close()
            end_line_length = len(Editor.intro) - len(file_content)
            print(end_line_length*"=", "\nSaved successfully")
            return True
        else:
            Editor.content += "\n"

    def default(self, line: str):
        Editor.content += Editor.prompt + f"{line}\n"
        if line[-1] == ":" or line[0] == "\t":
            Editor.prompt += 4*" "


if __name__ == "__main__":
    Editor().cmdloop()