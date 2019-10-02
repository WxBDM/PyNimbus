# Contributing to PyNimbus

First off, I want to be the first to say thank you for wanting to contribute to PyNimbus! This document serves as a basis to show you how to go about contributing to an open source project.

If you have a question pertaining to the usage of PyNimbus, do not open an issue or pull request. Rather, contact the project manager directly. Information can be found under "Contact".

## How the repository is set up

The master branch is the code that is the latest version (that is, published on PyPi). The development branch is the branch that all of the contributions get merged into before getting pushed to the latest version. Every other branch is a contributor's "workspace". Each contributor works in their own branch, and when they are ready to have their code reviewed, they'll issue a pull request and a project manager will review the code before merging it into the development branch. When a new version is ready to be released, the development branch will be merged into master.

## Important links for contributions

Below are some important links that you may need while contributing to the project.

- [HTML Documentation](https://pynimbus.readthedocs.io/en/latest/)

- [Issues](https://github.com/WxBDM/PyNimbus/issues)

## What can I do to contribute?

[This]() is more of a question of "what can't I do to contribute?", simply because there is so much to do. The first place to start is by checking out the Issues Tracker and seeing if something there works for you. If nothing intrigues you, then look around at the documentation and see if there's anything to be improved upon there. TL;DR: look around, you'll find something eventually :)

#### Hacktoberfest

If you are here for Hacktoberfest, pop on over to the [Issue Tracker](https://github.com/WxBDM/PyNimbus/labels/Hacktoberfest) page. Keep checking back because more issues will be added.

#### What if I don't want to code?

No worries, there's a lot of house-keeping related things that needs to get done such as improving existing documentation. Check out the HTML documentation page and see if there's anything that can be improved upon. If you want to get in touch with your inner artist, you can create diagrams and/or flow charts of how stuff works in this project.

#### What if I've never contributed to an open source project before?

See below section (issuing a pull request) for step-by-step instructions.

## Issuing a pull request

All contributions are made via pull requests. Before doing issuing a pull request, please comment on an issue or send the project manager an email to explain what you want to work on.

Once you're added to the project, fork the repository. Then, go into your GitHub profile, find the repository, and click on it. From there, click the green button that says "Clone or Download" and click the clipboard icon to copy the link.

From here, open a new terminal window and navigate to the directory where you want to store the source code. Type `git clone` and paste the link you had copied. This will clone the repository locally.

Now, create a new branch by typing `git checkout -b YOUR_GITHUB_USERNAME` (replacing YOUR_GITHUB_NAME with your GitHub username). Now type `git checkout YOUR_GITHUB_USERNAME` to switch to that branch. Now, you're able to begin working on your end of the project.

Once you are ready to submit, add your files (`git add .`), commit (`git commit -m "YOUR_MESSAGE_HERE"`), and push your branch (`git push origin YOUR_BRANCH_NAME`).

Now, navigate to the repository on GitHub and click "Compare & Pull Request" and open a pull request. A project manager will review the code and either accept or deny it. If denial happens, don't worry! It's their job to ensure that you're given the push in the right direction. If your code is accepted, congratulations! You have successfully made a contribution to the project. 

#### IMPORTANT

Make sure you are working within the branch you created from the steps above and not any other branch. This should equate to your GitHub username. __Any pull requests in which modified code is not located in your branch will be rejected.__ In addition, any pull request to merge into master will be changed to the development branch. To see which branch you are working in, type `git checkout` and an asterick (\*) will show up with the current branch. The master branch is reserved for the stable release, whereas "development" is the unstable release.

### Hearing back from Pull Requests

Please note that the project owner is in school, so it may take a bit to hear back. However, you should hear something within 24 hours.

## Contributing License Agreement

Unfortunately, I have to have this here in case any legal issues pop up. See the Contributing License Agreement file for more details.

## Contact

You can contact the project owner, Brandon Molyneaux, via e-mail at bdm0041@auburn.edu.

## PyNimbus Contributors

The following is a list of people who have contributed to PyNimbus:

__Project Owner/Manager:__ Brandon Molyneaux

__Project contributors:__  
[rishabmenon](https://github.com/rishabmenon)
