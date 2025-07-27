CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE file (
    id SERIAL PRIMARY KEY,
    file_name TEXT NOT NULL,
    mime_type TEXT,
    object_key TEXT NOT NULL,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE chunk (
    id SERIAL PRIMARY KEY,
    file_id INTEGER NOT NULL REFERENCES file(id) ON DELETE CASCADE,
    chunk_index INTEGER NOT NULL,
    chunk_text TEXT NOT NULL,
    embedding vector(1536) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);