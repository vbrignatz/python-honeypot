# Python Honeypot

A proxy filter the data stream based on a secretkey. If the secret key is not given or wrong, the proxy will reroute the traffic to a fakeapp, responding with gibrish data. Otherwise, the traffic is forwarded to the realapp.

## Usage

Start the app with :
```
docker-compose up --build
``` 

To test the app, I use curl. If the `secretkey` is not present in the header, the fakeapp always return the dawn of time : January the 1st of 1970.
```
$ curl -X GET http://vm.local:6969
{"data":"00:00:00 01/01/1970"}
```

If `secretkey` is given, then the realapp will respond with the current time.
```
curl -X GET http://vm.local:6969 --header "secretkey:1234"
{"data":<heure courante>}
```
