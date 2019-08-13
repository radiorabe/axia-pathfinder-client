# axia-pathfinder-client

This is an early start at writing a python client/sdk for the the telnet based API on [Axia Pathfinder](https://www.telosalliance.com/Axia/Pathfinder-Routing-Control) software/appliances from the [Telos Alliance](https://www.telosalliance.com).

Currently it is more a proof of concept rather than anything ready for production. We have plans to integrate it with our current [songticker glue code](https://github.com/radiorabe/nowplaying).

Please raise an [issue](https://github.com/radiorabe/axia-pathfinder-client/issues) if you would like to collaborate with [Radio Bern RaBe](https://www.rabe.ch) on this python/pathfinder integration effort. We plan on primarily focusing this library on our needs but contributions are always welcome and we would be happy to accomodate you!

## Features

* partially implements the "SAPv2" protocol as described in the [pathfinder manual](https://www.telosalliance.com/images/Axia%20Products/Pathfinder%20PC/Support%20Files/PathFinder%20PC%20Manual-5.00.pdf)
  * only "LOGIN" and "GET" operators are currently supported
  * "INDI" responses to "GET" requests get parsed and returned in a timeout governed timeout fashion
* Uses a PEG-style parser-combinator based on [parsy](https://github.com/python-parsy/parsy) to parse responses from the telnet interface

## Contributing

Please let us know what you would like to contribute before you get invested! This is really a proof of concept at this stage.

### pre-commit hook

```bash
pip install pre-commit
pip install -r requirements-dev.txt -U
pre-commit install
```

### Testing

```bash
pytest
```
