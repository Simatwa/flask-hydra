# flask-hydra
> Server for testing http login attack with hydra
## Installation

1. Install [addtopath](https://github.com/Simatwa/addtopath)
2. Clone repo 

```sh
git clone https://github.com/Simatwa/flask-hydra.git
cd flask-gydra
```

3. Execute `$ addtopath main.py flask-hydra`

## Usage

- `$ flask-hydra`
- By default the server will be hosted locally on port `8000`

<details>

<summary>

* For more info run `$ flask-hydra --help`

</summary>

```
usage: flask-hydra [--help] [-u USER] [-p PASS]
                   [host] [port]

Server for testing password attacks - hydra

positional arguments:
  host                  Address for hosting the server -
                        127.0.0.1
  port                  Port to listen at - 8000

options:
  --help                Show this help mesage and exit
  -u USER, --username USER
                        Login username - admin
  -p PASS, --password PASS
                        Login password - dommy

#POST /login/post #GET /login/get user=^USER^&pass=^PASS^
```
</details>
