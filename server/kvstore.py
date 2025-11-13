import os

base = "db.store"


def put(pid, contents):
    """Store content with proper file handling using context manager"""
    path = get_path(pid)
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(path, "w", encoding="utf-8") as f:
        f.write(contents)

    return True


def delete(pid):
    """Delete a stored file"""
    path = get_path(pid)
    if os.path.exists(path):
        os.remove(path)


def get(pid):
    """Retrieve stored content with proper file handling"""
    path = get_path(pid)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            contents = f.read()
        return contents
    else:
        return None


def get_path(pid):
    if len(pid) < 4:
        path = os.sep.join([base, pid])
    else:
        path = os.sep.join([base, pid[0:2], pid[2:4], pid])
    return path


if __name__ == "__main__":
    import sys
    import time
    import json
    import random

    def batch_write(count):
        start_time = time.time()
        for i in range(count):
            pid = "%d12345678%d" % (i, i)
            payload = {
                "contents": "contents for pid " + pid,
                "extra": "time is %d" % (int(time.time()),),
            }
            put(pid, json.dumps(payload))

        delta = time.time() - start_time
        print("wrote %d records in %d ms. %.4f ms per record") % (
            count,
            int(delta * 1000),
            (delta * 1000 / count),
        )

    def batch_read(count):
        pids = []
        for i in range(count):
            pid = "%d12345678%d" % (i, i)
            pids.append(pid)

        random.shuffle(pids)

        start_time = time.time()
        found = 0
        for pid in pids:
            js_contents = get(pid)
            if js_contents:
                contents = json.loads(js_contents)
                if contents:
                    found += 1
                    if verbose:
                        print(json.dumps(contents, indent=2))

        delta = time.time() - start_time
        print("found %d of  %d records in %d ms. %.4f ms per record") % (
            found,
            count,
            int(delta * 1000),
            (delta * 1000 / count),
        )

    args = sys.argv[1:]
    pid = "12345678"
    verbose = False
    write = False
    count = 1

    while args:
        arg = args.pop(0)

        if arg == "--pid":
            pid = args.pop(0)
        elif arg == "--count":
            count = int(args.pop(0))
        elif arg == "--verbose":
            verbose = True
        elif arg == "--write":
            if args and not args[0].startswith("--"):
                payload["extra"] = args.pop(0)
            write = True
        else:
            print("unknown arg", arg)
            sys.exit(1)

    if write:
        batch_write(count)
    else:
        batch_read(count)
