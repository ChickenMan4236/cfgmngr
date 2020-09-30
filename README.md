# cfgmngr

## About
Cfgmngr is a simple tool to keep your system config files up to date. 
With cfgmngr you can synchronize your config files with theese from previous installation or from another computer.
You can specify which config files should be stored. Cfgmngr will pack them together to one directory and push them
to git repository. Then you can pull them to another computer and cfgmngr will automatically copy them to proper locations.

## Installation
Simply clone this repository, go to `src/` and use `make`. Now you can use cfgmngr by simply typing `cfgmngr` in terminal.

## How to use?
#### Git repository
> First you have to specify where to store your files. You can create a private repository on github or another service and then set url to repository in cfgmngr:
- `cfgmngr set-repo [URL]`
> You can check your current repository URL by typing:
- `cfgmngr repo`
#### Files
> When you set your github repository, you can add files, that you want to store:
- `cfgmngr add-file [PATH TO FILE]`
> To see what files are currently stored you can type:
- `cfgmngr files`
> If you want to remove a file from storage simply type:
- `cfgmngr rm-file [FILE NAME]` 
#### Sync
> When you already have some files in storage, you can push them to you repository:
- `cfgmngr push`
> To pull them, you must have just specified repository, and then you can type:
- `cfgmngr pull` 
> Note that all pulled files will overwrite your current configuration files!

## License



MIT License

Copyright (c) 2020 Jakub Szczerbiński

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
