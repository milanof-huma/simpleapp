# simpleapp

## How to Run : 

    `helmfile apply`


## Info: 

    1. Application is running in `dev` ns
    2. monitoring (grafana and loki) is running in `monitoring` ns
    3. Use this to get grafana password (user is `admin`): 

    kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo


    4. use this to view Grafana on local : 
    kubectl  port-forward service/grafana 3081:80 -n monitoring

    5. Dashboard id is 12777 (https://grafana.com/grafana/dashboards/12777)

    6. Alerts and Conditions are set in Dashboard itself as json
        a. For every 500, slack notification will trigger
        b. If for any 5 minute period, number of 401s > 10 , then it will trigger the slack notification. 

        Both conditions are check every 10s.
    7. DataSource is in grafana/values.yaml
    8. Slack notification channel is in grafana/values.yaml


Note: Tried adding dashboard from json and comfigMap, but it was not allowing me to do so, so had to host it.