"""Create a verifiable manifest for a selected set of local files."""
from runtime import *

import hashlib
import stat
def process(data):
    root=Path(text(data["root"],"root")).resolve(strict=True)
    if not root.is_dir(): raise ValueError("root must be a directory")
    paths=strings(data["paths"],"paths")
    if not paths or len(paths)>1000: raise ValueError("provide 1..1000 paths")
    if len(set(paths))!=len(paths): raise ValueError("duplicate path")
    output=[]
    total=0
    groups={}
    for name in paths:
        rel=Path(name)
        if rel.is_absolute() or ".." in rel.parts: raise ValueError("path escapes root")
        current=root
        for part in rel.parts:
            current=current/part
            if current.is_symlink(): raise ValueError("symlinks are not supported")
        before=current.stat()
        if not stat.S_ISREG(before.st_mode): raise ValueError("path is not a regular file")
        if before.st_size>64*1024*1024: raise ValueError("file exceeds 64 MiB")
        digest=hashlib.sha256()
        count=0
        with current.open("rb") as stream:
            while True:
                chunk=stream.read(65536)
                if not chunk: break
                count+=len(chunk)
                total+=len(chunk)
                if count>64*1024*1024 or total>512*1024*1024: raise ValueError("read limit exceeded")
                digest.update(chunk)
        after=current.stat()
        if (before.st_size,before.st_mtime_ns,before.st_ino)!=(after.st_size,after.st_mtime_ns,after.st_ino) or count!=before.st_size:
            raise ValueError("file changed during read")
        hashed=digest.hexdigest()
        output.append({"path":name,"bytes":count,"sha256":hashed})
        groups.setdefault(hashed,[]).append(name)
    return {"files":output,"total_bytes":total,"duplicate_groups":[v for v in groups.values() if len(v)>1]}

if __name__ == "__main__":
    sys.exit(main(process, "Create a verifiable manifest for a selected set of local files."))
