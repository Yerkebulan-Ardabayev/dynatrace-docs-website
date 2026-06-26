# Что ещё нужно перевести (EN -> RU)

**Готово: 2637 / 2698 (97.74%).**

- **Активный перевод (`ingest-from`): осталось 23 файлов** — это реальная работа.
- Прочие/legacy страницы: 38 (топ-левел / cluster-API, управляются CI-рескрейпом, низкий приоритет).

> Генерируется автоматически: `python scripts/_gen_pending_md.py`.
> Как доперевести: открыть Claude Code в этой папке и сказать, например:
> «продолжай перевод раздела amazon-web-services по тому же пайплайну (движок `_zos_canon_l4if71`, глоссарий, субагенты, QA, крит.ревью)».
> EN-исходник: `docs/managed/<путь>` -> RU-результат: `docs/managed-ru/<путь>`.

## Активный перевод — ingest-from

### ingest-from/google-cloud-platform  (15)

- [ ] `ingest-from/google-cloud-platform/gcp-integrations/cloudrun.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only.md`
- [ ] `ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster.md`
- [ ] `ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy.md`
- [ ] `ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy.md`
- [ ] `ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy.md`

### ingest-from/technology-support  (6)

- [ ] `ingest-from/technology-support/application-software/go/support/go-known-limitations.md`
- [ ] `ingest-from/technology-support/application-software/java/graalvm-native-image.md`
- [ ] `ingest-from/technology-support/application-software/java/quarkus.md`
- [ ] `ingest-from/technology-support/application-software/nginx.md`
- [ ] `ingest-from/technology-support/application-software/nginx/kong-gateway.md`
- [ ] `ingest-from/technology-support/known-solutions-and-workarounds.md`

### ingest-from/setup-on-container-platforms  (2)

- [ ] `ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy.md`
- [ ] `ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-openshift-legacy.md`

## Прочие / legacy (низкий приоритет, управляется CI)

### managed-cluster/api-references  (30)

- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/create-cluster-tokens.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/delete-cluster-token.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-para.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-req.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-tokens.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/update-cluster-token.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/environments/create-managed-environment.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/environments/delete-specific-managed-environment.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/environments/list-managed-environments.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/environments/list-specific-managed-environment.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/environments/update-specific-managed-environment.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/export-license-data/get-export-license-data.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/log-monitoring/get-log-monitoring-status.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/log-monitoring/post-update-log-events-per-cluster-for-log-monitoring.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/get-all-cluster-access-requests.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/get-cluster-access-request.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/post-remote-access-permission.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/put-change-access-request-state.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/delete-a-location.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-a-location.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all-locations.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-node.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/post-a-location.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/delete-cluster-user-session.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions-configuration.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions.md`
- [ ] `managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/update-cluster-user-sessions-configuration.md`

### backup.md  (1)

- [ ] `backup.md`

### cluster.md  (1)

- [ ] `cluster.md`

### configuration.md  (1)

- [ ] `configuration.md`

### installation.md  (1)

- [ ] `installation.md`

### managed.md  (1)

- [ ] `managed.md`

### operations.md  (1)

- [ ] `operations.md`

### security.md  (1)

- [ ] `security.md`

### update.md  (1)

- [ ] `update.md`

