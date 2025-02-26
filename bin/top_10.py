#!/usr/bin/python3
import json
import requests
import datetime
import sys
from datetime import timedelta
import os

# Calculate time range for last 24 hours
gte = (datetime.datetime.utcnow() - timedelta(hours=24)).isoformat(timespec='milliseconds') + "Z"
lte = datetime.datetime.utcnow().isoformat(timespec='milliseconds') + "Z"

# Elasticsearch query body
body = {
    "aggs": {
        "2": {
            "terms": {
                "field": "src_ip.keyword",
                "order": {
                    "_count": "desc"
                },
                "size": 10,
                "shard_size": 25
            }
        }
    },
    "size": 0,
    "fields": [
        {
            "field": "@timestamp",
            "format": "date_time"
        },
        {
            "field": "end_time",
            "format": "date_time"
        },
        {
            "field": "flow.end",
            "format": "date_time"
        },
        {
            "field": "flow.start",
            "format": "date_time"
        },
        {
            "field": "start_time",
            "format": "date_time"
        },
        {
            "field": "time_iso8601",
            "format": "date_time"
        },
        {
            "field": "timestamp",
            "format": "date_time"
        },
        {
            "field": "tls.notafter",
            "format": "date_time"
        },
        {
            "field": "tls.notbefore",
            "format": "date_time"
        }
    ],
    "script_fields": {},
    "stored_fields": ["*"],
    "runtime_mappings": {},
    "_source": {
        "excludes": []
    },
    "query": {
        "bool": {
            "must": [],
            "filter": [
                {
                    "query_string": {
                        "query": "*"
                    }
                },
                {
                    "bool": {
                        "should": [
                            {"bool": {"should": [{"term": {"type.keyword": "Adbhoney"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Ciscoasa"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "CitrixHoneypot"}}],
                                      "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "ConPot"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Cowrie"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Ddospot"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Dicompot"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Dionaea"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "ElasticPot"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Endlessh"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Glutton"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Hellpot"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Heralding"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Honeytrap"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Honeypots"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Log4pot"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Ipphoney"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Mailoney"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Medpot"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Redishoneypot"}}],
                                      "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Tanner"}}], "minimum_should_match": 1}},
                            {"bool": {"should": [{"term": {"type.keyword": "Wordpot"}}], "minimum_should_match": 1}}
                        ],
                        "minimum_should_match": 1
                    }
                },
                {
                    "range": {
                        "@timestamp": {
                            "format": "strict_date_optional_time",
                            "gte": gte,
                            "lte": lte
                        }
                    }
                }
            ],
            "should": [],
            "must_not": [
                {
                    "match_phrase": {
                        "src_ip.keyword": ""
                    }
                }
            ]
        }
    }
}

url = "http://127.0.0.1:64298/logstash-*/_search"

try:
    # Execute Elasticsearch query
    resp = requests.get(url, json=body)
    resp.raise_for_status()
    resp_data = resp.json()

    # Process results
    buckets = resp_data.get('aggregations', {}).get('2', {}).get('buckets', [])
    message = f'timestamp:{lte}; top10:'

    if not buckets:
        message += "No attacks"
    else:
        for result in buckets:
            ip_address = result['key']
            count = result['doc_count']
            message += f'{ip_address}\\t{count}\\n'

    message += ';\n'

except Exception as e:
    # Error handling
    message = f'timestamp:{lte}; top10:Error fetching data: {str(e)};\n'

# Output and logging
print(message)
with open("/data/top_10/log/top_10.log", "a") as f:
    f.write(message)