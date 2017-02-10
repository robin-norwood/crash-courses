# Git for Developers

An introduction to git for junior to intermediate software developers.

## Intro
(useful for meetup.com event description)

### Git for Developers

Join The Iron Yard instructor Robin Norwood for a deep dive into git. Over the last few years, git has become one of the most popular ways for software developers to manage their code. However, git adds several layers of complexity over previous systems. Many developers are using git without being able to make use of all of its features and power. This talk aims to fix that by exploring some of the ways that git’s features and design can make our lives as developers easier. Some experience with git or other version control systems is recommended, and you should bring a laptop with git installed so you can follow along.

## Who am I?
Developer, product manager, engineering manager for ~15 years at Rackspace and Red Hat. Now I’m an instructor at the Iron Yard.

## Who are you?
* No experience with git?
* Used git, but not comfortable yet?
* Used git for awhile, but *still* not comfortable with it?
* Have heard that git uses a “Directed acyclic graph”?
* Actually know what that means, and how it applies to git?
* Git experts?

## Why are you here?
* What do you hope to get out of this?
* What to expect

## How will the class go

* Interactive! Fingers on keyboards!
* Make mistakes.
  * I’ll make mistakes too.
  * ...and that’s ok!
* Ask questions.

## What will we learn?

* Git concepts
* Advanced git commands
* Git workflows
* How to learn more...

## What is Git?

Git is a *decentralized version control system*. It’s job is to give developers a way to track changes to the software they write. In contrast to some other version control systems, git is designed to be decentralized - meaning it doesn’t require a single server to be the “source of truth” for a project. It was built to manage source code for large scale open source projects, specifically the Linux kernel.

## Why is git hard?
Almost everyone agrees that git is an incredibly powerful tool. Why do so many developers find it hard to use and understand? I think there are three reasons:

* **Terminology**: Git terminology is a mess. It’s inconsistent, it often “leaks” implementation details, and in many cases the same concept has different names in different places, whether it be the official documentation, the way people describe how it works, and the output of the commands themselves.
* **Exposed wiring**: The git documentation and commands themselves are often more concerned with the underlying details of git’s implementation than with what the user is trying to accomplish. In programmer-speak, it’s a “leaky abstraction”. As a result, git commands can seem opaque and hard to use, and sometimes a single command does wildly different things based on the options and arguments given.
* **Git isn’t always the focus**: Usually, developers are just trying to write the code. They’re often reluctant to spend a whole lot of time learning a lot about the tools they’re using to write the code. This talk is meant to help you fix that by improving your mental model of how Git works and how you can use it.
Many of us learn how to do things with git the same way we do anything else - we google for “how do I …”. Unfortunately, many of the results give you a step-by-step list of esoteric commands without getting into *why* or even *how* the commands work. After this class, you’ll probably still have to do this, but I encourage you to think through the “how” and the “why” these commands work.

## How to use git

Despite the shortcomings I just mentioned, I strongly encourage all developers to learn to use git better. It really is a powerful and elegant system once you learn how to use it. To do that, you’ll need to learn about some of the internals of how git works, and get familiar with some of the esoteric terminology because of some of the issues I mentioned before. In this talk, we’ll dive into git concepts at the same time as we learn how to use git to manage our code.

So...let’s git started! (This is the only ‘git’ pun I plan to make, honest!)

### Concept: Working Directory

Git stores files in a tree of directories, just like pretty much every modern operating system. The git term for your files is the *working directory*. This is the first of the four main locations we’ll need to understand to use git more effectively. In short, your *working directory* is the directory on your computer where your files are stored.

### Concept: Repository

A *repository* or *repo* is where git stores all of the information about your project.

#### Create a local git repo

`git init` - create a local repository

The repository you create lives on your system (in the `.git` directory inside your working directory), and contains all of the information about your project tracked by git.

While your repository actually lives inside a hidden ‘.git’ directory inside your working directory, it’s much more useful to think of it as a separate “location” with stuff inside it. We’ll get into what “stuff” is there later, but for now, know that it includes every version of your working directory git knows about.

#### First steps: Add and Commit

Once we have a repository, we want to put stuff in it. With git, this is a two-step-process:

`git add` - add changes to the *staging area*

`git commit` - Creates a *snapshot* from the contents of the staging area.

`git commit` creates a snapshot of your project at a given point in time. Conceptually, a snapshot knows the state of all of the files in your project, which snapshot is its parent, and some other metadata, like the author, a commit message, and a SHA1 hash of the snapshot, which is used as a unique ID. In everyday conversation, the terms “commit” and “snapshot” are used interchangeably. I’ll use “commit” today.

### Concept: Staging area

The *staging area* is the third conceptual location we need to understand in order to use git. Git uses the staging area to build snapshots/commits. Conceptually, you *stage* all of the changes for your next commit with `git add` (or `git rm` or `git mv`).

**Terminology note**: “staging area”, “index”, and “cache” all refer to the staging area. We’ll use the term “staging area”.

#### The most basic git workflow: Work, add, commit, repeat

These tools give us the most basic git workflow.

First, Do some work.

Once you’ve done a logical “unit” of work, add those changes to the *staging area*, commit, and get back to work - or take a break. This gives you a series of checkpoints in your project, breaking your project into meaningful units of work.

#### Commit messages: The medium is the massage

One of the most important part of a commit is the *message*. These messages are a critical part of documenting the history of your project, so spend some time perfecting the art of a great commit message:

The first line is short (<=50 characters), has no period, and in the imperative mood.
A good tip for getting your message in the imperative mood is to fill in the blank with your message: “Applying this commit will _______”

Optionally, you can include a blank line, and then more details about the commit. Use your text editor to keep the line width to 72 characters or less.

Why the line length limitations? Various git tools do little or not formatting  of the message, and keeping the lines below those limits will prevent ugly wrapping or eliding.

#### Getting information: Git status, git log, and git show

* `git status` - compares the Working Directory, Staging Area, and Repository and summarizes differences between them.
* `git log` - shows a list of commits that are ancestors of the current (or given) commit.
* `git show` - shows information about a given commit.

For once, `git status` is a command without too many options. Two that might be interesting are `-s` for a short summary, and `-b` to show branch info even when `-s` is used.

On the other hand `git log` has a huge number of options and modes. With no parameters or options, git log will show you a log of changes leading up to the current commit. The `--oneline` parameter shows a one line summary of the changes. You can also use `--since` and `--until` to narrow the range of commits, or `--author` to search the author info, or `--grep` to search commit messages. More on git log after we learn about...branches!

`git show` is the way to see an individual commit. It will show the differences introduced in a given commit.

#### “Oops” moments: amending the latest commit
It’s inevitable that you’ll have an “oops” moment...you’ll commit something, and almost immediately realized you made a mistake. Maybe it’s a small typo, or you forgot to “stage” a change, or you realize your commit message isn’t quite right.

* `git amend` - modify the most recent commit

You can change everything about a commit with `amend`, including the author, commit message, and contents of the commit. To use it, add the changes to the staging area, and run `git amend`. It will, in effect, “squash” the two commits. There are three basic uses of `git amend`:

##### Fix the author metadata

If you’ve just set up git on a new computer, but haven’t yet set the “author” info, git will still let you commit without proper authorship info. You can use `git config --global user.name` and `user.email`, followed by `git commit --amend` to reset that info for the previous commit.

##### Fix your commit message

Sometimes you realize your commit message just...isn’t right. All modes of `git --amend` give you a chance to edit it, even if there are no other changes.
Add new changes
Maybe you forgot to `git add` a change, or meant to `git rm` a file. No problem. Just add those changes to the *staging area*, and run `git commit --amend`. The two sets of changes will be squashed into a single commit.

##### Removing committed changes

If you committed changes that you want to “un-commit”, it gets a little more complicated. First, you have to reset the changed file back to the previous state:

```
git reset HEAD~1 <path>
git commit --amend
```

This process will leave the “de-committed” changes in your working directory to do with as you will. More on `git reset` later.

Warning: Never use `git amend` with commits you’ve shared with others through `git push`, or that others may have pulled with `git pull`. NEVER DO THIS. BAD THINGS COULD HAPPEN.

### Concept: Branches
In git, a *branch* is a series of commits with a name. Since each commit knows its own parent, a git stores a branch simply a reference to the last commit in that branch. This makes things like creating and modifying branches incredibly fast.

* `git branch` - create, list, and modify branches

* `git checkout` - switch to branch (or commit, or “ref”)
  * Sets the *current* commit (aka “HEAD”) to the given one
  * Updates the *working directory* to match

When you create a branch: A new branch is created, and points to the given commit. If no commit is given, the new branch points to the current commit (aka “HEAD”). Git branch doesn’t modify the working directory or staging area; it just operates on the repository

In git’s documentation, you may read about *refs* - git branches are refs, as well as a few other things (like tags and HEAD). The default branch in each repository is called “master” unless you change it.
Concepts: Branches, refs, HEAD, and the DAG
So, a branch is just a name that *refers* to a commit. Branches, as well as tags (which we’ll get to soon) are just references, or names, to a commit.

The *HEAD* ref is a “symbolic” ref that acts as a pointer to the “current” branch or commit. Most git commands that operate on commits and branches take *HEAD* into account, or update it. For instance, `git checkout <branch>` updates *HEAD* to point to that branch, and updates the working directory to match it.

Since refs are just names that point to commits, creating, updating, and deleting them are very fast operations in git.

You may have heard that git “stores data as a directed acyclic graph”. Now we know enough to talk about what that actually means. Starting at the end, a *graph* is simply a kind of data structure that has nodes and connections between them. In git, each commit is a node on the graph, and the connections are the parent commit, as well as refs. “Directed” means that those connections have a fixed “direction” that is meaningful - from commit to parent commit. “Acyclic” simply means that the graph cannot have “cycles” - a commit can never be an ancestor of itself. This data structure is fundamental to how git works, but we don’t really need any specialized knowledge of data structures beyond this to understand how to use git.

#### You’re it: Tags
So what about tags? A tag is a ref, just like a branch. The only difference is that a tag always points at a given commit (unless you move it), whereas a branch gets updated if you commit while HEAD is pointing to it, and from some other commands like *merge* and *rebase*.

* `git tag <name>` - create a tag

Tags are most often used to mark (or tag) a given version of your software. As a best practice, released versions of your software are usually tagged, so that you can reliably get back to them. Although it is possible to change the commit a tag points to, this is almost always a bad idea. Especially so if the tag is a “public” one that others might be relying on; git makes changing these difficult and painful by design.

### Combining branches: Merging
Splitting your development history with `git branch` is incredibly useful, but usually only if you can bring the two branches together again.

* `git merge` - combine the changes in two branches

In the default usage, merge brings the changes from the given branch into the current one. This is the classic way to combine two lines of development.

#### Concept: Feature Branches
One of the most common use cases for a branch is a “feature branch”. You want to work on a given feature without affecting - or being affected by - other work going on in the repository. So, your workflow looks like this:

1. Starting from a “known good” stage, create a branch for your feature
2. Switch to that branch (`git checkout -b <branchname>` does both)
3. Do work. Commit as often as you like
4. Once your work is done, switch back to the original branch, and run `git merge <branchname>`

#### Resolving conflicts
If all goes well, git will automatically merge all the changes from the other branch into your current one. Git is very, very good at figuring out how to merge changes, and will usually only have a conflict if the same part of the same file is changed in each branch. When that happens, git will enter a state known as a *merge conflict*, and requires your help to resolve the conflict. When you are in the middle of a merge conflict, `git status` will show you which files have conflicts. Git expects you to edit those files to resolve the conflict, and add/commit those changes to finish the merge. Occasionally, you’ll decide to abort the merge, and deal with the problem later. `git merge --abort` is your escape mechanism.

When resolving a merge, the rule of thumb is “make the conflicting files look like they are supposed to look”. Never, ever commit a merge conflict marked by `>>>>>`, into your file.

#### Concept: Two kinds of merge
Behind the scenes, git has two very different ways of merging: “three-way” merges, and “fast-forward” merges.

##### Three-way merges
With a three-way merge, git examines the history of both branches looking for a common point, examines the differences in each branch, and creates a new commit in the current branch incorporating those differences. If a conflict occurs along the way, you enter the merge conflict state described above, changes are left in the staging area, and the merge doesn’t actually occur until you commit those changes (along with your resolution).

##### Fast-forward merges
Fast-forward merges are actually a much simpler operation for git. If your current branch has no commits since the two branches diverged, there’s no difference between the state of the tree at the “tip” of the other branch and after a merge, so git simply “fast-forwards” by pointing the current branch at the same commit as the other one. Not only is this operation very fast, it also keeps a linear history of your project, as opposed to three way merges, which create a “tree”.

##### Navigating branches and history: git log revisited
Git log has a couple of features to help visualize branches and merges:

* `--graph` - shows branches and merges in a visual graph format
* `--decorate` - shows branches, tags and the HEAD ref

* `git log --oneline --graph --decorate` is a great combo. Try it out.

Going in the direction of more verbosity, you can see more information about each commit in the log:
* `--stat` shows a summary of files changed in each commit
* `--patch` shows the full *patch* of changes included in the commit

You can use ‘..’ syntax to get a range of commits, like: `git log <commit1>..<commit2>` - you can think of it as *from..to*. Since you can use a ref instead of a commit, you can do `git log <branch1>..<branch2>` to see changes that are in branch2 but not branch1...in other words, the changes that will be merged with `git merge branch2` from branch1.

One last set of options to git log:
* `git log --merges` - show only merge commits
* `git log --no-merges` - don’t show merge commits

There are lots more features of git log, but these are some of the most useful.

#### Repeating merges
One more thing with merges - you don’t have to merge just once. You can repeatedly merge from one branch to another. Each time, git will compare how the two branches have differed, and merge any differences found. There are two main uses for repeated merges:

1. Keep a feature branch in sync with the ‘master’ branch by regularly running `git merge master`. This is one way to ensure that master doesn’t diverge too far from your feature, and your feature branch can be easily committed when it’s ready.
2. Some teams use different branches for different environments, or parts of their workflow. For instance, a `dev`, `staging`, and `production` branch. If you merge a feature into dev, and then discover a bug, you can fix the bug in your feature branch, and then merge it back into dev. Later, when the change is merged into the other branches, it will contain all of the changes for the feature.

#### Turn up the (Re)base
Of all the git commands, “rebase” seems to be the one that many of us regard with fear and awe. Knowing how it works is the key to using it effectively.

* `git rebase <upstream>` - graft the current branch onto the tip of &lt;upstream&gt;
* `git rebase <upstream> <branch>` - graft &lt;branch&gt; onto the tip &lt;upstream&gt;
* `git rebase --onto <newbase> <upstream> <branch>` - graft &lt;branch&gt; onto the tip &lt;newbase&gt;

In the first version, rebase looks at the difference between the current branch and &lt;upstream&gt;, and “replays” those commits, as if &lt;branch&gt; were branched from the current tip of &lt;upstream&gt;. `git log <upstream>..HEAD` will show you these commits.

The second version works much the same way, except explicitly gives the branch. `git log <upstream>..<branch>` shows the commits.

The third version again looks at the difference between &lt;upstream&gt; and &lt;branch&gt;, but then applies those changes to &lt;newbase&gt; instead of upstream.

You can think of rebase as giving the current branch a new *base* commit - the tip of the other branch. In effect, this gathers all of the commits in the current branch since it diverged with &lt;upstream&gt;, and “replays” them as a branch from the tip of &lt;upstream&gt;. This means an entirely new set of commits is created. For this reason, rebase is another command you should not use on “public” branches. In every case, &lt;branch&gt; is moved to point to the last commit, but &lt;upstream&gt; and &lt;newbase&gt; are unaffected.

##### Rebase in interactive mode

`git rebase -i ...` allows you to control the rebase process on a per-commit level. It will first open a text editor, and allow you to chose what operation to do with each commit. This is a good way to combine, modify, or remove commits from your history. Git provides a good summary of those options when you do a rebase.

If a rebase is “paused” due to a merge conflict or during an interactive rebase, you’ll first need to commit any additional changes, then one of:

* `git rebase --continue` - continue with rebase
* `git rebase --abort` - cancel the rebase

#### Concept: Rebase and merge use cases
Rebase and merge do similar things: they bring changes from one branch into another.

With *merge*, the history of the repository isn’t changed, but is left in the original branch. A *rebase*, on the other hand, re-writes history by replaying the commits into a new version of history. We’ve talked about what rebase does, now let’s talk about why. A few common use cases for rebase are:

1. You’ve done some work in a (private) branch, and want to “clean up” the history of that branch before it is merged to an upstream branch. You can run `git rebase -i <starting commit>` to enter an interactive rebase of the commits from the starting one to the tip of your branch. By rewriting history, you can make the changes you're about to merge more understandable to someone reviewing your work.
2. Work has continued on two branches to the point where they may start to diverge significantly. You rebase the (private) feature branch against the main branch to keep them from diverging too much with `git rebase master`.
3. Some teams have a policy of only doing fast-forward merges, so mandate that you do a rebase on a topic branch right before merging it with `git rebase <master> <topic branch>` and `git merge --ff-only <topic branch>`. This keeps project history looking clean and linear.
4. Sometimes, someone makes a massive mistake when committing or merging. Judicious use of `git rebase` can be used to repair project history.

Once again, it’s almost always a bad idea to rebase public branches. Since an entirely new set of commits is created, your version of the branch and someone else’s will be completely different, and not easily merged or reconciled.

Merges are both conceptually simpler and generally easier to use. Any time you want the changes from one branch added to another, you can use merge. As an alternative to the “always fast-forward” strategy mentioned above, some teams have an “always make a merge commit” rule. `git merge --no-ff` will ensure that a merge commit is always created.

#### Cherry Pick
Git cherry-pick is a third way of applying changes. Unlike merge and rebase, cherry-pick takes one or more commits, and applies the changes in them to your current branch.

* `git cherry-pick <commits>` - apply one or more commits directly to current branch

The selected commits are applied to the current branch as if they were patches.

#### Reflog
You’ve seen git log; a log of commits. There’s another log, the reflog. This is a log of changes to *refs*. In short, whenever the tip of a branch moves, that change is logged in the reflog.

* `git log --walk-reflogs` - show reflog information in log
* `git reflog` - Changes to history of current branch
* `git reflog --all` - Changes to history of all branches and refs

In general, I recommend starting with `git log --walk-reflogs` to get a picture of the reflog. Consider the `git reflog` commands as more low-level tools.

#### Revert
Git revert is a fairly straightforward command.

* `git revert <commit>` - create a new commit that undoes the changes in the given commit.

Since this command creates a new commit, and doesn’t modify history, it’s often the safest and cleanest way to undo a change.

##### Reset

Of all the confusing git commands, `git reset` may be the most confusing. In part, this is because it operates in a few different modes, depending on the arguments given. For another thing, it can do scary (and sometimes destructive) things to your repository. Let’s look at the most basic mode first.

* `git reset --soft <commit>` - points current branch to &lt;commit&gt;

In `--soft` mode, all that happens is that the current branch is now at the given commit. Often, this commit is somewhere in the past. What that means is that the commits after the one you reset to are lost; either to that branch, or to the entire repository if no other branch refers to them. They aren’t lost forever, though; you can use `git reflog` to see where the HEAD and branch pointers were pointing to, and another `git reset --soft` to return your branch pointer to the correct place. Your working directory is unaffected. One use of this is if you make local changes, and then realize they should be committed to a different branch.

* `git reset --mixed <commit>` - *--mixed* is optional, as it is the default. Points current branch to <commit>, and puts the changes between the old head of the branch and the new one in the *staging area*.

This is the default use of reset. It first does the same re-pointing as with `--soft`, but also puts the differences in the staging area, where they could be committed later. This is similar to a merge, but the old commits may be "lost". This may be used if work has been committed to one branch that should have been committed to another, and it is safe to "throw away" the history of the old branch.

* `git reset --hard <commit>` - Also makes the working directory match the commit in question. This is the "I've gone down the wrong path, I just want to start over" command.

To make matters even more interesting, if files are specified, reset skips the first step and does not set the head reference. In this mode, you can think of reset as meaning “make the staging area (--mixed) or the working directory (--hard) look like this commit.”

Like rebase, it’s almost always a bad idea to reset a “public” branch. Don’t do that.

#### Stash
The *stash* command is useful when context switching. It puts your changes in the working directory and staging area into the “stash”, which is completely separate from the rest of the git version control we’ve talked about.

* `git stash -u` - Stash all changes aside
* `git stash pop` - Remove the last item from the stash, put those changes back in staging area/working directory

The ‘-u’ flag is important - with it, git also stashes *untracked* files and directories (ie, files you’ve never *added* to the staging area or committed. It's almost never a good idea to leave off the '-u' flag.

##### Remote Repositories
We usually use git when working with other developers, which brings us to the fourth “location”: Remote repositories.

Remote repositories (usually called “remotes”) are just like the one on your system, they just happen to live somewhere else. One of the most common places for remote repositories to be hosted is the awesome github.com - github provides free public repositories for individuals and companies, and charges for “private” repos.

We used `git init` to create a local repository. `git clone` also creates a local repository by *cloning* a remote repository.

* `git clone <url>` - creates a local repository as a clone of a remote repository, and sets up some connections between the two.

Clone really does two operations:

1. It sets up a *remote* for the local repo, called `origin` by default.

2. It sets up a default branch, usually called `master`, and a remote-tracking branch, called origin/master

This is most often used when you want to connect to a service like GitHub.

##### Tracking branches

A *tracking branch* is a branch on your local system that "tracks" a branch in a *remote*. In other words, you're telling git "I want my branch to be associated with this remote branch"

* `git checkout --track <remote>/<branch>` - configure current branch to track given remote
* `git checkout <branch>` - will create and track a remote branch if branch doesn’t already exist locally
* `git branch -vv` - list local and tracking branch information

You don't commit to tracking branches. You'll commit to your local branches, and use tracking branches to *fetch* changes from the remote repository.

##### Tug of war: Push and Fetch

* `git push` - send changes from a local branch to a remote repo
* `git fetch` - get changes from a remote repo into your tracking branch
* `git pull` - get changes from a remote branch into your tracking branch **and** merge them into a local branch

Often tutorials will describe `git push` and `git pull` as equivalent. This isn't entirely correct, since behind the scenes `git pull` does two things. To understand this, let's start with `git push`.

`git push` takes our current branch, and checks to see if there is a tracking branch for a remote repository connected to it. If so, it takes changes from our branch and *pushes* them to the remote branch. This is how we share our code with a remote repository. You can think of it as "make the remote branch look like my local branch". This will fail if the remote branch has *diverged* from your local branch: there are commits in the remote branch that aren't in your local branch. When this happens, you need to get your local branch "in synch" with the remote branch using `git pull` or `git fetch` and `git merge`.

`git fetch` again takes our current branch, and checks to see if there is a tracking branch. If so, it looks for changes in the *remote* branch, and pulls them into the tracking branch. It **does not** change your local branch. To do that, you'll need to do `git merge origin/master` (for the "master" branch) to merge those changes into your branch - probably also called "master".

`git pull` simply does a `git fetch` followed immediately by `git merge`. This is often what we want to do, but some people prefer to use `git fetch` followed by `git merge` to make sure they understand the changes they are merging into their branch before the merge happens.

##### The End

We've covered a lot of information!

As I said when we started, git is a very complex and powerful tool. I encourage all developers who use it to keep learning as you use it, to take full advantage of that power, and to extricate yourself from nasty situations that can occur when that power is misused. To do that, I recommend three things:

1. Think. When you use git, think about what is hapenning "under the hood"
2. Practice. Set up a "non-work" git repo and try out these commands in a place where you won't do any damage if you make a mistake.
3. Read. Pro git is a great resource: https://git-scm.com/book/en/v2
4. Ask. Ask your local "git person" for help and advice.
