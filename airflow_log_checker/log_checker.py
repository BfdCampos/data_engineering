import os

def search_file(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            with open(os.path.join(root, file), "r", encoding='latin-1') as f:
                lines = f.readlines()
                for line in lines:
                    if "Done. PASS=" in line:
                        pass_index = line.find("PASS=")
                        warn_index = line.find("WARN=")
                        if pass_index != -1 and warn_index != -1:
                            pass_num = int(line[pass_index+5:].split()[0])
                            warn_num = int(line[warn_index+5:].split()[0])
                            print(f"{os.path.join(root, file)} -- WARN={warn_num}, PASS={pass_num}")
                            if warn_num > 0:
                                print(f"Found WARN in {os.path.join(root, file)}")
                        else:
                            print(f"Error in parsing line: {line}")

    if len(warn_files) > 0:
        print("The following files have WARNs:")
        for file in warn_files:
            print(file)
    else:
        print("No files have WARNs.")

search_file(".")

