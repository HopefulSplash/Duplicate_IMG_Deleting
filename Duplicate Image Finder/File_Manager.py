import os
import hashlib

# path to search
path = "/Users/h.clewlow/Desktop/Python Practice/Python WebScrapper/Images"
duplicate_Files = []
hashed_Files = []


# scan the path and return a count and list of file DIRs
def scan_Path(this_Path):
    folder_Files = []
    count = 0
    print("Files and Directories in '% s':" % this_Path)
    # searches folder and sub folders
    for (root, dirs, file) in os.walk(this_Path):
        for f in file:
            if '.jpg' in f:
                count = count + 1
                folder_Files.append(root + '/' + str(f))
                hash_File(root + '/' + str(f))

    return folder_Files, count


def delete_Single_File(file_Path):
    #check if it exsists
    if os.path.isfile(file_Path):
        os.remove(file_Path)
        print("File Deleted successfully")
    else:
        print("File does not exist")


def hash_File(file):
    #makes a hash
    hasher = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
        hashed_Files.append(hasher.hexdigest())


def delete_Duplicates():
    #runs through the hashes
    for index, file in enumerate(hashed_Files):
        if hashed_Files.count(file) > 1:
            #delete if count is more than 1
            delete_Single_File(file_List[index])
            #add reference
            duplicate_Files.append(file_List[index])
            #remove from file and hash lists
            file_List.pop(index)
            hashed_Files.pop(index)
            #THE Power Of RECURSION
            delete_Duplicates()


if __name__ == '__main__':
    file_List, file_Count = scan_Path(path)
    print("File Dir: ", file_List, )
    print("File Count: ", file_Count)

    delete_Duplicates()