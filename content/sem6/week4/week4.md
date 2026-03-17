---
layout: default
title: "WEEK4 Documentation"
### This Readme consists all the tasks required to be completed before the end of [WEEK4]
---


## Docker Documentation
### ***Introduction***

Docker is an open platform that is used for development, shipping and running of Applications. It enables user to build and develop application in a separate [Sandboxed environment]().
With Docker, you can manage your infrastructure in the same ways you manage your applications.
Docker significantly shortens the delay between [writing code](), [testing it]() and [deploying]() it in Production where each second counts.
Docker can package an application and its dependencies in a virtual container that can run on any Linux, Windows, or macOS computer.
Docker refers to these Sandboxed environments as conatiners.


#### What is a [Container](https://www.docker.com/resources/what-container/) ?

- A Container in terms of Docker is a lightweight, standalone, executable piece of Software that includes everything that is needed to run an Application such as code, runtime, system tools and libraries.
- As Containers are lightweight and contain everything that is needed to run the application, the host is not needed to need any external software besides docker to run the applicaiton.
- Containers are designed to run consistently across different computing environments, making them portable and efficient.
- Containers are isolated from each other and each bundle their own separate software.

### Installation of Docker on Arch Linux

#### 1. Update Your System

First, ensure system's package database is up-to-date. Open your terminal and run:
~~~
sudo pacman -Syyu
~~~
{: .language-bash}


#### 2. Install Docker

Install the **Docker** package from the official Arch repositories.
~~~
sudo pacman -S docker
~~~
{: .language-bash}


#### 3. Start and Enable the Docker Service

After installation, you need to start the Docker service and enable it to launch automatically on system boot.

* **Start the *docker.service* now:**
    ~~~
    sudo systemctl start docker.service
    ~~~
    {: .language-bash}

* **Enable the *docker.service* for startup:**
    ~~~
    sudo systemctl enable docker.service
    ~~~
    {: .language-bash}


#### 4. Add Your User to the Docker Group (Optional but Recommended)

To run `docker` commands without needing to type `sudo` every time, you must add your user to the `docker` group. This group is created automatically during the package installation.

Replace `your-username` with your actual username, or simply use the `$USER` variable.

~~~
sudo usermod -aG docker $USER
~~~
{: .language-bash}

**Important:** For this change to take effect, you must **log out and log back in**, or simply reboot your system.

#### 5. Verify the Installation

Verify the installation by running checking docker version using following command 
~~~
docker -v 
~~~
{: .language-bash}

You should now be able to see Docker Version as output in your terminal.

***Output***
- ![docker-version](../../assets/images/docker-version.png)

#### 6. Run Hello World 

After logging back in, you can verify that Docker is installed and running correctly by executing the classic "hello-world" container.

~~~
docker run hello-world
~~~
{: .language-bash}

The installation was successful, you will see a message beginning with "Hello from Docker!". You now have a fully functional Docker setup on your Arch Linux machine.

***Output***
- ![docker-output](../../assets/images/docker.png)

---

