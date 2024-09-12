
* [Postgres is a great pub/sub & job server (2019)](https://webapp.io/blog/postgres-is-the-answer/)
* [Get Away with Just PostgreSQL (2021)](https://spin.atomicobject.com/redis-postgresql/)
* [Choose Postgres queue technology (2023)](https://adriano.fyi/posts/2023-09-24-choose-postgres-queue-technology/)

```sql
BEGIN;
WITH job AS (
  SELECT id FROM jobs WHERE status = 'pending'
  LIMIT 1 FOR UPDATE SKIP LOCKED
) UPDATE jobs SET status = 'running'
WHERE jobs.id = job.id RETURNING jobs.*;
COMMIT;
```

![[Pasted image 20240912160834.png]]

```sql
CREATE OR REPLACE FUNCTION ci_jobs_status_notify()
	RETURNS trigger AS
$$
BEGIN
	PERFORM pg_notify('ci_jobs_status_channel', NEW.id::text);
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER ci_jobs_status
	AFTER INSERT OR UPDATE OF status
	ON ci_jobs
	FOR EACH ROW
EXECUTE PROCEDURE ci_jobs_status_notify();
```

```go
make(chan interface{}) //equivalent to 'LISTEN ci_jobs_status_channel;'
listener.Listen("ci_jobs_status_channel")
go func() {
  for event := range listener.Notify {
    select {
      case tryPickupJob <- true:
    }
  }
  close(tryPickupJob)
}
for job := range tryPickupJob { //try to "claim" a job }
```
