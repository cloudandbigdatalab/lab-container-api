# lab-container-api
Service / API to automate creating Docker containers for online tutorials and labs.

Essentially we want to provide a service / API framework that quickly spins up working environments or runs app processes that coincide with a Coursera, CodeAcademy, etc. type tutorial. The user will provide credentials to some cloud service (Google, Rackspace, Chameleon, Digital Ocean, Amazon, etc.). We then create a docker host for our API if one does not exist. We then run containers on this host. The goal of the service is to instantly (or as quickly, painlessly as possible) get a user into a working environment or running some app. They won't have to configure anything.

The API will take their credentials, an id or name for an image hosted on Docker Hub (or some other docker image repo), create a host (if one does not already exist), and then return the SSH login information.

A UI implementation would look like:
- they're on a tutorial site
- they enter their credentials in
- they're go to a tutoial
- they click "launch lab"
- they're given a terminal in the browser
- they can start coding, experimenting, etc.
- they didn't have to set up anything

## Phase 1: Discovery
- look at what's currenlty available / see if people have already done it
- if they have, is it open source? and is there a meaningful, different way to do it? is there room for improvement?

**Results**  
I found several services that *kind of* relate to this but aren't exaclty what we're thinking of. Many of them require you to use a CLI. I didn't find any accessbile via a RESTful API. They all seem to manage containers like many services manage VMs. But nothing that just returns a login for you. List of services I looked at:
- Tutum
- Orchard
- dotCloud
- StackDock
- Quay.io
- Container Engine
- sloppy.io
- chef
- 

# Phase 2: Script Through Flow
Going to setup the flow in shell scripts.
