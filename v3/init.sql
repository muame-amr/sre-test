CREATE TABLE IF NOT EXISTS access_logs (
    id SERIAL PRIMARY KEY,
    ip VARCHAR(100),
    timestamp TIMESTAMP
);
