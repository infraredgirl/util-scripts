aws
============

Amazon Web Services utility scripts.  
Written in Python using [boto](https://github.com/boto/boto/).

First, edit the configuration file `aws_settings.py` to specify your own AWS settings data.


### EC2 utilities (ec2.py)

Currently supported functionalities:

* `stop_non_production_instances()` finds and stops all non-production AWS EC2 instances.
Production instances are inferred by the key and value of the tag given to them. Make sure you specify this in the
configuration file.
* `start_non_production_instances()` finds and starts all stopped non-production instances. In addition, it associates
every instance with its elastic ip address, if this value has been provided in the configuration file.

```python
>>> from ec2 import stop_non_production_instances, start_non_production_instances


>>> stop_non_production_instances()

Connecting to region your-region with access key id = YOUR-AWS-ACCESS-KEY-ID and secret access key = YOUR-AWS-SECRET-ACCESS-KEY ...
Connected.
Getting non-production instances ...
Found 2 instances.
Stopping 2 non-production instances ...
	Instance i-aaaaaaaa stopped.
	Instance i-bbbbbbbb stopped.
Done stopping instances.


>>> start_non_production_instances()

Connecting to region your-region with access key id = YOUR-AWS-ACCESS-KEY-ID and secret access key = YOUR-AWS-SECRET-ACCESS-KEY ...
Connected.
Getting non-production instances ...
Found 2 instances.
Starting 2 non-production instances ...
	Instance i-aaaaaaaa stopped.
	Instance i-aaaaaaaa pending.
	Instance i-aaaaaaaa pending.
	Instance i-aaaaaaaa running.
	Instance i-aaaaaaaa associated to elastic ip 1.2.3.4.
	Instance i-bbbbbbbb stopped.
	Instance i-bbbbbbbb pending.
	Instance i-bbbbbbbb pending.
	Instance i-bbbbbbbb running.
	Instance i-bbbbbbbb associated to elastic ip 5.6.7.8.
Done starting instances.
```
