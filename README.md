# Home network monitoring ETL

This repo setup the home network monitoring ETL.

## Use

Launch ETL using `python etl.py`.

> It is mandatory to use this soft using `sudo` privileges.

## Configuration

The configuration file should be called `etl-configuration.json` and be structured as :

```JSON
{
    "monitoring_delay": 5,
    "routines_delay": 3600,
    "entities": [
        {
            "ip": "127.0.0.1",
            "domain": "localhost",
            "description": "loopback of current machine"
        },
        ...
    ]
}
```

## Troubleshooting

The ETL should launch some database routines every X seconds, defined in configuration file. If for some reason, it does not work, the module can be call such as `python database_routines.py`.