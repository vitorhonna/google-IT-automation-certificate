# GIT Cheatsheet

- `diff <file1> <file2>`: diff is used to find differences between two files. 
- `diff -u <file1> <file2>`: diff -u is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output -> `diff -u menu1.txt menu2.txt`

```
~$ cat menu1.txt 
Menu1:

Apples
Bananas
Oranges
Pears

~$ cat menu2.txt 
Menu:

Apples
Bananas
Grapes
Strawberries

~$ diff -u menu1.txt menu2.txt 
--- menu1.txt   2019-12-16 18:46:13.794879924 +0900
+++ menu2.txt   2019-12-16 18:46:42.090995670 +0900
@@ -1,6 +1,6 @@
-Menu1:
+Menu:
 
 Apples
 Bananas
-Oranges
-Pears
+Grapes
+Strawberries
```
- `diff -u <file1> <file2> > <diff_file_name>.diff`: create a .diff file from the output, it can then be used to patch the original file.
- `patch`: useful for applying file differences -> `patch <filename_to_be_patched> < <diff_file>.diff`

```
~$ cat hello_world.txt 
Hello World
~$ cat hello_world_long.txt 
Hello World

It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt 
--- hello_world.txt     2019-12-16 19:24:12.556102821 +0900
+++ hello_world_long.txt        2019-12-16 19:24:38.944207773 +0900
@@ -1 +1,3 @@
 Hello World
+
+It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff
~$ patch hello_world.txt < hello_world.diff 
patching file hello_world.txt
~$ cat hello_world.txt 
Hello World

It's a wonderful day!
```

- `git commit -am "<commit message>"`: Stages files automatically
- `git log -p`: Produces patch text
- `git show`: Shows various objects
- `git diff`: Is similar to the Linux `diff` command, and can show the differences in various commits
- `git diff --staged`: An alias to --cached, this will show all staged files compared to the named commit
- `git add -p`: Allows a user to interactively review patches to add to the current commit
- `git mv`: Similar to the Linux `mv` command, this moves a file
- `git rm`: Similar to the Linux `rm` command, this deletes, or removes a file
- `git checkout <branch name>`: is used to switch branches.
- `git reset`: basically resets the repo, throwing away some changes.
- `git commit --amend`: is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.
- `git revert`: makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.
- `git branch`: Used to manage branches
- `git branch <name>`: Creates the branch
- `git branch -d <name>`: Deletes the branch
- `git branch -D <name>`: Forcibly deletes the branch
- `git checkout <branch>`: Switches to a branch.
- `git checkout -b <branch>`: Creates a new branch and switches to it.
- `git merge <branch>`: Merge joins branches together. 
- `git merge --abort`: If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.
- `git log --graph --oneline`: This shows a summarized view of the commit history for a repo.
- `git clone <URL>`: Clone a remote repo into a local workspace
- `git push`: Push commits from the local repo to the remote repository
- `git pull`: Fetch the newest updates from a remote local repository and merges it into the local repository
- `git remote`: List remote repos
- `git remote -v`: List remote repos verbosely
- `git remote show <name>`: Describes a single remote repo
- `git remote update`: Fetches the most up-to-date objects (doesn't merge the updates)
- `git fetch`: Downloads specific objects (doesn't merge the updates)
- `git branch -r`: List remote branches (read only)
- `git rebase <branch_name>`: Move the current branch on top of the "branch_name" branch