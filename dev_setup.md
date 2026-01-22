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

In your WSL bash terminal:

```sh
sudo apt update
sudo apt upgrade
```

### 1.5. Using WSL2 w/ VSCode DevContainers

Open up [VSCode](https://code.visualstudio.com/download) on your Windows machine. Install the `Remote Development` Extension. In the bottom-left, click on the Remote Window button (blue w/ arrows).
![alt text](https://canonical-ubuntu-wsl.readthedocs-hosted.com/en/latest/_images/remote-extension.png)

Select `Connect to WSL using Distro` and select `Ubuntu-22.04`.

This will open VSCode in your newly made WSL environment.

---

## 2. Configure Git and SSH Keys

In a WSL bash terminal, set enter your Git credentials:

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

Note that, before integration, you will need to shut down WS:

```sh
wsl --shutdown
```

**Checkpoint:**

```sh
docker run hello-world
```

---

## 5. Install the Duckietown Shell

The Duckietown Shell (`dts`) is a CLI that provides key operations like updating a Duckiebot, keyboard control, and acess to sensor data. Install with:

```sh
pipx install duckietown-shell
pipx upgrade duckietown-shell
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

## 9. Duckietown-Gym [Simulation](https://docs.duckietown.com/daffy/devmanual-software/intermediate/simulation/gym-simulation-in-duckietown.html)

Install the simulator in a virtual environment:

```sh
sudo apt install python3-pip
pip3 install virtualenv
cd ~ && virtualenv dt-sim
source dt-sim/bin/activate
pip3 install duckietown-gym-daffy

sudo apt-get install freeglut3-dev
```

NOTE: I had to modify some of their dependencies to get it to work:
```sh
pip3 install "pyglet==1.5.11"
pip3 install "numpy>=1.21,<1.24"
```

Let's run a test script! In your virtual environment:
```sh
sudo apt install gedit python-is-python3
touch test_sim.py
gedit test_sim.py
# copy & paste `test_sim.py`
python test_sim.py
```

---


To run prebuild examples, in your virtual environment, clone the simulation repository:

```sh
git clone https://github.com/duckietown/gym-duckietown.git
```

Run the simulation!

```sh
./gym-duckietown/manual_control.py --env-name Duckietown-udem1-v0
# Try controlling the DuckieBot with your arrow keys
```

---
