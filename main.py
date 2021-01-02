r"""This script compreses and encrypts a given directory into a single file.
Uses custom compression and encryption algorithms."""

# importing standard modules --------------------------------------------------
import sys
import os


def walkandprintdirectorystructure(
    absolute_path_to_target: str, 
    __level__=0 # Used to calculate spacing and nesting (internal to function)
    ) -> list:
    r"""Function to beautifully print to console the provided list containing
    directory names and file names. Implements Step 1"""

    result_list = list()
    result_list.append(absolute_path_to_target)

    spacing: str = " "*__level__
    print(spacing + "+ " + absolute_path_to_target)
    __level__ += 1
    spacing = " "*__level__
    target_directory_contents = os.listdir(absolute_path_to_target)
    for item in target_directory_contents:
        item = os.path.join(absolute_path_to_target, item)
        if os.path.isdir(item):
            next_dir: str = os.path.abspath(item)
            temp = walkandprintdirectorystructure(next_dir, __level__)
            #temp.insert(0, next_dir)
            result_list.append(temp)
        else:
            file_path: str = os.path.abspath(item)
            print(spacing + "- " + file_path)
            result_list.append(file_path)
    
    # The 'result_list' will contain atleast one 'str' indicating the 
    # 'absolute_path_to_target' argument. If the function finds other files or
    # directories then the composition of 'result_list' will be as follows:
    # The first 'str' in the list indicates the base directory.
    # Any subsequent 'str' in the list is a path to a file.
    # Any list in the list will indicate a directory, and the first 'str' in
    # the nested list will be the path to the directory.
    return result_list
        


# Step #:
# Given a path to a directory, walk the directory and output all contents in it.

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
    target_directory_contents = walkandprintdirectorystructure(
        absolute_path_to_target
    )
    
    print(target_directory_contents)
