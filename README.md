# ![](logoFull.png)

## Contributions
All contributions are welcome in this repository!

## About
Cfgmngr is a simple tool to store your dotfiles on github. 
With cfgmngr you can add files to be tracked just one time. You dont have to copy them one after another to proper locations, cfgmngr will do it for you!

## Installation
```shell
git clone https://github.com/ChickenMan4236/cfgmngr
cd cfgmngr
sudo make install
```
- And now you can use cfgmngr by typing `cfgmngr` or `cfgm` in your terminal

## How to use?
#### Git repository
> At first you have to specify where to store your files. You can create a private repository on github or another service and then set url to repository in cfgmngr:
- `cfgmngr set-repo [URL]`
> You can check your current repository URL by typing:
- `cfgmngr repo`
#### Files
> When you set your github repository, you can add files, that you want to store:
- `cfgmngr add-file [PATH TO FILE]`
> Your files will be stored in one directory so they should have unique names. When you have to add multiple files with same names, you should set custom names for theese files:
- `cfgmngr add-file [CUSTOM NAME] [PATH TO FILE]`
> To see what files are currently stored you can type:
- `cfgmngr files`
> If you want to remove a file from storage simply type:
- `cfgmngr rm-file [FILE NAME]` 
#### Sync
> When you already have some files in storage, you can push them to you repository:
- `cfgmngr push`
> :warning: Note that all pulled files will overwrite your current configuration files!
> To pull them, you must have specified repository, and then you can type:
- `cfgmngr pull` 
> Cfgmngr stores backup of your files from last pull. You can find them in `~/.config/cfgmngr/backup/`

## License



MIT License

Copyright (c) 2020 Jakub Szczerbiński

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
