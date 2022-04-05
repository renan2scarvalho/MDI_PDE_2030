"""
    Description:

    Implementa uma funcionalidade que o Boto3 da AWS
    não possui que é baixar apenas os arquivos selecionados
    por uma expressão regular.

    Author:           @Thales/Palin
    Created:          2021-05-17
    Copyright:        (c) Ampere Consultoria Ltda
"""

import sys

try:
    import re

    import boto3
    from dynaconf import Dynaconf

    settings = Dynaconf(
        envvar_prefix="AMPERE",
        settings_files=["settings.toml", ".secrets.toml"],
        environments=True,
        load_dotenv=True,
    )

except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")
except Exception as exception:
    print(exception)
    sys.exit()


def filtra_arquivos_S3_por_regex(bucket="ampere-ecmwf", prefix="", patternRegex=""):
    """
    https://alexwlchan.net/2019/07/listing-s3-keys/
    Generate objects in an S3 bucket.

    :param bucket: Name of the S3 bucket.
    :param prefix: Only fetch objects whose key starts with
        this prefix (optional).
    :param suffix: Only fetch objects whose keys end with
        this suffix (optional).
    """
    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")
    kwargs = {"Bucket": bucket}

    # We can pass the prefix directly to the S3 API.  If the user has passed
    # a tuple or list of prefixes, we go through them one by one.
    if isinstance(prefix, str):
        prefixes = (prefix,)
    else:
        prefixes = prefix

    for key_prefix in prefixes:
        kwargs["Prefix"] = key_prefix

        for page in paginator.paginate(**kwargs):
            try:
                contents = page["Contents"]
            except KeyError:
                break

            for obj in contents:
                key = obj["Key"]
                key_path = key.split("/")
                m = re.search(patternRegex, key_path[1])
                if m is not None:
                    yield obj


def filtra_arquivos_s3_pela_extensao(bucket, prefix="", suffix=""):
    """
    - suffix é como o nome do arquivo termina.
    Ex: se os arquivos chamassem [arq1.gz, arq2.gz, arq3.txt]
    Usando suffix=".gz" retornaria [arq1.gz, arq2.gz]

    Ou Usando suffix="1.gz" retornaria [arq1.gz]

    Generate objects in an S3 bucket.

    :param bucket: Name of the S3 bucket.
    :param prefix: Only fetch objects whose key starts with
        this prefix (optional).
    :param suffix: Only fetch objects whose keys end with
        this suffix (optional).
    """
    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")

    kwargs = {"Bucket": bucket}

    # We can pass the prefix directly to the S3 API.  If the user has passed
    # a tuple or list of prefixes, we go through them one by one.
    if isinstance(prefix, str):
        prefixes = (prefix,)
    else:
        prefixes = prefix

    for key_prefix in prefixes:
        kwargs["Prefix"] = key_prefix

        for page in paginator.paginate(**kwargs):
            try:
                contents = page["Contents"]
            except KeyError:
                break

            for obj in contents:
                key = obj["Key"]
                if key.endswith(suffix):
                    yield obj
