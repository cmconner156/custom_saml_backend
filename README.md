# custom_saml_backend
Backend for remapping SAML username to another username.  Steps to use:

1.  Edit customsamlbackend.py and alter the variable username to match whatever you need and return the username.  It currently strips anything after the "@".

2.  Create a local directory on each Hue server.  Recommendations:

  - /var/lib/hue/customsamlbackend - If not using CM
  - /opt/cloudera/customsamlbackend - If using CM

3.  Copy the customsamlbackend.py and samlsettings.py to the local directory on each Hue server.

4.  Set the following environment variables before starting Hue.  If using CM, these go in the Hue Configuration in "Hue Service Environment Advanced Configuration Snippet (Safety Valve)"

  PYTHONPATH=/opt/cloudera/customsamlbackend #/var/lib/hue/customsamlbackend if no CM
  DJANGO_SETTINGS_MODULE=samlsettings #This is the name of the samlsettings file, should be samlsettings
5.  Set the backend to the custom backend in your Hue config:

[desktop]
redirect_whitelist="^\/.*$,^https:\/\/shibboleth.test.com\/.*$"
[[auth]]
backend=customsamlbackend.CustomSAML2Backend

6.  Restart Hue after properly configuring for SAML.  If you add "DEBUG=true" and "DESKTOP_DEBUG=true" to the "Hue Service Environment Advanced Configuration S    nippet (Safety Valve)" before restarting, you can check the "/var/run/cloudera-scm-agent/process/<id>-hue-HUE_SERVER/logs/stderr.log" for these messages to confirm it's in use:

Using CustomSAML2Backend
Mapping username from XXX to YYY
Using custom samlsettings
