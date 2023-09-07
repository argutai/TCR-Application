## Repository for TCR application

### About

Application for sharing TCR sequencing analyses.

This Flask application is configured to be deployed to an Apache2 server with WSGI, and is currently hosted on a VM on KCL’s CREATE cloud.

### Steps for updating deployment

Project name: **er_prj_tcr_analytics**. Request access from argutai@hotmail.com. The name of the VM instance is TCR-Analytics which has an IP address [10.211.116.43](mailto:ubuntu@10.211.116.43). 

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
    │       │   │   ├── Sample_bubbles/
    │       │   │   ├── Sample_expanded_heatmaps/
    │       │   │   ├── clonotype_count/
    │       │   │   └── clonotype_proportions/
    │       │   └── metadata/
    │       │       └── metadata.txt
    │       ├── main.css
    │       └── templates/
    │           ├── layout.html
    │           ├── home.html
    │           ├── overview.html
    │           └── patients.html
    ├── flaskapp.py
    ├── flaskapp.wsgi
    └── instance
```

To update the application after changes to this repository, `cd flaskapp`, and `git pull`. To update the content after update to analytical content (KCL-content), you will need to update the git submodule which points to a separate private repository: 

```
git submodule update --init --recursive
git submodule update --recursive --remote
```

To actualise any changes to code to deployment, you will need to reload Apache:

```bash
sudo systemctl reload apache2
curl https://localhost:443 --insecure

# To debug:
sudo systemctl status apache2.service
cat /var/log/apache2/error.log
```

Check the server to see app is running as expected:

https://tcr-analysis.sites.er.kcl.ac.uk/patients