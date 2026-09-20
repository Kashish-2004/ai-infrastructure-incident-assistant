# Disk Usage Troubleshooting Runbook

## Problem 
Disk usage is critically high.

## Possible Causes
- Large log files
- Temporary files
- Old application files
- Database or backup files consuming too much

## Investigation Steps
1. Check which directories are consuming the most disk space.
2. Identify unusually large log files.
3. Check temporary files and caches.
4. Check old backups or unused application files.


## Recommended Actions
- Remove unnecessary temporary files.
- Archive or rotate old logs.
- Remove obsolete backups after verification.
- Do not delete important application or database files without confirmation.

## Safety
Destructive cleanup actions should require human approval.