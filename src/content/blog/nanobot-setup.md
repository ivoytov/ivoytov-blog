---
title: "Guide to Setting up a Nanobot (better Openclaw)"
description: "Technical guide to setting up Openclaw in a secure and affordable way"
date: "Apr 10 2026"
---

Since OpenClaw first went viral, I wanted to have an AI agent, but I was very worried about security.

I recently setup [Nanobot](https://github.com/HKUDS/nanobot) and found it to be not only easier to configure, but also much more secure from ground up.

First follow the basic instructions on how to set it up on your local machine. I got it connected to Telegram for chat and to a new Google Workspace email account - I picked `agent@ai.voytov.com`. I use iCloud Email for my personal email, but went with Google Workspace due to easier user provisioning than creating a new Apple account.

Then it's time to move it to the cloud. I initially used Digital Ocean, but they block port 587 (SMTP) by default. Although it only took 24 hours for them to unblock it, I already moved to Hetzner VPS and recommend you start there.


---

## 1. Server Provisioning & Prep

* **The Host:** Spin up a Hetzner Cloud instance (CX22 is usually plenty). Choose the **Docker** "App" image (Ubuntu-based).
* **The "Brain" Directory:** Create the local config folder and fix permissions immediately. The container runs as user `1000`, so the host must grant ownership:
    ```bash
    mkdir -p ~/.nanobot
    sudo chown -R 1000:1000 ~/.nanobot
    ```
* **Config Sync:** Transfer your `config.json` or `settings.json` from your local machine to `~/.nanobot/` on the server using `scp`.

---

## 2. Environment & Code

* **Deployment:** `git clone` your nanobot repository into `~/nanobot-app`.
* **Secrets:** Create a `.env` file inside `~/nanobot-app/`. 
    > **Highlight:** Do not hardcode API keys in the JSON. Use the `.env` for `OPENAI_API_KEY`, `TELEGRAM_TOKEN`, etc., and ensure it is secured: `chmod 600 .env`.

---

## 3. The Optimized Docker Compose
Your `docker-compose.yml` needs specific "Inception-level" permissions to allow the internal sandbox (Bubblewrap) to function.

```yaml
x-common-config: &common-config
  build: .
  env_file: .env
  volumes:
    - ~/.nanobot:/home/nanobot/.nanobot
  cap_drop:
    - ALL
  cap_add:
    - SYS_ADMIN   # Required for container management
    - SETUID      # REQUIRED for Bubblewrap
    - SETGID      # REQUIRED for Bubblewrap
  security_opt:
    - apparmor=unconfined
    - seccomp=unconfined

services:
  nanobot-gateway:
    container_name: nanobot-gateway
    <<: *common-config
    command: ["gateway"]
    restart: unless-stopped
    networks:
      - default

networks:
  default:
    enable_ipv6: false # Prevents "Network unreachable" errors during web searches
```

---

## 4. The "Secret Sauce" (Undocumented Fixes)
Most documentation assumes the container has full reign, but modern Linux kernels (Ubuntu 24.04+) block the sandbox by default. **Run these on the Hetzner host terminal:**

### A. Fix the Kernel Sandbox Block
Bubblewrap requires unprivileged user namespaces, which are often restricted on new servers:
```bash
# Apply immediately
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
sudo sysctl -w kernel.unprivileged_userns_clone=1

# Make permanent
echo "kernel.apparmor_restrict_unprivileged_userns=0" | sudo tee /etc/sysctl.d/60-bwrap-userns.conf
echo "kernel.unprivileged_userns_clone=1" | sudo tee -a /etc/sysctl.d/60-bwrap-userns.conf
```


---

## 5. Execution Commands
```bash
# Build and launch
cd ~/nanobot-app
docker compose build
docker compose up -d

# Quick restart after config changes
docker restart nanobot-gateway && docker logs -f nanobot-gateway
```

---
