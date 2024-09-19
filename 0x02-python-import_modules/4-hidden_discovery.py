#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for s in range(len(name)):
        if name[s][0] != "_" and name[s][1] != "_":
            print(name[s])
