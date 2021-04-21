## Quickstart instruction

This sample requires only the default installation of `same` in order to work.

To run it, simply execute the following:

```bash
same program run --experiment-name "Sample calculations" --run-name "FirstRun"
```

To view the results via a UI, use port forwarding:

```bash
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```

Then access it via a browser: [https://localhost:8080](https://localhost:8080)
