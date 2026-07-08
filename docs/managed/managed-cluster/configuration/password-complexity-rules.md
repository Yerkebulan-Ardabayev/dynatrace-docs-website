---
title: Password complexity rules
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/password-complexity-rules
---

# Password complexity rules

# Password complexity rules

* Reference
* 2-min read
* Updated on Jun 18, 2026

Password complexity rules define the configuration details, best practices, and default values for the **Password policy** settings. The password complexity rules apply only to the embedded administrator account and internal user accounts (see [User groups and permissions](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Learn about the supported permissions and policies, how you can assign them to groups, and how you can manage your users and groups.")). When the password policy changes, Dynatrace prompts all users to update their passwords the next time they sign in.

The **Password policy** settings force passwords to meet a series of strong-password guidelines. You can configure passwords to meet the following requirements:

1. The password contains a minimum number of alphanumeric characters.
2. The password contains a minimum number of characters from the following categories:

   * Uppercase Latin alphabet letters (`A` through `Z`, with diacritic marks)
   * Lowercase Latin alphabet letters (`a` through `z`, sharp-s, with diacritic marks)
   * Base 10 digits (`0` through `9`)
   * Non-alphanumeric characters (special characters): (`` ~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/ ``) Currency symbols such as the Euro or British Pound aren't counted as special characters for this policy setting.

Dynatrace enforces complexity requirements when users change or create passwords.

## Default values

The following table lists the actual and effective default policy values. Default values are also listed on the **Password policy** page. The value range for the policy properties is between `8` and `128` for the **Minimum password length** property and between `0` and `128` for other policy properties.

| Policy property name | Default value | Recommended |
| --- | --- | --- |
| Minimum password length | `8` for existing Managed Clusters installed before 1.206 `12` for new Managed Clusters installed in or after 1.206 | `12` |
| Minimum number of uppercase characters | `1` | `1` |
| Minimum number of lowercase characters | `1` | `1` |
| Minimum number of digits | `1` | `1` |
| Minimum number of non-alphanumeric characters | `0` | `any` |

## Best practices

Since 2013, the "NIST Special Publication 800-63. Appendix A" advises to include in passwords irregular capitalization, special characters, and at least one numeral. Change passwords at least every 90 days. Most systems follow this guidance, and many standards that businesses must comply with incorporate it.

* Maintain the 12-character minimum length requirement (longer length requirement isn’t necessarily better).
* Enforce a combination of uppercase, lowercase, digits, and non-alphanumeric characters.
* Educate your users not to reuse their Dynatrace passwords for non-Dynatrace purposes.
* If possible, use your organization’s central user repository service (LDAP or SSO).