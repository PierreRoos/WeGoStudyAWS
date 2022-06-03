# WeGoStudyAWS GitHub

### 1. Create a local copy of this repository. 
Do not fork it, we don't want a new repository on your GitHub Page. We want to collaborate on **THIS** repository. Use **git clone** to create a local copy of this repository.
	
	> cd future/repository/location/  # Where do you want to create your clone in your local system?
	> git clone git@github.com:PierreRoos/WeGoStudyAWS.git  
	> cd WeGoStudyAWS	          # go into your cloned directory
	> ls			          # lists the files in the folder

In this folder are the files which you will be sending back to GitHub. **EDIT THESE FILES** to add your section of code or make any changes.

### 2. Push a new branch back to remote repository
**Create a branch** to add code for a new feature. **Add files** and **commit changes** to the branch, then **push the branch** to this repository.
	
	> git checkout -b branch_name  # creates new branch and moves us into it  
	> 			       # Branch name should represent the feature it is working on (ex. Log_in, create_user, etc.).  

	> git branch  		       # verify your branch  


After you've made changes to files in the folder, its time to add, commit and push the branch.
	
	> git add             # use frequently as you're building your branch
	> 	 .            # add all files 
	>	 --all        # add all files
	>	 filename.ex  # add specific file
	
	> git status	      # shows the status of changes as untracked, modified, or staged
	
	> git commit -m "message describing change"   # use when you finish a part of code that works 
	
	> git push --set-upstream origin branch_name  # set the branch that you want to push (use first time)
	> git push  				      # push your current branch to the repository (use next times)
		

### 3. Submit a pull request
On GitHub web interface, submit a **pull request** and ask for a **review.** The 'Merge Master' or 'Reviewer' will decide whether to merge your branch to the main branch or give feedback.



# WeGoStudyAWS1
