- title: Setting Up a ROS Development Environment
- date: 2020-10-17
- modified: 2020-10-17 00:00
- category: Engineering
- tags: Software Engineering, DevOps
- slug: RosDock
- summary: Setting up ROS in a Docker container
- header_cover: images/data-centre.jpg

There are a lot of tutorials out there about how to set up and use [ROS](https://www.ros.org). But all of them assume that the intention is to have ROS take over the default environment. This becomes very problematic when you only have one development machine and are working on a lot of other projects -- dependency conflicts are one of the main pain-points when using ROS.

One solution is to consider containerizing your development environments. While virtual machines have their place in this solution, it's typically not viable because robotics development is focused on as near real-time performance as possible. Like ROS, [Docker](https://www.docker.com) has enjoyed a lot of success and has an equally rich set of tutorials; most are focused around deployment of some web service. It gives you the advantage of using the actual system hardware while simply tricking the environment its running upon. But Docker can be challenging to ensure grapical applications (like [Gazebo](https://gazebosim.org)) function properly.

So let's walk through how to get this set up!

**Disclaimer**: The following was implemented on Ubuntu 20.04 Desktop. This process likely works with other versions of Linux and can be adapted for use in Win10, but it will be up to the reader to do so.



# Installing Docker
The *de facto* guidance for installation is through Docker's [documentation](https://docs.docker.com/engine/install/ubuntu/). But we can break down the process into a few easy to manage steps:


## 1. Prepare the System
We like to start with a clean slate.

```bash
sudo apt remove -y docker docker-engine docker.io containerd runc # Clean-slate
```

Then let's set up the dependencies we need to get Docker installed.
```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```

Finally, we can add the repository.
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - # Adds the repository key to our list

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update # Fetch the latest updates from our recently added repository
```

If you like to live on the wild-side, you can change the option to `"edge"`, but this may create instabilities with your installation.


## 2. Install Docker
Since we're using Aptitude, installation is a breeze:
```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io
```


## 3. Do a Test Run of Docker
Docker installations can have some really odd error cases. So we're going to do a simple test to ensure everything installed properly before changing the environment further.
```bash
sudo docker run hello-world
```

This will start the basic `hello-world` container that just opens another Ubuntu instance, and echos the following message:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

If you run into issues, this will easily show what went wrong. Follow them or turn to [StackOverflow](https://stackoverflow.com).


## 4. Cleanup
Docker typically requires root access because the running containers will share the hardware resources with the host system. But we can configure specific users to granted it root access by default. This is done with the following:
```bash
sudo groupadd docker
sudo usermod -aG docker ${USER}
```

That will add yourself to the `docker` group so you can call it without root privilege (note that you needed root privilege to both generate the group and add yourself to it, so it kinda signals that you're trustworthy).

It's recommended that you reboot the system at this point. Most tutorials and Docker's own documentation says log out and back in again, but a refresh of the running state can shake out other issues. After rebooting, you should be able to re-run the `hello-world` container without needing root privilege.



# Ok, So What Do I Do With Docker?
There is an endless sea of tutorials that can walk anyone through every facet of how to use, manipulate, configure, launch, and store Docker containers. Instead, we're going to focus on the minimum subset of what's needed to install and launch our container.

Though [DockerHub](https://hub.docker.com/) is a very popular way of distributing containers, we're instead going to focus on constructing one "from scratch" using a *Dockerfile*. The main motivation behind this two-fold: First, those files are very small and easier to share around. The other is because you can embed specific instructions to match it to the host-system's user instead of relying on a generic user.



# The `ROS_Box` Container
To begin, you'll need to download the [Dockerfile](https://github.com/jhill515/RosBox/blob/main/Dockerfile) attached to this article (MD5 Checksum = `390750aec555944b0e6ac24a9e4917c8`). I won't walk through how to construct this file, but you can check out [Docker for Beginners](https://docker-curriculum.com/#dockerfile) by [Prakhar Srivastav](https://prakhar.me/) to understand the details.

Building is generally a breeze, but we should specify two arguments...

```bash
docker build --build-arg TZ=`cat /etc/timezone` \ # Set timezone
             --build-arg USR=${USER} \            # Create a default user for yourself
             -t rosbox:1.0 .                      # Tag your build with a meaningful name and use Dockerfile here
```

This extends the *Open Source Robotics Foundation*'s container with Ubuntu 20.04 and ROS Noetic with the full desktop package. This also includes Gazebo and a number of other packages & utilities to get started on virtually any development project.

The build takes a little while, but you can observe what it's doing as it runs.



# Ensuring Graphical Support
This can be a bit tricky, but ultimately it involves ensuring that when we run the container, Docker has the right interfaces available. Essentially, we need the following when we run:

```bash
docker run -it \                                               # Just starts the interactive session
           --hostname rosbox \                                 # Use a good name
           --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \ # Use the host's display authority credentials
           --env="DISPLAY" \                                   # Turn the display on
           --net=host \                                        # Use the host's network connections
           rosbox:1.0                                          # Run the container we just built
```
