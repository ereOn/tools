#!/bin/bash

# This script configures git

# User
git config --global user.name "Julien Kauffmann"
git config --global user.email "julien.kauffmann@freelan.org"

# Aliases
git config --global alias.st "status"
git config --global alias.ci "commit"
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.cl "clean -d -x -f"
git config --global alias.sub "submodule"
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"

# Colors
git config --global color.ui auto

# Diff
git config --global diff.tool gvimdiff

# Core
git config --global core.excludesfile "${HOME}/.gitignore_global"
