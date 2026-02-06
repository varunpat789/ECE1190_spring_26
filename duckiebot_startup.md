# DuckieBot Flashing

## 1. Flash the SD Card

Choose a hostname for your robot. Valid hostnames must be lowercase, start with a letter, and contain only letters, numbers, and underscores.

Insert your SD card with a reader, then run:

```sh
dts init_sd_card --hostname <HOSTNAME> --type duckiebot --configuration DB21M --wifi designlab:designlab1
```

When prompted, enter `32` for the microSD card size.

---

## 2. Boot the Duckiebot

1. Insert the SD card into your robot
2. Press the button on side (by the battery) to boot

Ensure your computer is connected to the same WiFi network as the Duckiebot. You can monitor the boot process:

```sh
dts fleet discover
```

This displays all reachable Duckiebots with their model, hostname, and status.

---

## 3. Post-Boot Updates

Once the status shows **Ready**, it is done booting. Now update the software:

```sh
dts duckiebot update <DUCKIEBOT_HOSTNAME>
```

---

## 4. Access the Dashboard

Your dashboard has key robot debugging tools, sensor streams, and health information. Open your browser and navigate to:

```
http://<YOUR_DUCKIEBOT_NAME>.local/
```

NOTE: If that doesn't work, try without `.local`:

```
http://<YOUR_DUCKIEBOT_NAME>/
```

---

## 5. Start Roboting!

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