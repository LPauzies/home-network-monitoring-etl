-- Routine to delete last values from 7 last days
DELETE FROM Ping
WHERE EventTime < strftime('%s', datetime('now' , '-7 days'))