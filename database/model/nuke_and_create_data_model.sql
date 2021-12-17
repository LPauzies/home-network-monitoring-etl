-- Nuke the current data model
DROP TABLE IF EXISTS Ping;

-- Create the Ping table which contains every entries from network pinger etl
CREATE TABLE IF NOT EXISTS Ping (
    EventTime INTEGER NOT NULL, -- Timestamp (in milliseconds) of the time since 1st January 1970
	IP TEXT NOT NULL, -- Should have the RFC IP format
   	DomainName TEXT, -- Should be the domain name resolved above IP column
	IPDescription TEXT, -- Should describe the given IP
	ResponseTime REAL NOT NULL, -- Should represent the latency between current IP and home network
    PacketLoss INTEGER NOT NULL, -- Should be 0 or 1 for True/False
	PRIMARY KEY (EventTime, IP) -- Primary key on EventTime + IP should be unique
);