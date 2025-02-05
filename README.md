# TASK 1 SIMPLE API

A simple public api for the HNG stage 0 backend task. it retuns a basic json data.

## Requirements
- git
- python3
- venv


## Getting Started
1 - Activate your virtual environment

2 - Run the folowing commands inside the virtual environment

```shell
git clone https://github.com/hasheddev/01-numbers-api.git
cd 01-numbers-api
pip install -r requirements.txt
python3 api/app.py
```

## Backlink
[HNG Python Backend Developer](https://hng.tech/hire/python-developers)

## API DOCUMENTATION

### ENDPOINT
- GET /api/classify-number
  Retieves information about a number

Request Parameters
- number: integer(required)
  
#### Response Format
  
  - status code 200 json dormatted data abount number
  - status code 400: invalid or missing query parameter number

Example request
Get //api/classify-number?number=371

Example Response
 - success
```
{
    "digit_sum":11,
    "fun_fact":"371 is a narcissistic number."
    ,"is_perfect":false,
    "is_prime":false,
    "number":371,
    "properties":["armstrong","odd"]
}
```

  - error
  
  ```
{
    "number": "alphabet"
    "error": true
}
  ```




