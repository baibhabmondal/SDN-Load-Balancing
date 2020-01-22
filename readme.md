### Common commands

---

* Running onos on Baibhab's system:

```
> sudo /opt/onos-2.0.0/bin/onos-service [clean | start]
```
* Navigate to 

```
cd /home/baibhab/mininet/custom/Load

(Make sure to replace the path with your directory)
```
* Now you are on the current directory
* Run the main python file, which in turn runs mininet

```
sudo mn -c
sudo python ./onos2.py
```

* Important mininet commands

```
sudo mn -c  (to clean)

mininet> nodes (to display nodes)
mininet> pingall (to test connections)
mininet> xterm h1 (any  nodename; to open terminal for the particular node)

mininet> iperf n0 (any node; to measure bandwidth)
```

* ONOS GUI:

```
27.0.0.1:8181/onos/ui/  

(username: onos; passwd: rocks)

```

* Enable following applications:

```Control Message Stats Provider
Control Plane Manager
Default Drivers
Host Location Provider
LLDP Link Provider
OpenFlow Base Provider
OpenFlow Provider Suite
Optical Network Model
Reactive Forwarding
```
