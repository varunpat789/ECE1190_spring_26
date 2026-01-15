# Duckiebot DB21M Setup Guide

This guide walks through setting up a Duckiebot DB21M, compiling instructions from the [official Duckietown documentation](https://docs.duckietown.com/daffy/opmanual-duckiebot/setup/setup_laptop/setup_dependencies.html).

---

## 1. Install Ubuntu 22.04 with WSL2 (Windows Only)

Make sure Windows is up to date before proceeding.

In PowerShell or Windows Command Prompt, run:

```powershell
wsl --set-default-version 2
wsl --install -d Ubuntu-22.04
```

You'll be prompted to create a username and password (the password won't display as you type).

**Checkpoint:** In another terminal, verify the installation:

```powershell
wsl --list -v
```

For troubleshooting, see the [WSL install manual](https://learn.microsoft.com/en-us/windows/wsl/install-manual) or [troubleshooting guide](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting).

---

## 2. Configure Git and SSH Keys

Set up Git credentials matching your GitHub account:

```sh
git config --global user.name "your_user_name"
git config --global user.email "youremail@domain.com"
```

Generate and add an SSH key:

```sh
# Generate SSH key (press Enter to skip all prompts)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Display the public key
cat ~/.ssh/id_ed25519.pub
```

Copy the entire key, then add it to your GitHub account: **Settings → SSH and GPG Keys → New SSH Key**

See the [GitHub SSH documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for detailed instructions.

---

## 3. Install Basic Tools

```sh
sudo apt update
sudo apt install -y pipx git git-lfs curl wget
pipx ensurepath
```

**Checkpoint:**

```sh
pipx --version
```

---

## 4. Install Docker

Follow the [Docker Desktop WSL instructions](https://docs.docker.com/desktop/features/wsl/) to install Docker.

You will need to restart your system after installation.

**Checkpoint:**

```sh
docker run hello-world
```

---

## 5. Install the Duckietown Shell

The Duckietown Shell (`dts`) is a CLI that provides key operations like updating a Duckiebot, keyboard control, and acess to sensor data. Install with:

```sh
pipx install duckietown-shell
```

**Checkpoint:**

```sh
which dts
# Should output a path ending with "dts"
```

---

## 6. Configure the Duckietown Shell

Set the shell to use the `daffy` distribution:

```sh
dts profile switch daffy
```

---

## 7. Set Up Your Duckietown Token

1. Create a free account at the [Duckietown Hub](https://hub.duckietown.com)
2. Copy your token from your profile
3. Register the token with `dts`:

```sh
dts tok set <INSERT_TOKEN_HERE>
```

**Checkpoint:**

```sh
dts tok status
# Output: dts : Correctly identified as uid = ***
```

---

## 8. Configure Docker Credentials

1. Create a Docker account at [docker.com](https://app.docker.com/signup)
2. Generate a [personal access token](https://docs.docker.com/security/access-tokens/)
3. Log in to Docker (use your access token as the password):

```sh
docker login -u <DOCKER_USERNAME>
```

4. Pass docker credentials to Duckietown:

```sh
dts config docker credentials set --username <DOCKERHUB_USERNAME> --password <DOCKERHUB_ACCESS_TOKEN>
```

**Checkpoint:**

```sh
dts config docker credentials info
```

---

## 9. Flash the SD Card

Choose a hostname for your robot. Valid hostnames must be lowercase, start with a letter, and contain only letters, numbers, and underscores.

Insert your SD card with a reader, then run:

```sh
dts init_sd_card --hostname <HOSTNAME> --type duckiebot --configuration DB21M --wifi designlab:designlab1
```

When prompted, enter `32` for the microSD card size.

---

## 10. Boot the Duckiebot

1. Insert the SD card into your robot
2. Press the button on side (by the battery) to boot

Ensure your computer is connected to the same WiFi network as the Duckiebot. You can monitor the boot process:

```sh
dts fleet discover
```

This displays all reachable Duckiebots with their model, hostname, and status.

---

## 11. Post-Boot Updates

Once the status shows **Ready**, it is done booting. Now update the software:

```sh
dts duckiebot update <DUCKIEBOT_HOSTNAME>
```

---

## 12. Access the Dashboard

Your dashboard has key robot debugging tools, sensor streams, and health information. Open your browser and navigate to:

```
http://<YOUR_DUCKIEBOT_NAME>.local/
```

NOTE: If that doesn't work, try without `.local`:

```
http://<YOUR_DUCKIEBOT_NAME>/
```

---

## 13. Start Roboting!

To move your Duckiebot, open a terminal and run:
```sh
dts duckiebot keyboard_control <DUCKIEBOT_NAME>
```

## Common Commands

| Action        | Command                             |
| ------------- | ----------------------------------- |
| Shutdown      | `dts duckiebot shutdown <HOSTNAME>` |
| Reboot        | `dts duckiebot reboot <HOSTNAME>`   |
| Discover bots | `dts fleet discover`                |
| SSH           | `ssh duckie@<ROBOT_HOSTNAME>.local` |

Note that shutdown can take up to 20 seconds.