# Dynatrace Managed Overview

Dynatrace Managed is the on-premises deployment option for organizations that require full control over their monitoring infrastructure.

## What is Dynatrace Managed?

Dynatrace Managed provides:

- **On-premises deployment** - Host in your own data center
- **Full data control** - Your data never leaves your environment
- **Compliance** - Meet regulatory requirements
- **Same features** - All capabilities of Dynatrace SaaS

## Architecture

```
┌─────────────────────────────────────────┐
│         Managed Cluster                 │
│  ┌───────────────────────────────────┐  │
│  │   Cluster Management Console       │  │
│  └───────────────────────────────────┘  │
│  ┌───────────────────────────────────┐  │
│  │   Cluster Nodes                    │  │
│  │   - Processing                     │  │
│  │   - Storage                        │  │
│  │   - UI                             │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
           ↑
           │ Monitoring data
           │
    ┌──────┴───────┐
    │  OneAgents   │
    │  (deployed   │
    │  on hosts)   │
    └──────────────┘
```

## Key Features

### Data Sovereignty
- All data stored on-premises
- No data transmission to Dynatrace cloud
- Full control over data retention

### Customization
- Custom integrations
- Private network deployment
- Flexible sizing options

### High Availability
- Multi-node cluster setup
- Automatic failover
- Disaster recovery options

## System Requirements

### Minimum Requirements

- **CPU:** 8 cores
- **RAM:** 32 GB
- **Storage:** 200 GB (SSD recommended)
- **OS:** Linux (Ubuntu, RHEL, SUSE)

### Recommended for Production

- **CPU:** 16+ cores
- **RAM:** 64+ GB
- **Storage:** 500+ GB SSD
- **Network:** 1 Gbps+

## Installation

See our [Installation Guide](installation.md) for detailed instructions.

## When to Choose Managed?

Choose Dynatrace Managed if you need:

- ✅ On-premises deployment
- ✅ Data sovereignty
- ✅ Air-gapped environments
- ✅ Custom compliance requirements
- ✅ Integration with private networks

## Next Steps

- [📥 Installation Guide](installation.md)
- [⚙️ Configuration](configuration.md)
- [🔧 Maintenance](maintenance md)
- [🆘 Troubleshooting](troubleshooting.md)

## Need Help?

- 🤖 [Quick questions - AI Chat](../../ai/gemini.md)
- 🔬 [Complex analysis - NotebookLM](../../ai/notebooklm.md)
