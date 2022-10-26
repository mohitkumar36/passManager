# passManager

A secure GUI password manager which keeps your password locally stored in your PC. Written using Python, PyQt5, MySQL. Uses [pbkdf2](https://en.wikipedia.org/wiki/PBKDF2) to derive a 256 bit key from a MASTER PASSWORD and DEVICE SECRET to use with AES-256 for encrypting/decrypting.


## Installation
You need to have python3 and MySQL to run this on Windows.
### Requirements
```
pip install -r requirements.txt
```

### Setting up the Database

- Login as root with the password you chose while installation
```
mysql.exe -u root -p
```
- Create user
```
CREATE USER 'pm'@localhost IDENTIFIED BY 'password';
```
- Grant privileges
```
GRANT ALL PRIVILEGES ON *.* TO 'pm'@localhost IDENTIFIED BY 'password';
```

## Run

### Configure

You need to first configure the password manager by choosing a MASTER PASSWORD. This config step is only required to be executed once.
```
python config.py make
```
The above command will make a new configuration by asking you to choose a MASTER PASSWORD.
This will generate the DEVICE SECRET, create db and required tables.

```
python config.py delete
```
The above command will delete the existing configuration. Doing this will completely delete your device secret and all your entries and you will loose all your passwords. So be aware!

```
python config.py remake
```
The above command will first delete the existing configuration and create a fresh new configuration by asking you to choose a MASTER PASSWORD, generate the DEVICE SECRET, create the db and required tables.

## Usage

Navigate to the below folder

```
./scr/utils
```

Run the loginUI.py file and you can manage your entries and also generate a password.

```
py loginUI.py
```

## Screenshots

![Screenshot_20221026_163002](https://user-images.githubusercontent.com/57846872/198010004-f27fe6cd-0c56-40fb-84e0-37fb7e022e70.png)


![Screenshot_20221026_163028](https://user-images.githubusercontent.com/57846872/198010064-99b3e5a8-e13c-4ab4-a09b-b2ba26b5608f.png)


![Screenshot_20221026_163058](https://user-images.githubusercontent.com/57846872/198010076-cce968b4-64bc-493f-a72e-39e0f0fa4f0f.png)


![Screenshot_20221026_163113](https://user-images.githubusercontent.com/57846872/198010095-1d46eedb-f7e7-47c1-a715-b9819ada3be7.png)


