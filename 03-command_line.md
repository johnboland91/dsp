# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

cd Home Directory
ls Short Listing
open[file] Opens a file
clear clears screen
reset resets terminal display
touch[file] creates new file
pwd full path to working directory
. current directory
mkdir[dir] creates a new directory
rmdir[dir] removes directory

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`   gives short listing of items in current directory
`ls -a`gives short listing of items in current directory including hidden files
`ls -l` gives long listing of items in current directory
`ls -lh`gives long listing of items in current directory with human readable file sizes 
`ls -lah`gives long listing of items in current directory including hidden files with human readable files sizes 
`ls -t`  gives short listing of items in current directory displaying newest items first 
`ls -Glp`  gives long listing of items in current directory, displaying directories with/,but excludes owners name



---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE
'-r' displays files in reverse order
'-1' displays each entry on a line
'-x' displays files as rows across screen
'-u' Displays files by file access time
'-m' displays the names as a comma separated list
---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs executes arguments 
find ./music -name "*.mp3" -print0 |xargs -0 ls

 

