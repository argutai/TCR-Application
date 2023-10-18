## Repository for TCR application

### About

Application for sharing TCR sequencing analyses.

This Flask application is configured to be deployed to an Apache2 server with WSGI, and is currently hosted on a VM on KCL’s CREATE cloud.

### Run locally for development

Clone repo. Install dependencies:

- python, pip
- Pip install flask, pandas, os, flask_sqlalchemy

From root directory, run `python flaskapp.py`, and connect to [localhost:5000](http://localhost:5000) on browser.

### Steps for updating deployment

Project name: **er_prj_tcr_analytics**. Request access from argutai. The name of the VM instance is TCR-Analytics which has an IP address [10.211.116.43](mailto:ubuntu@10.211.116.43). 

Connecting to VM from local requires King’s VPN. Install Tunnelblick. Follow steps on https://docs.er.kcl.ac.uk/CREATE/tools/openvpn/ to create an OpenVPN certificate to connect to VPN. Once configured, `ssh` into VM with

```bash
ssh -J <your-v-number>@bastion.er.kcl.ac.uk [ubuntu@10.211.116.43](mailto:ubuntu@10.211.116.43)
```

Once successfully signed in, you should see this git repository in the root directory:

```
.
└── flaskapp/
    ├── app/
    │   ├── __init__.py
    │   ├── logic.py  
    │   ├── models.py  
    │   ├── routes.py  
    │   └── static/
    │       ├── KCL-content/
    │       │   ├── figures/
    │       │   └── metadata/
    │       ├── main.css
    │       └── templates/
    ├── flaskapp.py
    └── flaskapp.wsgi
```

To update the application after changes to this repository, `cd flaskapp` and run: 

```
bash ./operations/deploy.sh <KCL-email-address> <password>
```

This will pull the latest version of the TCR app and update the git submodule containing all of the content and figures. It then reloads apache to actualise the changes and sends a HTTP request to the server to check if it is working as expected. You must enter an email and password for the documentation page to work correctly as it automatically updates from a word document on sharepoint. If you receive an error, debug with:

```
sudo systemctl status apache2.service
cat /var/log/apache2/error.log
```

Check the server to see app is running as expected:

https://tcr-analysis.sites.er.kcl.ac.uk