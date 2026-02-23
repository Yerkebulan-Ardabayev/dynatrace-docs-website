---
title: Log rotation patterns (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-rotation-patterns
scraped: 2026-02-23T21:28:27.017884
---

# Log rotation patterns (Logs Classic)

# Log rotation patterns (Logs Classic)

* Explanation
* 3-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace monitors rotation patterns for log files. This functionality ensures the completeness of the file reading process, even if OneAgent is temporarily switched off or the application crashes. The monitoring process has two dimensions:

* [Rotation tracking based on the file name](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-rotation-patterns#filenametracking "Learn about supported log rotation patterns")
* [Rotation tracking based on log generation type](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-rotation-patterns#gennametracking "Learn about supported log rotation patterns")

## Rotation tracking based on the file name

Typically, rotated log files have their specific rotation identifiers embedded into file names. The rotation identifiers can be an appended timestamp or a counter. For example:

* Active log file with no rotation identifier:  
  `/var/log/application.log`
* Rotated/archived log files with appended identifiers as date stamp:  
  `/var/log/application.log.20220509`  
  `/var/log/application.log.20220508`  
  â¦  
  `/var/log/application.log.20220503`
* Rotated/archived log files with appended identifiers as counter:  
  `/var/log/application.log.1`  
  `/var/log/application.log.2`

### Rotation identifier and the log name

Depending on the file type, Dynatrace might replace the rotation identifier with the `#` symbol in the log autodiscovery process.

#### Example of rotation identifier replacement with hashtag

Active log file:
`/var/log/application20220509_060000.log`

Rotated/archived log files:  
`/var/log/application20220509_030000.log`  
`/var/log/application20220508_000000.log`  
`/var/log/application20220508_210000.log`  
â¦  
`/var/log/application20220503_090000.log`

are detected as `/var/log/application#_#.log`

### Supported rotation identifiers

The data types that can be substituted by `#` include:

* Decimal numbers of any length
* Hexadecimal numbers that are at least eight digits long
* Globally unique identifiers (GUIDs), the 128-bit text strings that represent identification (ID)

To be monitored, a rotated log file must contain a rotation identifier preceded **and** followed by one of the predefined separators, including `.` (dot), `-` (hyphen), `_` (underscore), `()`(brackets) or `[]` (square brackets).
In a scenario where a rotation identifier is a decimal number, it is sufficient that it is either preceded **or** followed by a predefined separator.

Apart from explicit rotation identifiers visible under the `#` symbol, Dynatrace implicitly supports monitoring of rotated files that:

* Contain a decimal suffix appended to the end of the log name
* Contain a decimal infix instead of any of the predefined separators (`.`, `-`, `_`, `()`, `[]`)

#### Examples of detected rotated log files with implicit identifiers.

Active log file:
`/var/log/application.log`  
Dynatrace detects a file with the '/var/log/application.log' name and identifies rotated files in all examples below:

`/var/log/application.log.1`  
`/var/log/application.log.2`  
â¦  
`/var/log/application.log.9`  
or  
`/var/log/application.20220509.120000.log`  
`/var/log/application.20220509.060000.log`  
`/var/log/application.20220508.120000.log`  
â¦  
`/var/log/application.20220503.120000.log`  
or  
`/var/log/application.20220509.log.1`  
`/var/log/application.20220509.log.2`  
`/var/log/application.20220508.log.1`  
â¦  
`/var/log/application.20220503.log.1`  
`/var/log/application.20220503.log.2`

## Rotation tracking based on log generation type

Dynatrace supports the main types of log generation, including:

* Rotated log generation based on the **'Index'** rule, where the application opens files one by one and provides them with index numbers.
* Rotated log generation based on the **'Rename and replace'** rule, where the application logs to a file with the same name. If a rotation criterion is met (for example, the required file size is reached), a new file with the same name is opened while the old one is renamed.
* Rotated log generation based on the **'Copy and truncate'** rule, where the application logs to a file with the same name, but the rotation itself is performed by an external process that, after a rotation criterion is met, copies the file's content into another location and truncates the content of the original (active) file. The 'logrotate' process on Linux is an example here.

## Log rotation limits

Scenarios that are not supported in the rotated log monitoring process include:

Type

Description

Rotated log generation with a directory change

The potential consequence is the creation of duplicates and/or incomplete logs.

Rotated log generation with immediate compression

If a rotation criterion is met (for example, the required file size is reached), the file is moved to another location and immediately compressed. Example: `/var/log/application.log -> /var/log/application.log.1.gz -> /var/log/application.log.2.gz -> /var/log/application.log.3.gz`. This process might again lead to incomplete log ingest. There should be at least one uncompressed rotated file.

Rotated log generation with queue logic

The oldest log records are removed whenever new content is added to a file, resulting in a relatively constant log file size. This scenario can be easily replaced with a supported rotation scheme by, for example, starting a new file when the current file reaches a predefined size.