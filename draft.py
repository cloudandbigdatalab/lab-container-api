from subprocess import check_output, CalledProcessError, STDOUT
import os
import re

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
        machine_output = check_output([
        "docker-machine",
        "env",
        "lab-container-api",
        ], stderr=STDOUT)

        regex_splits = re.split('^export\s(\w+)=\"(\w)\"$',
        machine_output)

        for token in regex_splits:
            print token+"\n"

        """
        output = check_output([
        "docker",
        "run",
        "-it",
        "--rm",
        image_name
        ], stderr=STDOUT)
        print output
        """
    except CalledProcessError as error:
        print error.output
