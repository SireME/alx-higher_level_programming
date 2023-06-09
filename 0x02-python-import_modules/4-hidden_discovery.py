#!/usr/bin/python3

# import and list all defined names in compiles .pyc
if __name__ == "__main__":
    import importlib.util

    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for i in sorted(dir(module)):
        if i[0] != "_":
            print(i)
