#!/usr/bin/python3
# Chime Kingsley @author
''' A program that prints content of hidden_4 file'''
if __name__ == "__main__":
    import hidden_4
    content = dir(hidden_4)
    for name in content:
        if name[:2] != "__":
            print(name)
