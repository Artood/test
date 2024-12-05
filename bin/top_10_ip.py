#!/usr/bin/python3  
import json 
import requests 
import datetime 
import sys 
from datetime import timedelta 
import os 


gte = (datetime.datetime.utcnow() - timedelta(hours=24)).isoformat(timespec='milliseconds') + "Z" 
lte = datetime.datetime.utcnow().isoformat(timespec='milliseconds') + "Z"


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
  "stored_fields": [
    "*"
  ],
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
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Adbhoney"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Ciscoasa"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "CitrixHoneypot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "ConPot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Cowrie"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Ddospot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Dicompot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Dionaea"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "ElasticPot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Endlessh"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Glutton"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Hellpot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Heralding"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Honeytrap"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Honeypots"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Log4pot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Ipphoney"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                     "term": {
                        "type.keyword": "Mailoney"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Medpot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Redishoneypot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Tanner"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "term": {
                        "type.keyword": "Wordpot"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              }
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



#gte = (datetime.datetime.utcnow() - timedelta(hours=24)).isoformat(timespec='milliseconds') + "Z" 
#lte = datetime.datetime.utcnow().isoformat(timespec='milliseconds') + "Z"

url = "http://127.0.0.1:64298/logstash-*/_search"

#message = (f'{{"timestamp":"{lte}","top10":"')
message =  (f'timestamp:{lte}; top10:')
resp = (requests.get(url, json=body)).text 
#print(resp)
for result in json.loads(resp) ['aggregations']["2"]['buckets']:
    ip_address = result['key']
    count = result['doc_count']
    #message += (f'{{"ip_address":"{ip_address}","count":{count}}}\n')
    #message += (f'{{"ip_address":"{ip_address}","count":{count},"timestamp":"{lte}"}}\n')
    #message += (f'{number}.\\t{ip_address}\\t{count}\\n')
    message += (f'{ip_address}\\t{count}\\n')
#message += (f'"}}\n')
message += ';\n'
print(message)

with open("/data/top_10/log/top_10.log", "a") as f: 
  f.write(message)








