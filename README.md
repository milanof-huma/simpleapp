# This is a simple web app serving as a helmfile spec example

## About

Simpleapp is a simple web app on flask/python:3.8

Navigate to http://localhost:5000/log

Expected output:

`{'bar': 'foobar'}`

[Helmfile](https://github.com/roboll/helmfile) is a declarative spec for deploying helm charts. It lets you...

- Keep a directory of chart value files and maintain changes in version control.
- Apply CI/CD to configuration changes.
- Periodically sync to avoid skew in environments.

## Generate charts

    $ helmfile repos
    Adding repo stable https://charts.helm.sh/stable
    "stable" has been added to your repositories

**A lot of YAML files should be in output like:**

    $ helmfile template --skip-deps
    Templating release=ingress-controller, chart=stable/nginx-ingress
    ---
    apiVersion: v1
    kind: Pod
    metadata:
    name: "simpleapp-test-connection"
    labels:
        helm.sh/chart: simpleapp-0.1.0
        app.kubernetes.io/name: simpleapp
        app.kubernetes.io/instance: simpleapp
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    annotations:
        "helm.sh/hook": test-success
    spec:
    containers:
        - name: wget
        image: busybox
        command: ['wget']
        args: ['simpleapp:5000']
    restartPolicy: Never

## Checked tools versions

        $ helmfile -v
        helmfile version v0.138.4
        $ helm version 
        version.BuildInfo{Version:"v3.5.2", GitCommit:"167aac70832d3a384f65f9745335e9fb40169dc2", GitTreeState:"dirty", GoVersion:"go1.15.7"}
