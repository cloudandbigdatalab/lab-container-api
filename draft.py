import subprocess

# only Digital Ocean for now
def connect(token):
  f = open("debug.txt", "w")
  subprocess.check_call(["docker-machine", "create", "-d", "digitalocean", "--digitalocean-access-token="+token, "lab-container-api"], stdout=f, stderr=subprocess.STDOUT)
  f.close()

connect("f8edd967671537a7d77ed65ac992296b89940032df26aa1345ce9d23b68fcf84")
