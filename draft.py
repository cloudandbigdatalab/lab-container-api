from subprocess import check_output, CalledProcessError, STDOUT
import os

def connect(token):
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

connect(os.environ['DO_KEY'])
