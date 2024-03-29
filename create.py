import sys
import os
from github import Github

path = "/Users/.../" #Set the path to where you'll store your projects

username = "" #Insert your github username here
password = "" #Insert your github password here

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Successfully created repository {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()
