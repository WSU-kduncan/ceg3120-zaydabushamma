



# Project 0 - Git Guide

In your repo for this course, create a file named `git-guide.md`. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it. `status` has a sample of what a well done filled in entry looks like.

Entries that are currently crossed out we will get to later in the course that you could go back and write some details on later.

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
     
- clone
 Clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository (visible using git branch -r), and creates and checks out an initial branch that is forked from the cloned repository's currently active branch.
git clone https://github.com/<user name>/<repository name>
- add
  updates the index using the current content found in the working tree, to
  prepare the content staged for the next commit. It typically adds the current content of
  existing paths as a whole
  git add project0.txt
- rm
   Remove files from the index, or from the working tree and the index. git rm will not
   remove a file from just your working directory.  When --cached is given, the staged content has to match either the tip
   of the branch or the file on disk, allowing the file to be removed from just the index.
  git rv project0.txt
- commit
  Stores the current contents of the index in a new commit along with a log message from the
  user describing the changes.
           $ edit hello.c
           $ git rm goodbye.c
           $ git add hello.c
           $ git commit
  
  
- push
  Updates remote refs using local refs, while sending objects necessary to complete the
  given refs.
git push origin
  
  
- fetch
  Fetches named heads or tags from one or more other repositories, along with the objects
  necessary to complete them.
  git fetch origin
- merge
  Incorporates changes from the named commits (since the time their histories diverged from
  the current branch) into the current branch. This command is used by git pull to
  incorporate changes from another repository and can be used by hand to merge changes from
  one branch into another.
  git merge fixes enhancements
  
- pull
  
  Incorporates changes from a remote repository into the current branch. In its default
  mode, git pull is shorthand for git fetch followed by git merge
   git pull origin
  
- branch
  List, create, or delete branches
  
               $ cd my.git
               $ git branch -d -r origin/todo origin/html origin/man   
               $ git branch -D test 
  
- checkout
   Updates files in the working tree to match the version in the index or the specified tree.
       If no paths are given, git checkout will also update HEAD to set the specified branch as
       the current branch.
  
               $ git checkout master             
               $ git checkout master~2 Makefile  
               $ rm -f hello.c
               $ git checkout hello.c            

- ~~init~~
  This command creates an empty Git repository - basically a .git directory with
       subdirectories for objects, refs/heads, refs/tags, and template files. An initial HEAD
       file that references the HEAD of the master branch is also created.
git init <directory>
- ~~remote~~
 Manage the set of repositories ("remotes") whose branches you track.
  git remote add -f -t master -m master origin git://example.com/git.git/
## git files & folders

- .git folder
- .gitignore file
- ~~.git/hooks~~

## GitHub

- Pull requests
- SSH authentication to repositories
- ~~Actions~~

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project0
