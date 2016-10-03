# Crash Course - Beyond GUI: Command Line Basics

## Intro
(useful for event description)
Beyond the GUI: Command Line Basics


The command-line interface, sometimes called the CLI, is a tool into which you can type text commands to perform specific tasks—in contrast to the mouse's pointing and clicking on menus and buttons. Since you can directly control the computer by typing, many tasks can be performed more quickly, and some tasks can be automated with special commands that loop through and perform the same action on many files—saving you, potentially, loads of time in the process.

Join The Iron Yard instructor Robin Norwood for an introduction to the UNIX command line. This will be an interactive class, and you’ll need a Mac or Linux laptop to participate. We’ll learn some basics of using and navigating the command line, including navigating directories, modifying files, and running commands. You’ll leave with an understanding of the basics of using the command line, and an appreciation for this powerful set of tools.

## Who am I?
Developer, engineering manager, and product manager for ~15 years at Rackspace and Red Hat. Now I’m an instructor at the Iron Yard.

## Who are you?
* No experience with the command line?
* Used the CLI, but not comfortable yet?
* Used the CLI for awhile, but *still* not comfortable with it?
* CLI experts?

## Why are you here?

* What do you hope to get out of this?
* What to expect?
* How will the class go?
* Interactive! Fingers on keyboards!
* Make mistakes.
* I’ll make mistakes too.
* ...and that’s ok!
* Ask questions.

## What will we learn?

* How to get around in the command line
* Files & directories
* Running commands
* How to learn more...

## The Terminal

### Opening the Terminal

The *Terminal* is an application we use to access the command line on modern operating systems. In Mac OS, it's available in the *Applications* folder, or by typing `Command-Spacebar terminal` (Hold down the Command key, press Spacebar, release both keys, and type `terminal` in the Spotlight Search bar).

If you haven't done anything to configure the Terminal, you'll probably see an window with black text on a white background, with some text in it that looks a little like this:

    Last login: Tue Mar 29 08:30:37 on ttys000
    Robins-MBP:~ rnorwood$

We can safely ignore the first line. The second line is the *prompt*. It tells us the name of the computer we're on (`Robins-MBP`), followed by the directory we're in (`~`), and the user we're logged in as (`rnorwood`). The `$`, followed by a rectangle, means the terminal is ready for our commands.

## Basic commands

Now, let's learn some basic commands. From now on, I'll just show the `$` part of the prompt, followed by the command you should type.

    $ ls
    Applications	Documents	Library		Music		Public
    Desktop		Downloads	Movies		Pictures	git

The `ls` (*list*) command shows us the *Directories* (sometimes called *Folders*) in the current directory. What is the current directory? The Terminal starts out in your *home directory* - this is where all of your files and directories are stored. The `pwd` (*print working directory*) will tell us what directory we're in:

    $ pwd
    /Users/rnorwood

`/Users/rnorwood` is my home directory - yours will be different.

The `cd` (*change directory*) command will let us move to a new directory:

    $ cd Documents/
    $ pwd
    /Users/rnorwood/Documents

Your prompt will now probably say `Documents` to let you know you're in that directory. Let's `mkdir` (*make a directory*) to practice in:

    $ mkdir practice
    $ cd practice
    $ ls
    [no output]

Notice that none of those commands had any output - this is typical of the command line. If it doesn't have anything to say, it won't say anything. In this case, no feedback is good feedback. If we give an invalid command, it will tell us so:

    $ cd mimsy
    -bash: cd: mimsy: No such file or directory

By the way, *bash* is the name of the application that provides the command line inside of Terminal. Sometimes we might say *bash shell* or just *shell* instead of *command line*.

### Arguments and Options

You man notice a theme. When using commands, we type the name of the command, like `cd`, sometimes followed by a space and more information, called *arguments*. Most commands also have *options* which modify their behavior:

    $ ls -l ~
    total 0
    drwxr-xr-x   6 rnorwood  staff   204 Mar 23 13:21 Applications
    drwx------+  3 rnorwood  staff   102 Mar 14 11:55 Desktop
    drwx------+  7 rnorwood  staff   238 Mar 29 09:26 Documents
    drwx------+ 13 rnorwood  staff   442 Mar 22 14:02 Downloads
    drwx------@ 50 rnorwood  staff  1700 Mar 22 07:41 Library
    drwx------+  3 rnorwood  staff   102 Mar 14 11:55 Movies
    drwx------+  3 rnorwood  staff   102 Mar 14 11:55 Music
    drwx------+  3 rnorwood  staff   102 Mar 14 11:55 Pictures
    drwxr-xr-x+  5 rnorwood  staff   170 Mar 14 11:55 Public
    drwxr-xr-x   3 rnorwood  staff   102 Mar 16 13:48 git

The `-l` option to `ls` gives us a *long* list, with a lot more information about each file and directory. Don't worry about what all of that information means (yet). The `~` (*tilde*) argument is shorthand for "the current user's home directory".

### Creating, copying, moving, and removing files

*Files* live inside directories. A file is often a document, like one might create with Word, Excel, or any other application. We'll use files a lot during the class, so you should know how to work with them from the command line. Since we're in the `~/Documents/practice` directory we created, we shouldn't clobber any files you already have on your computer.

    $ touch hello.txt
    $ ls
    hello.txt

The `touch` command creates a file if it doesn't already exist. This is one command we won't use much, but it's useful to create a file we can practice other commands on. Now *copy* the file with `cp`:

    $ cp hello.txt goodbye.txt
    $ ls
    goodbye.txt      hello.txt

We want to keep our files organized, so create a directory, and *move* them with `mv`:

    $ mkdir "Text files"
    $ mv hello.txt "Text files"
    $ mv goodbye.txt "Text files"

Notice that this time we put `"` (*quotes*) around the name of the directory - since the command line uses spaces to separate arguments to a command, we have to use the quotes so the command line knows this is a directory name with a space, not two separate arguments.

You may be tired of typing "Text files" so much - use the `tab` key to save some typing:

    $ ls "Tex[tab][enter]
    goodbye.txt	    hello.txt

Another interesting fact about `mv` - not only can it *move* files from one directory to another, it can rename them. So, there's no separate command to rename a file, we just move a file to the new name:

    $ cd "Text files"/
    $ mv goodbye.txt adios.txt
    $ ls
    adios.txt	    hello.txt

Maybe we've decided that this "Text files" directory is a bad idea. Move the files back out of "Text files", into the "practice" directory:

    $ mv *.txt ..
    $ cd ..
    $ ls
    Text files	    adios.txt	    hello.txt

Two new concepts here: First, the `*` (*star* or *glob*) symbol essentially matches any number of letters. You can think of `*.txt` as meaning "everything that ends in `.txt`".

Second, the `..` symbol means "The directory that contains the current one" - sometimes we say "the directory above this one". So in english, the command was "move every file that ends in .txt to the directory above this one".

So, now the `practice` directory has our text files in it, as well as the `Text files` directory, which itself is empty. Since we don't need it anymore, we should *remove* it with `rm`.

WARNING: `rm` is a dangerous command. You can easily remove the wrong files, with little chance of recovery. Use it with extreme caution.

    $ rm -r "Text files"/
    $ ls
    adios.txt	    hello.txt
    $ rm *.txt

No we've removed the text files we created as well. Note that the command line doesn't have a "Trash"; those files are gone permanently, with no easy way to get them back. The command line doesn't mess around.


## Summary of common commands and symbols

So far, we've learned about the following commands:

- `ls` *list* files and directories
- `pwd` *print working directory*
- `cd` *change directory*
- `mkdir` *make* a *directory*
- `cp` *copy* files and directories
- `mv` *move* (or renamed) files and directories
- `rm` *remove* files and directories

We also learned some symbols we can use with these commands:

- `~` the current user's home directory
- `*` match any number of letters in a file or directory name
- `..` the directory that contains the one you're in
- `.` the directory that you're in
- `"` used around a directory or file name that contains a space
- `[tab]` key, used to complete the name of a file or directory (or a command!)

## cat and tail

The `cat` (*concatenate*) command can be used to read from or write to files from the command line. Usually we'll just use a text editor, but occasionally `cat` can be more efficient.

    $ cd ~/Documents/practice/
    $ cat > poem-1_0.txt
    This is just a poem.
    It isn't very good.
    Sorry about that.
    [control-D]

The `>` symbol is called a redirect. In short, using `cat` this way will create poem.txt (or replace it!) with what you type, until you press `[control-D]` to let cat know you're done.

    $ cat poem-1_0.txt
    This is just a poem.
    It isn't very good.
    Sorry about that.

Using `cat` this way concatenates the file to our terminal window (technically to *standard output*). Finally we can append to a file with `>>`:

    $ cat >> poem-1_0.txt

    Hard to believe
    but
    the second stanza
    is worse than the first.
    [control-D]

Cat is pretty useful to quickly see what's in a file, but since it will concatenate the *entire* file, you'll often get more than you bargained for. `head` (*heading*) will instead concatenate just the first lines of a file, and `tail` does the same thing at, well, the other end:

    $ head -n 5 /usr/share/dict/words
    A
    a
    aa
    aal
    aalii
    $ tail -n 5 /usr/share/dict/words
    zythem
    Zythia
    zythum
    Zyzomys
    Zyzzogeton
    $

Tail is most often used with the `-f` argument, which will *follow* the file as more lines are added to it:

    $ tail -f /var/log/wifi.log
    <several cryptic lines of text>

At this point, try turning your wifi connection on and off; you should see more lines of text appear in the Terminal window. Hit `Control-C` in the terminal window to cancel the `tail` command.

## Linking files

Sometimes it is useful to have more than one name for a single file or directory. We use the `ln` (*link*) command to do this. There are two kinds of links: "hard links" and "symlinks". Symlinks will be the better choice almost all of the time, and we use the `-s` option to tell `ln` we want a symlink instead of a hard link, so you'll almost always use `ln -s` together. Just like `cp`, the first argument is the "source", and the second argument is the "destination":

    $ ln -s poem-1_0.txt poem.txt
    $ ls
    poem-1_0.txt	poem.txt
    $ cat poem.txt
    This is just a poem.
    It isn't very good.
    Sorry about that.

    Hard to believe
    but
    the second stanza
    is worse than the first.
    $

If we remove the original file, we'll have what's known as a *broken link*. The command line will still let us do that, though:

    $ rm poem-1_0.txt
    $ cat poem.txt
    cat: poem.txt: No such file or directory

This can be a confusing sort of error to diagnose; `ls -l` can be handy, as it shows the symlink and the file that it is meant to link to:

    $ ls -l
    total 8
    lrwxr-xr-x  1 rnorwood  staff  12 Mar 29 11:39 poem.txt -> poem-1_0.txt

The very first letter (`l`) on the line tells us that the file is a `link`, and the last part of the line tells us that `poem.txt` is meant to link to `poem-1_0.txt`. It doesn't tell us that poem-1_0.txt no longer exists, but we can tell that it doesn't, otherwise it would be listed here.

You can remove links just like any other file:

    $ rm poem.txt

You can also link files outside of your current directory:

    $ ln -s /usr/share/dict/words words
    $ cat words
    [many lines of output]
    zythum
    Zyzomys
    Zyzzogeton


## Open

MacOS provides a nice command line program called `open`, which will *open* a file with whatever the default application is to open that type of file.

    $ open ~/Documents/practice/words
    <A window opens - probably TextEdit>

## Getting help

We've just touched on a few of the basics of the command line. There are lots of ways to get help, starting with `man`, which is the command that shows the *manual* for another command:

    $ man cp
    <screen will fill with text - use arrows to scroll, press 'Q' to quit>

man pages are generally exhaustive help on a given command. They can be a valuable reference, but are more focused on what you can do with the command, not how you can get a specific task done. Often a better way is to search Google for "How to ______ with the command line".

[Explainshell](http://explainshell.com/) is another great tool.

Asking a friend is of course always a good idea.

One more resource is [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) on github, which gives a fairly comprehensive summary of things you can do from the command line.

Permissions in UNIX (the type of operating system that forms the basis for Mac OS and Linux) are a complex topic. For this class, we'll only scratch the surface, but you should leave with enough of an understanding for most everyday tasks.

## Users and sudo

In a UNIX system, there are three kinds of user account:

- *User*: This is what you'd normally think of as a "User" of a computer - a person. When you login to your mac with your username and password, this is the User that represents you on the system. Your user account has permission to do a lot of things, but not everything.
- *System*: A "system" account has a specific set of permissions, and is usually used to run a specific service, such as a web server or a database.
- *Root*: The "root" account, sometimes called the "superuser", has permission to do anything on the system.

You've probably noticed that often when you need to do something that affects the whole system, like install new software, you need to re-enter your password. Behind the scenes, Mac OS is configured to allow your user to have permission to do things like this, but you have to enter your password first. There's an equivalent for the command line called "sudo" (*super user do*). Open a terminal and run:

    $ ls /var/root/
    ls: : Permission denied
    $ sudo ls /var/root/
    Password: <enter your password>
    .CFUserTextEncoding	    .forward		Library

This is a harmless example, but be very cautious running commands with sudo. A common "trick" that some people will play on people new to UNIX is to get them to run (NOTE: DO NOT RUN THIS COMMAND) `sudo rm -rf /` - this will proceed to delete every file on your system, rendering it unusable.

### Listing users from the command line

The `dscl` command accesses Mac OS's user database:

    $ dscl . -list /Users
    [long list of user names, including yours]

## Groups and ids

A similar concept to users is groups. A UNIX group has users in it, and some of the permissions from the group are "inherited" by the users in the group.

Each user and group has both a name, and an *id*. You can list your user information with the `id` command:

    $ id
    uid=501(rnorwood) gid=20(staff) groups=20(staff),701(com.apple.sharepoint.group.1),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),33(_appstore),100(_lpoperator),204(_developer),395(com.apple.access_ftp),398(com.apple.access_screensharing),399(com.apple.access_ssh)

## Permissions to files and directories

Remember the `ls -l` command? It tells us both who owns a file or directory, as well as what permissions are set for them:

    $ ls -l ~
    total 0
    drwxr-xr-x   7 rnorwood  staff   238 Mar 29 23:23 Applications
    drwx------+  5 rnorwood  staff   170 Mar 29 18:17 Desktop
    drwx------+  7 rnorwood  staff   238 Mar 29 09:26 Documents
    drwx------+ 15 rnorwood  staff   510 Mar 29 21:34 Downloads
    drwx------@ 50 rnorwood  staff  1700 Mar 22 07:41 Library
    drwx------+  3 rnorwood  staff   102 Mar 14 11:55 Movies
    drwx------+  3 rnorwood  staff   102 Mar 14 11:55 Music
    drwx------+  3 rnorwood  staff   102 Mar 14 11:55 Pictures
    drwxr-xr-x+  5 rnorwood  staff   170 Mar 14 11:55 Public
    drwxr-xr-x   3 rnorwood  staff   102 Mar 16 13:48 git
    -rw-r--r--   1 rnorwood  staff     0 Mar 31 10:50 test.txt

Starting with `rnorwood` and `staff`, this tells me that the user `rnorwood` and the group `staff` "own" each file and directory in my home directory.

The very first character on each line is `d` for directories, `l` for symbolic links, and `-` for regular files. Following that are three sets of three characters each representing the permissions set on that file for:

1) The user who owns it: `rnorwood` for these files.
2) The group who owns it: `staff` for these files.
3) Everyone else.

For each of these three sets, the value will either be a letter or `-` (meaning "no" or "not set"), and is always in the same order:

- `r`: Read a file, or list files within a directory
- `w`: Write to a file, or create/delete files within a directory
- `x`: Execute (run) a file, or enter (`cd`) a directory

So, according to the `ls` command above:

- Anyone logged into my laptop can read or execute files in my `Applications`, `Public`, or `git` directories, but only I (or my user `rnorwood`).
- Only I can read, write, or execute things in most other directories.
- Anyone can read the contents of `test.txt`, but only I can write to it. No one can execute it - not that anyone would want to, since it's a text file.

## Changing permissions

The `chmod` (*change mode*) command can change permissions on files (among other things).

    $ chmod g+w test.txt
    $ ls -l test.txt
    -rw-rw-r--  1 rnorwood  staff  0 Mar 31 10:50 test.txt

As you can see, now anyone in the `staff` group can write to test.txt. The first argument for chmod works like this:

- The first character is `u` for "user", `g` for "group", `o` for "others", and `a` for "all".
- The second character is `+` to add permission, or `-` to remove permission.
- The third character is `r` for "read", `w` for "write", and `x` for execute.

    $ cat > poem.txt
    I want this poem to
    last forever.
    Like plastic.
    <Control-D>
    $ cat poem.txt
    [text of the poem]
    $ chmod a-r poem.txt
    $ ls -l poem.txt
    --w-------  1 rnorwood  staff  6 Mar 31 11:10 poem.txt
    $ cat poem.txt
    cat: poem.txt: Permission denied

Oops. Now not even I can read the file! I can remove it, though (because `w` is set for my user):

    $ rm poem.txt

Good riddance to bad poetry!

## Permissions and web development

One of the nice things about developing software in Mac OS is that the UNIX underpinnings are similar to those of Linux, which is what most web servers run, including permissions. So, not only will things work in a similar way when your application is deployed, most of the same concepts and tools can be used to troubleshoot problems that occur.

This has been a very brief introduction to permissions. As we said at the beginning, this is a vast topic, and this introduction won't by itself prepare you to solve every (or even most) of the permissions-related problems you might encounter. However, you should have a basic understanding of this topic so you can learn more, and be able to ask (or google for) the right questions when you run into trouble. Also, in most teams, there will be dedicated "operations" staff responsible for system administration, including permissions errors, but as a developer you will at least need to know the basics, so you can work effectively with them.
