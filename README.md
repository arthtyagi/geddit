# Geddit 🦄

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/arthtyagi/geddit) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django?style=flat-square)
[![Requirements Status](https://requires.io/github/arthtyagi/geddit/requirements.svg?branch=master)](https://requires.io/github/arthtyagi/geddit/requirements/?branch=master)
![GitHub top language](https://img.shields.io/github/languages/top/arthtyagi/geddit)
![GitHub Pipenv locked dependency version (branch)](https://img.shields.io/github/pipenv/locked/dependency-version/arthtyagi/geddit/django/master)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/django?color=green)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/django)
![GitHub Pipenv locked Python version (branch)](https://img.shields.io/github/pipenv/locked/python-version/arthtyagi/geddit/master?color=black&style=flat-square)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![GitHub last commit (branch)](https://img.shields.io/github/last-commit/arthtyagi/geddit/master?style=for-the-badge)


![code (2)](https://user-images.githubusercontent.com/41021374/86322013-c1ee0680-bc57-11ea-8152-ca67856d9df4.png)

Geddit is an open-source web app that is essentially a skeleton project of DomeCode with similar components. It is being used for testing purposes.
The project has two modules, the Notes app and the To-Do app and other upcoming modules.

NOTE : The Forum, Notes and Tasks in the basic usable form is all there will be to Geddit since I don't intend to make DomeCode free initially. I'll consider open-sourcing DomeCode in the future. 

- 10th July 2020 - Once I'm done with adding a decent yet purely basic forum to Geddit, I'll halt the contributions to Geddit and shift my workflow to DomeCode that will have more features with a better UI and more AND might also be open-sourced in the future. As for Geddit, I'll make its apps re-usable and continue to accept PRs if there are any. If you're interested in working on [DomeCode](https://arthtyagi.me/domecode), feel free to contact me. The link I've added for DomeCode gives a quick and rough overview of what it'll be, however it is to be noted that it is not a complete representation of the features being built for DomeCode by any measure. 

The modules are made using :
- Django, 🐍
- Bootstrap 🎃 and well, 
- DHTML 👀
- React.js ⚛️ soon! 🍻

## Upcoming Modules :

- Forums :page_with_curl:
- Resumé 💼
- FAQ 🙋

## TO-DO :

- [X] Notes specific to individual users.
- [X] Signin using Email. 
- [X] Signin using Github.
- [X] To-do Lists specific to individual users.

### Projected Timeline:

There's no such thing as timeline for Geddit, it's a project that will have various branches and will be a skeleton project to test new project. Albeit, a sandbox. So yeah, have at it! Fork this thing.

### What's new?

Well as of now, it has a fairly good responsive UI, notes, tasks, a search bar, Github Login, an upcoming forum, labels and images in notes. Increased the security of this repo by using decouple. More on the way since essentially all of these features are being ported over by me to [DomeCode](https://arthtyagi.me/domecode) except they'll be more polished and would hopefully make the end user spend more time on the application. ( Application since it'll be a PWA i.e. a Progressive Web Application as well ).

July 5th Update : Ajaxified Like Buttons. In simple words, the pages don't have to reload to process the task of liking an object, in the case of Geddit, a note or a task.

### Fun shit :

 - [ ] Adding date picker
 - [ ] Redoing the UI in React.js
 - [ ] Public and Private Notes and Tasks.
 - [ ] Adding a How-To use this animator.
 - [X] Support Markdown
 - [X] Support Rich Text Editing

### Am I using AJAX?

Yes, I'm using Ajax at certain places in the app. I feel that a technology shouldn't be used just because it's "cool" but only if it actually fulfills a purpose that wouldn't be achieved otherwise.

I've used Ajax only where it makes a significant difference such as Like/Upvote Buttons and Incremental Search ( search as you type ). I've not used AJAX in my Todo either which seems radical but trust me, I've crafted the ToDo such that AJAX wouldn't have made a particularly huge difference.

- Does this mean I won't be implementing AJAX anywhere? 

No, not really. I'll be implementing AJAX only if it provides a performance increase to a substantial amount of traffic since then it'd really make sense but that's still in the future and also, implementing AJAX for performance improvements is still down on my list below better core functionality of the application so yeah, I'll eventually come to it. Or hopefully, someone else does and creates a pull request.

The way the app works is such that the effect of AJAX on the application itself won't be much hence, I'm not in a hurry to implement that. Most of the app works on page refreshes since the cases where there is a POST request are generally scenarios where the user would spend quite a bit of time and a page refresh would make sense, it doesn't have much of an effect on UX. However, in conditions like that of an Upvote Button, an AJAX call makes way more sense since the user wants the result instantly and a page refresh for every such small task would be stupid.

In a nutshell, use the tool when it has a valid use case. Throwing tools at a thing might work but it's just not good I suppose.

### What kind of search engine am I using?

I'm using a primitive search engine that's made through simple logic. It powers Notes, Tasks and Forums since these are the only features requiring a search bar in all honesty. Especially the forums. The search engine works effectively for finding exact content/keyword in your notes and tasks. However, for forum it's useful to look for the particular topic instead of typing multiple keywords since the caveat of this search engine is the inability to handle multiple keywords unless they are discovered in succession in the content. To improve upon this, I could be using enterprise solutions but since that's just an overhead expense until I see decent user base growth on the platform, DomeCode, I'll stick to using this. Although, given that forums would need better search ability, I'll add sorting options along with the pre existing keyword search engine to make it viable in the domain of a standard forum. 

### A new feature that could be really sick!

Private messaging would be great I suppose to contact people you meet on the forums along with a secret feature I'm planning to work on, it will set the whole vibe for the DomeCode application.

Private messaging because mind you, this is not a standard forum application or a to-do application, these all are just submodules of a bigger application that revolves around providing resources for code from all over the internet and also allows users to practice within the app. Hence, private messaging as an addition to all the features DomeCode will have soon would prove to be really sick. The whole idea is to create a small ecosystem within the application and make it possible for the user to get things done with way more ease than other similar platforms because of the simple yet intuitive and extensive features DomeCode would hold.

### What does that look like right now?

![image](https://cdn.discordapp.com/attachments/593123274465083393/727562175010570350/unknown.png)
![image](https://cdn.discordapp.com/attachments/593123274465083393/727562377007988836/unknown.png)
![image](https://cdn.discordapp.com/attachments/593123274465083393/727562337946435715/unknown.png)

### How to get started with contributing to Geddit? 

Feel free to pick up any of the issues, point out some if you find and make some enchancements.

###  How to contribute? 

This shouldn't be a legit question but I'm still gonna include a simple 3 step process for the noobs.

- Fork this repo and then clone that fork on your local machine.
- Open the project in Vim/Emacs ( or whichever editor you prefer ), start the virtual environment with `pipenv shell`.
- I've also included the requirements.txt file just in case in case you wanna use `venv`. Either way, install the requirements and start coding!

Contributions, stars and forks are appreciated! This project looks basic rn but is growing continously in a large codebase for an even better codebase of DomeCode ( a product I'm building ) of which this acts as testing project with hands-on experience. Code for one, make progress with two ideology! :P 
