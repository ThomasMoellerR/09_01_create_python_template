import argparse
import os


nl = "\n" # newline
ss = "\"" # string sign
bs = " \\" # back slash

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output_folder", help="")
args = parser.parse_args()


if args.output_folder != "": # Sicherheitsmechanismus, damit die eigene main.py und main.sh nicht überschrieben werden können
    if args. output_folder != os.path.dirname(os.path.abspath(__file__)):

        # Create an write "main.sh"
        f = open(os.path.join(args.output_folder, "main.sh"), "w")

        p = os.path.join(args.output_folder, "main.py")

        a = "sudo python3 " + p + bs + nl
        a += "--template " + ss + "template" + ss + bs + nl 

        f.write(a)
        f.close()


        # Create an write "main.py"
        f = open(os.path.join(args.output_folder, "main.py"), "w")

        a = "import argparse" + nl
        a += "import time" + nl
        a += nl
        a += "# Argparse" + nl
        a += "parser = argparse.ArgumentParser()" + nl
        a += 'parser.add_argument("--template", help="")' + nl
        a += 'args = parser.parse_args()' + nl
        a += nl

        a += 'while True:' + nl
        a += '\tprint("test")' + nl
        a += '\ttime.sleep(1)' + nl
        
        f.write(a)
        f.close()


        # Create an write "tmux.sh"
        f = open(os.path.join(args.output_folder, "tmux.sh"), "w")

        p = os.path.join(args.output_folder, "main.sh")

        a = "#!/bin/bash" + nl
        a += "tmux new-session -d -s template " + ss + "bash " + p + ss + nl
        a += "exit 0" + nl

        f.write(a)
        f.close()




        # In main.sh change args.output_folder to ""

        """
        f = open(os.path.join("", "main.sh"), "w")

        p = os.path.join(args.output_folder, "main.sh")

        a = "#!/bin/bash" + nl
        a += "tmux new-session -d -s template " + ss + "bash " + p + ss + nl
        a += "exit 0" + nl

        f.write(a)
        f.close()
        """
