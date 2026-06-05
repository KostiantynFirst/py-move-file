import os


def move_file(command: str) -> None:
    command_line = command.split(" ")
    if len(command_line) == 3:
        source = command_line[1]
        dest = command_line[2]

        if command_line[0] == "mv":
            filename = os.path.basename(source)

            if dest.endswith("/") or os.path.isdir(dest):
                final_dest = os.path.join(dest, filename)
            else:
                final_dest = dest

            parent_dir = os.path.dirname(final_dest)

            if (parent_dir
                    and not os.path.isdir(parent_dir)
                    and not os.path.isfile(parent_dir)):
                os.makedirs(parent_dir, exist_ok=True)

            if os.path.exists(final_dest):
                os.remove(final_dest)

            os.rename(source, final_dest)
