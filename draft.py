from subprocess import check_output, CalledProcessError, STDOUT

# only Digital Ocean for now
def connect(token):
  f = open("debug.txt", "w")

  machine_output = None
  try:
      machine_output = check_output([
      "docker-machine", "create", "-d", "digitalocean",
      "--digitalocean-access-token="+token, "lab-container-api"
      ], stderr=STDOUT)
  except CalledProcessError:
      print machine_output

  f.close()

connect("f8edd967671537a7d77ed65ac992296b89940032df26aa1345ce9d23b68fcf84")
