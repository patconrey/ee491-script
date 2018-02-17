# ee491-script
The pi side communication for senior design

# Version control stuff

Hi!

We're gonna go through an example work flow. The assumption is you've just finished writing some code that you want to put on the pi. Let's get it there.

So, push your changes to whatever branch you choose. For example, if it's a sufficiently experimental change, you might want to branch off of Master. To do that from that command line, simple type in `git checkout -b your_new_branch_name_here`. Alternatively, if the branch you want to push to exists, then _before you commit any code_, type in `git checkout branch_name_here`. When you name your branch, make it concise and descriptive. 

To push code to the branch, first, review the changes you've made. Type in `git status`. The output will be a list of files you changed. It'll also tell you what branch you're on. It's prety \#neat. You can also type in `git diff` and it'll give you an in-depth look at the files you've changed (e.g., line numbers, deleted code, added code, etc.). It's overkill and annoying and I hate it. 

Once you're sure you've changed _precisely_ what you've wanted to, it's time to add the code to the commit! Type in `git add file_name_here`. To add all the files you've changed, type in `git add .`. Then run a `git status` to make sure everything you want is written in green. Next step is to actually commit the code. Committing code is quite different than pushing the code to the branch. You can have several commits and only one push. Commits are a way of tracking what each change you made does to the code base. One commit per push is usually sufficient, but it's up to your preferences. When you commit, you have to add a message describing what you changed. Again, concise and descriptive is the goal here. So, after adding all the files to staging, type in `git commit -m "type in some message here about what you changed. you could even throw in some emojis: when you use emojis in git, they're called gitmojis. wild."`.

Once you've committed the files, go ahead and push to the branch you're on: `git push`. If you created a new branch, the terminal will output something along the lines of "that branch doesn't exist upstream." It'll then give you a command to run. Just copy and paste that command, and git will create the new branch upstream and push your code to it.

# Updating the pi
The pi is set up for SSH. There might be some tedious steps depending on if the IP of the Pi changes but we're not gonna talk about that, becuase it's a dark and terrifying place.

So, go to your terminal and type `ssh pi@<IP ADDRESS HERE>`. You'll be prompted to enter the password for the device. The default password, `raspberry`, works still because I'm lazy and I like fruit. 

Once you're in, type in `update-script`. That's an alias I created and takes care of the details. If you get any error message, set the device on fire and walk away. Ain't nobody got time for merge conflicts.
