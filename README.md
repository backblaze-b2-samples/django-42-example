# Django 4.2 with Backblaze B2

This is a minimal sample app that shows how to use Backblaze B2 as the default storage backend with [Django](https://www.djangoproject.com/) and [django-storages](https://django-storages.readthedocs.io/en/latest/index.html). The sample targets Django 4.2 and above, since storage configuration changed in that version.

To configure the app with your own Backblaze B2 application key and bucket, copy `mysite/.env-template` to `mysite/.env` and edit it as appropriate:

```
B2_APPLICATION_KEY_ID=<Your Backblaze B2 Application Key ID>
B2_APPLICATION_KEY=<Your Backblaze B2 Application Key>
B2_BUCKET_NAME=<Your Backblaze B2 bucket name>
B2_REGION=<Your Backblaze B2 bucket's region>
```

The region is the section of the bucket's endpoint between `s3.` and `.backblazeb2.com`. For example, if your bucket has the endpoint `s3.us-west-004.backblazeb2.com`, then its region is `us-west-004`.
