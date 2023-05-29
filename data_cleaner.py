def clean_srt_file(in_path, out_path):
    with open(in_path) as in_file:
        lines = in_file.readlines()

    o_file_lines = []
    for line in lines:
        line = line.strip()

        # Ignore blank lines
        if not line:
            continue

        # Ignore lines whose first character is a digit
        if line[0].isdigit():
            continue

        o_file_lines.append(line)

    with open(out_path, 'w') as out_file:
        for line in o_file_lines:
            print(line, file=out_file)

