from getpass import getpass
import hashlib
import random
import string
import sys
from utils.dbconfig import dbconfig

from rich import print as printc
from rich.console import Console

console = Console()


def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def config():
    # Create database
    db = dbconfig()
    cursor = db.cursor()
    try:
        cursor.execute("CREATE DATABASE pm")
    except Exception as e:
        printc("[red][!] An error occurred while trying to create db. Check if database with name 'pm' already exists - if it does, delete it and try again.")
        console.print_exception(show_locals=True)
        sys.exit(0)
        
    printc("[green][+][/green] Database 'pm' created")

    # Create tables
    query = "CREATE TABLE pm.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created")

    query = "CREATE TABLE pm.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, " \
            "password TEXT NOT NULL) "
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created")

    # GETTING the mainPASSWORD
    while True:
        mp = getpass("Enter a MASTER PASSWORD: ")
        if mp == getpass("Renter the MASTER PASSWORD: ") and mp:
            break
        printc("[yellow][-] Please try again. [/yellow]")

    # hash MASTERPASSWORD
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of MASTER PASSWORD")

    # Generate device secret
    ds = generateDeviceSecret()
    printc("[green][+][/green] Device Secret Generated")

    # Add to db
    query = "INSERT INTO pm.secrets (masterkey_hash, device_secret) values (%s, %s)"
    val = (hashed_mp, ds)
    cursor.execute(query, val)
    db.commit()

    printc("[green][+][/green] Added to DB")
    printc("[green][+][/green] Config Done!!!")
    db.close()


config()
