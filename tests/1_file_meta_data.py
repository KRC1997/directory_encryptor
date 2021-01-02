# importing standard modules --------------------------------------------------
import sys
import os
import stat
import datetime
import time
import pprint

"""
stat.ST_MODE
- Inode protection mode.

stat.ST_INO
- Inode number.

stat.ST_DEV
- Device inode resides on.

stat.ST_NLINK
- Number of links to the inode.

stat.ST_UID
- User id of the owner.

stat.ST_GID
- Group id of the owner.

stat.ST_SIZE
- Size in bytes of a plain file; amount of data waiting on some special files.

stat.ST_ATIME
- Time of last access.

stat.ST_MTIME
- Time of last modification.

stat.ST_CTIME
- The “ctime” as reported by the operating system. On some systems (like Unix) 
is the time of the last metadata change, and, on others (like Windows), is the 
creation time (see platform documentation for details).
"""


def getfilemetadata(absolute_path_to_file: str) -> dict:
    r"""Function to get file meta data as a dict"""
    file_stat = os.stat(absolute_path_to_file)
    result = dict()

    # Metadata that is important / retained
    result["mode"] = stat.filemode(file_stat.st_mode)
    result["size"] = file_stat.st_size
    result["last_access_time"] = time.localtime(file_stat.st_atime)
    result["last_modified_time"] = time.localtime(file_stat.st_mtime)
    result["create_time"] = time.localtime(file_stat.st_ctime)

    # Metadata that is unimportant / not retained
    # result["inode_number"] = file_stat.st_ino
    # result["inode_host_dev"] = file_stat.st_dev
    # result["inode_nlink"] = file_stat.st_nlink
    # result["owner_user_id"] = file_stat.st_uid
    # result["owner_group_id"] = file_stat.st_gid

    return result

if __name__ == "__main__":
    target_file_path: str = sys.argv[0]
    target_file_path = os.path.abspath(target_file_path)

    result = getfilemetadata(target_file_path)
    pprint.pprint(result)