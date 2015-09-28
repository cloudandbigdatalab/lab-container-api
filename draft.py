from subprocess import check_output, CalledProcessError, STDOUT
import os

def create(token):
    try:
        output = check_output([
        "docker-machine",
        "create",
        "-d",
        "digitalocean",
        "--digitalocean-access-token="+token,
        "lab-container-api"
        ], stderr=STDOUT)
        print output
    except CalledProcessError as error:
        print error.output


def delete():
    try:
        output = check_output([
        "docker-machine",
        "rm",
        "lab-container-api"
        ], stderr=STDOUT)
        print output
    except CalledProcessError as error:
        print error.output


def run(image_name):
    try:
        output = check_output([
        "docker",
        "run",
        "-it",
        "--rm",
        image_name
        ], stderr=STDOUT)
        print output
    except CalledProcessError as error:
        print error.output
