## HELM Update: helm_old.yaml → helm_new.yaml
**Timestamp:** 2025-08-20T18:47:58.735932

Here's a summary of the infrastructure diff in plain English:

* The old infrastructure had 2 replicas of the `my-app` service, while the new infrastructure has 3 replicas.
* The old infrastructure used a `ClusterIP` service type, while the new infrastructure uses a `LoadBalancer` service type.
* The old infrastructure exposed port 8080, while the new infrastructure exposes port 443 and 8443.
* The old infrastructure used an image version of `my-app:1.0.0`, while the new infrastructure uses an image version of `my-app:2.0.0`.
* The old infrastructure had a liveness probe that checked the `/health` path every 10 seconds, while the new infrastructure has a liveness probe that checks the `/healthz` path every 5 seconds.
* The old infrastructure had a readiness probe that checked the `/ready` path every 5 seconds, while the new infrastructure has a readiness probe that checks the `/readyz` path every 3 seconds.
* The new infrastructure adds a `LOG_LEVEL` configuration option set to `debug`, and enables the `FEATURE_X_ENABLED` and `FEATURE_Y_ENABLED` features.
* A new secret named `my-app-secret` is created in the new infrastructure, containing a password for the application's database.

