* Make sure jenkin is in docker group *
```
sudo sudo usermod -aG docker $USER
sudo usermod -aG docker jenkins
```

** Update the docker.service **

Edit the following file : `vi /usr/lib/systemd/system/docker.service`

* And edit this rule to expose the API : 

`ExecStart=/usr/bin/docker daemon -H unix:// -H tcp://localhost:2375 *`

```
systemctl daemon-reload
systemctl restart docker
```
Restart the jenkins service:

```
sudo /etc/init.d/jenkins restart
```

** Ubuntu 16.04 **

* update /lib/systemd/system/docker.service: *
replace:
`ExecStart=/usr/bin/dockerd fd://`
with
`ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375`

* Update file /etc/init.d/docker*:
replace
`DOCKER_OPTS=`
with
`DOCKER_OPTS="-H tcp://0.0.0.0:2375"`

