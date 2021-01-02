r"""This script compreses and encrypts a given directory into a single file.
Uses custom compression and encryption algorithms."""

# importing standard modules --------------------------------------------------
import sys
import os
import stat
import time


# Sub Task 1: Prepare Directory Tree with all relevant data
# Given a path to a directory, walk the directory.
# If a directory is encountered, recurse into it.
# else store the data of the file into result list
def walkdirectorystructure(absolute_path_to_target: str) -> tuple:
    r"""Function to generate directory structure along with other data"""
    file_size_total_bytes: int = 0
    def walker(absolute_path_to_target: str) -> list:
        r"""Function to build a list containing directory names and file 
        names."""
        nonlocal file_size_total_bytes
        result_list = list()
        result_list.append(absolute_path_to_target)
        target_directory_contents = os.listdir(absolute_path_to_target)
        for item in target_directory_contents:
            item = os.path.join(absolute_path_to_target, item)
            if os.path.isdir(item):
                next_dir: str = os.path.abspath(item)
                temp = walker(next_dir)
                result_list.append(temp) # Append the nested directory structure
            else:
                file_path: str = os.path.abspath(item)
                file_metadata = getfilemetadata(file_path)
                result_list.append((file_path, file_metadata))
                file_size_total_bytes += int(file_metadata['size'])
        
        # The 'result_list' will contain atleast one 'str' indicating the 
        # 'absolute_path_to_target' argument. If the function finds other files or
        # directories then the composition of 'result_list' will be as follows:
        # The first 'str' in the list indicates the base directory.
        # Any subsequent 'str' in the list is a path to a file.
        # Any list in the list will indicate a directory, and the first 'str' in
        # the nested list will be the path to the directory.
        return result_list
    directory_tree_list = walker(absolute_path_to_target)
    return (file_size_total_bytes, directory_tree_list)


# Sub Task 2: Print Directory Tree with all relevant data
# Given a list of directory paths (returned from 'walkdirectorystructure'),
# print directory paths prefixed with '+ ' and file paths prefixed with '- '.
# Print relevant details for both types as well
def printdirectorystructure(directory_tree_list: list, __level__=0) -> None:
    r"""Function to beautifully print to console the provided list containing
    directory names and file names. Implements Sub Task 2"""
    spacing: str = " "*__level__
    print(spacing + "+ " + directory_tree_list[0])
    __level__ += 1
    spacing = " "*__level__
    for item in directory_tree_list[1:]:
        if type(item) == list:
            printdirectorystructure(item, __level__)
        else:
            print("{}- {} mode:{} size: {}"\
                .format(spacing, item[0], item[1]['mode'], item[1]['size']))
    return None


# Sub Task 3: Get File Metadata
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
    for i, arg in enumerate(sys.argv):
        print("Arg[{}] = {}".format(i, arg))

    if len(sys.argv) <= 1:
        raise ValueError("Expected path to a directory as first argument")
    target_directory_path: str = sys.argv[1]
    if not os.path.isdir(target_directory_path):
        raise ValueError("""Expected path to a directory as first argument, \
got "{}" instead""".format(target_directory_path))
    else:
        absolute_path_to_target: str = os.path.abspath(target_directory_path)
    total_file_size, target_directory_contents = walkdirectorystructure(
        absolute_path_to_target
    )
    
    printdirectorystructure(target_directory_contents)
    print("Total size of files on disk (in bytes): {}".format(total_file_size))
