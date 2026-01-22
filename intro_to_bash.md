# Introduction to the Ubuntu CLI

Ubuntu Bash is a tool that lets you control and navigate your computer without having to interact with any GUIs. This lets you perform key tasks with just your keyboard.

This document is meant to summerize basic Bash CLI commands that are frequently used in SW development and will be organized by functionality.

This is not a complete list of every Bash commands, so I encourage you to explore the internet.

### Key Terminology:

1) **Command-line interface** (CLI): Actual interface/terminal where you are executing commands
2) **Sudo**: Short for "superuser do", `sudo` is a keyword that, when placed before any Bash command, allows you to run the command as the root user. Simply, this temporarily gives a regular user the power to run commands with elevated permissions. The Windows equivilant would be the option to open a terminal with "run as administrator” powers.
3) **Directory**: Location for storing files on your computer (Essentially a folder)
4) **Flags**: Options a user can select to modify a command's behavior. This usually occurs with a single or double dash (- or --) followed by a letter or word. While command has unique flags, there tends to be similarities. For example, many commands tend to use `--version` to print its version and `--help` to print additial information.


## Package Management
A package manager is a collection of tools that is meant to make installing, updating, and removing software easier and consistant. Ubuntu utilizes the [APT](https://ubuntu.com/server/docs/package-management) package manager, which can be utilized using the Ubuntu CLI.

Package information must first be fetched from the APT repository (and whatever other sources are added) in order to be downloaded. To do so, run: 

```bash
sudo apt update
```
To upgrade all currently installed packages, run:

```bash
sudo apt upgrade
```

To install a new package:

```bash
sudo apt install <package name>
```

To remove an installed package:

```bash
sudo apt remove <package name>
```

Sometimes, installed packages have dependencies that are also installed. To remove dependencies that are no longer needed:

```bash
sudo apt autoremove
```

## Files and Directories

### Most Commonly Used

Bash allows you to interact with your files and directories (folders) without having to use the file explorer. To move through your directory, you will primarily be using the `cd` and `ls` commands.

To change directories, use the `cd` command:

```bash
cd <path>  # Go into a directory or path

cd ..  # Go out of the directory you are currently in

cd ~/  # Change directories in reference to the home directory
```

To get a list of available directories and files with reference to your current directory: 
```bash
ls
```

To make a folder:
```bash
mkdir <path>
```

To make a file in your current directory:
```bash
touch <filename>
```

To remove a file in your current directory:
```bash
rm <filename> 
```

To remove a folder: (Be careful as you can delete your entire system)
```bash
rm -rf <path> 
```

### Additional Commands:

1) To unzip: `unzip <filename>`
2) To download a file from online: `wget <link to file>`
3) To copy a file to a new directory: `cp <source> <destination>`
4) To move a file: `mv <source> <destination>` 
5) To give a file executable permissions (ex. ROS nodes): `chmod +x <file>`
6) To change ownership of a file: `chown <user:group> <filename>`
7) To find the location of a specific command: `whereis <commandName>`


## Text and Searching

### CLI Text Editors

While Windows utilizes the Text Editor to edit files, Ubuntu provides a few primary options: vim (not beginner friendly), nano, and gedit (most like Text Editor). To use these:
```bash
vim <path_to_file>
nano <path_to_file>  # Reccomended, slightly harder to pick up
gedit <path_to_file>  # Reccomended, easiest to use
```

Note that if you are trying to edit a protect file, you will need to add `sudo` before.

### Printing and Searching

The `cat` command is extremely powerful and has numerous purposes.

1) `cat` stands for concatenation and can be used to combine files: `cat file1 file2 file3 > file4` would concatenate file1, file2, and file3 into file4.
2) More commonly, `cat` is used to read the contents of files: `cat file1` would print the contents of file`.
3) The `cat` command also can create files (though I personally favor `touch`): `cat > file1`
4) The `cat` command can also copy files: `cat oldfile.txt > newfile.txt`

Another powerful command is `grep`, which is used for searching. 

For example, `dmesg | grep "hello"` would search the start-up (kernal) messages for the keyword "error", useful for debugging hardware issues.

The `|` is refered to as a 'pipe' and directs the outpur from the first command into the second, with the second command in this case being `grep`.


## System Configuration

### Environemtal Variables

Environmental variables are values that are set outside of code and exist in the environment of your system. These values can impact how your system runs and how applications behave. This can include both user-set variables, settings, and paths to applications.

To print all environmental variables:

```bash
printenv
```

To read the value of a specific environmental variable:

```bash
printenv ENV_VAR_NAME
```

To edit a variable's value:

```bash
export ENV_VAR_NAME=value
```

To access an environmental variable in your Bash scipts, use `$`. For example, to go into the user directory:

```bash
cd /home/$USER
```

### .bashrc File

The `.bashrc` is a config file that is run every time a new Bash terminal is created. You can utilize this to automatically run any command you would like at the start of your Bash session (commonly used to automate sourcing paths and creating aliases). To edit your `.bashrc` file:

```bash
sudo gedit ~/.bashrc
```

## USB and Wi-Fi Connections

To list all USB connections: `lsusb`

To get more USB connection information: `sudo fdisk -l`

To list all possible network connections: `nmcli d`

To list all possible Wi-Fi connections: `nmcli d wifi list`

To connect to a Wi-Fi network: `sudo nmcli d wifi connect [SSID] password [PASSWORD]`

To test your Wi-Fi connection: `ping 8.8.8.8` (Should not return 0 if working correctly)



## Additional Resources
1) https://help.ubuntu.com/community/Beginners/BashScripting#:~:text=Bash%20is%20the%20language%20that,from%20one%20or%20the%20other.
2) https://www.digitalocean.com/community/tutorials/linux-commands
