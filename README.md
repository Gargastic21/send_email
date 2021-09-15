# This repo is to run flask and send mail to the users.

Flask is the main library for which we perform tasks.
## Installation

create ec2 instance, api gateway, lambda, dynamo db.

```bash
pip install flask
```
send_email_dynamo_SES_Lambda.py-->

integrating dynamo DB with AWS SES in Lambda. Also, Lambda is being triggered from the API gateway. API gateway is being triggered from the flask script present in ec2. 


python script flask running on ec2 instance. --->app.py
## Usage

```python
python app.py
or
python3 app.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
