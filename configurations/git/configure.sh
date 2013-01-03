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
git config --global alias.serve "daemon --reuseaddr --verbose --base-path=. --export-all ./.git"
git config --global alias.fix "commit --amend"
git config --global alias.fshow "!sh -c 'git show --pretty=\"format:\" --name-only \$1 | grep -v \"^\$\" | uniq | sed -e \"s#^#\`git rev-parse --show-toplevel\`/#\"' -"
git config --global alias.fvim "!sh -c 'vim -p \`git fshow \$1\`' -"
git config --global alias.fgvim "!sh -c 'gvim -p \`git fshow \$1\`' -"

# Colors
git config --global color.ui auto

# Diff
git config --global diff.tool gvimdiff

# Core
git config --global core.excludesfile "${HOME}/.gitignore_global"

# Rebasing
git config --global rebase.autosquash true

# Instaweb
git config --global instaweb.httpd webrick
git config --global instaweb.port 4000
git config --global instaweb.browser open
